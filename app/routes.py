from flask import Blueprint, render_template, request, jsonify
import math
import sympy
from sympy import lambdify, sympify

main_bp = Blueprint("main", __name__)


# VIEWS
@main_bp.route("/")
def index():
    return render_template("index.html")


# APIS EULER
@main_bp.route("/calcular/euler", methods=["POST"])
def calcularEuler():
    data = request.json
    errores = validar_entrada(data)
    if errores:
        return (
            jsonify(
                {
                    "message": "Error en los datos ingresados.",
                    "errores": errores,
                    "status": 400,
                }
            ),
            400,
        )

    f = data["f"]
    x0 = float(data["x0"])
    y0 = float(data["y0"])
    xn = float(data["xn"])
    h = float(data["h"])
    tabla = euler_mejorado(f, x0, y0, xn, h)
    print(tabla)
    return jsonify(
        {"message": "Cálculo realizado con éxito.", "resultados": tabla, "status": 200}
    )


# Funcion Newton
@main_bp.route("/calcular/newton", methods=["POST"])
def calcularNewton():
    data = request.json
    f = data["funcion"]
    x_ini = float(data["x_ini"])
    resultados, tabla = newton_raphson(f, x_ini)
    resultados["raiz"] = float(resultados["raiz"])
    resultados["iteraciones"] = int(resultados["iteraciones"])
    for iteracion in tabla:
        iteracion["x0"] = round(float(iteracion["x0"]), 5)
        iteracion["f(x0)"] = round(float(iteracion["f(x0)"]), 5)
        iteracion["df(x0)"] = round(float(iteracion["df(x0)"]), 5)
        iteracion["x1"] = round(float(iteracion["x1"]), 5)
    return jsonify(
        {
            "message": "Cálculo realizado con éxito.",
            "resultados": resultados,
            "tabla": tabla,
            "status": 200,
        }
    )


# Funcion Runge-Kutta
@main_bp.route("/calcular/runge-kutta", methods=["POST"])
def calcularRungeKutta():
    data = request.json
    errores = validar_entrada(data)
    if errores:
        return (
            jsonify(
                {
                    "message": "Error en los datos ingresados.",
                    "errores": errores,
                    "status": 400,
                }
            ),
            400,
        )

    f = data["f"]
    x0 = float(data["x0"])
    y0 = float(data["y0"])
    xn = float(data["xn"])
    h = float(data["h"])
    tabla = runge_kutta(f, x0, y0, xn, h)
    print(tabla)
    return jsonify(
        {"message": "Cálculo realizado con éxito.", "resultados": tabla, "status": 200}
    )


def euler_mejorado(f, x0, y0, xn, h):
    x, y = sympy.symbols("x y")
    f_expr = sympy.sympify(f)
    tabla = []
    xi, yi = x0, y0
    n = 0
    while xi <= xn:
        f_val = float(f_expr.subs({x: xi, y: yi}))
        predictor = yi + h * f_val
        f_corrector = float(f_expr.subs({x: xi + h, y: predictor}))
        yi_next = yi + (h / 2) * (f_val + f_corrector)
        yr = calcular_valor_real(xi)
        error = abs(yr - yi) if yr is not None else "N/A"
        tabla.append(
            {
                "N": n,
                "Xn": round(xi, 6),
                "Yn": round(yi, 6),
                "Yr": round(yr, 6) if yr else "N/A",
                "Yp": round(predictor, 6),
                "error": round(error, 6) if error != "N/A" else "N/A",
            }
        )
        xi = round(xi + h, 6)
        yi = yi_next
        n += 1
    return tabla


def newton_raphson(f, x0):
    f_expr = sympy.sympify(f)
    df = sympy.diff(f_expr)
    x = sympy.symbols("x")
    tol = 1e-6
    max_iter = 100
    iteracion = 0
    tabla = []
    while iteracion < max_iter:
        f_val = f_expr.subs(x, x0).evalf()
        df_val = df.subs(x, x0).evalf()
        if df_val == 0:
            break
        x1 = x0 - f_val / df_val
        if abs(f_val) < tol:
            break
        tabla.append(
            {
                "iteracion": iteracion,
                "x0": x0,
                "f(x0)": f_val,
                "df(x0)": df_val,
                "x1": x1,
            }
        )
        x0 = x1
        iteracion += 1
    resultados = {"raiz": x1, "iteraciones": iteracion}
    return resultados, tabla


def runge_kutta(f, x0, y0, xn, h):
    x, y = sympy.symbols("x y")
    f_expr = sympify(f)
    f_lambda = lambdify((x, y), f_expr)
    tabla = []
    xi, yi = x0, y0
    n = 0
    while xi < xn:
        k1 = f_lambda(xi, yi)
        k2 = f_lambda(xi + h / 2, yi + (h * k1) / 2)
        k3 = f_lambda(xi + h / 2, yi + (h * k2) / 2)
        k4 = f_lambda(xi + h, yi + h * k3)
        yi_next = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        tabla.append(
            {
                "N": n,
                "Xn": round(xi, 6),
                "Yn": round(yi, 6),
                "K1": round(k1, 6),
                "K2": round(k2, 6),
                "K3": round(k3, 6),
                "K4": round(k4, 6),
                "Yn+1": round(yi_next, 6),
            }
        )
        yi = yi_next
        xi += h
        n += 1
    return tabla


def calcular_valor_real(a):
    resultado = math.exp((0.2 * (a**2)) - 0.2)
    return resultado


def validar_entrada(data):
    errores = []
    try:
        x, y = sympy.symbols("x y")
        f_expr = sympy.sympify(data["f"])
        if not any(var in f_expr.free_symbols for var in (x, y)):
            errores.append("La función debe depender de 'x' o 'y'.")
    except (sympy.SympifyError, KeyError):
        errores.append("La función f(x, y) no es válida o no fue proporcionada.")
    for key in ["x0", "y0", "xn", "h"]:
        if key not in data:
            errores.append(f"El valor '{key}' es requerido.")
        else:
            try:
                float(data[key])
            except ValueError:
                errores.append(f"El valor '{key}' debe ser un número válido.")
    return errores
