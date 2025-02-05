from flask import Blueprint, render_template, request, jsonify
import math
import sympy

main_bp = Blueprint('main', __name__)

# VIEWS
@main_bp.route('/')
def index():
    return render_template('index.html')

# APIS
@main_bp.route('/calcular', methods=['POST'])

#FUNCIONES
def calcular():
    data = request.json
    errores = validar_entrada(data)
    if errores:
        return jsonify({'message': 'Error en los datos ingresados.', 'errores': errores, 'status': 400}), 400
    
    f = data['f']
    x0 = float(data['x0'])
    y0 = float(data['y0'])
    xn = float(data['xn'])
    h = float(data['h'])
    tabla = euler_mejorado(f, x0, y0, xn, h)
    print(tabla)
    return jsonify({'message': 'Cálculo realizado con éxito.', 'resultados': tabla, 'status': 200})


def euler_mejorado(f, x0, y0, xn, h):
    x, y = sympy.symbols('x y')
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
        tabla.append({
            "N": n,
            "Xn": round(xi, 6), 
            "Yn": round(yi, 6),
            "Yr": round(yr, 6) if yr else "N/A",
            "Yp": round(predictor, 6),
            "error": round(error, 6) if error != "N/A" else "N/A"
        })        
        xi = round(xi + h, 6)
        yi = yi_next
        n += 1
    return tabla
   
def calcular_valor_real(a):
    resultado = math.exp(( 0.2 * ( a ** 2 ) ) - 0.2)
    return resultado

def validar_entrada(data):
    errores = []
    try:
        x, y = sympy.symbols('x y')
        f_expr = sympy.sympify(data['f']) 
        if not any(var in f_expr.free_symbols for var in (x, y)):
            errores.append("La función debe depender de 'x' o 'y'.")
    except (sympy.SympifyError, KeyError):
        errores.append("La función f(x, y) no es válida o no fue proporcionada.")
    for key in ['x0', 'y0', 'xn', 'h']:
        if key not in data:
            errores.append(f"El valor '{key}' es requerido.")
        else:
            try:
                float(data[key])
            except ValueError:
                errores.append(f"El valor '{key}' debe ser un número válido.")
    return errores