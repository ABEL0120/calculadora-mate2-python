from flask import Blueprint, render_template, request, jsonify
import math
import sympy
import re
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    f = data['f']
    x0 = float(data['x0'])
    y0 = float(data['y0'])
    xn = float(data['xn'])
    h = float(data['h'])
    resultado = euler_mejorado(f, x0, y0, xn, h)
    return jsonify({'message': 'Cálculo realizado con éxito.', 'resultado': resultado, 'status': 200})


def euler_mejorado(f, x0, y0, xn, h):
    x, y = sympy.symbols('x y')
    f_expr = sympy.sympify(f)
    puntos = [{"x": x0, "y": y0}]
    xi, yi = x0, y0
    while xi < xn:
        f_val = f_expr.subs({x: xi, y: yi})
        predictor = yi + h * f_val
        f_corrector = f_expr.subs({x: xi + h, y: predictor})
        yi_next = yi + (h / 2) * (f_val + f_corrector)
        xi = round(xi + h, 10)
        yi = yi_next
        puntos.append({"x": float(xi), "y": float(yi)})
    return puntos


def es_funcion_valida(cadena):
    try:
        # Intenta analizar la cadena como una expresión matemática
        func = cadena.replace("(",'').replace(")",'').replace('=','-').replace("e**x", str(sympy.exp(sympy.symbols('x'))))
        x = sympy.symbols('x')
        print(func)
        sympy.sympify(func)
        # Verifica si la cadena contiene la variable x
        if 'x' not in sympy.latex(sympy.sympify(func)):
            return False
        return True
    except (sympy.SympifyError, TypeError):
        return False