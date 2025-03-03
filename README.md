# **Proyecto Calculadora**

---

### Descripción del Proyecto:

Esta aplicación está hecha para resolver problemas de:

- Euler Mejorado
- Newton-Raphson
- Runge-Kutta de Cuarto Orden

Proyecto en [GitHub](https://github.com/ABEL0120/calculadora-mate2-python).

---

### Instalación:

Para comenzar a utilizar el Proyecto Calculadora, sigue estos pasos de instalación:

1. **Librerías Necesarias:**
   ```bash
   # Instala con estos comandos:
   pip install flask
   pip install flask-cors
   pip install sympy
   ```
2. **Iniciar Proyecto:**
   ```bash
   # Iniciar con:
   python3 serve.py
   ```
   La aplicación se iniciará en [http://localhost:5000/](http://localhost:5000/).

---

### Uso

#### Interfaz de Usuario

1. Abre tu navegador web y navega a [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
2. Verás una página con tres botones: **Euler Mejorado**, **Newton-Raphson** y **Runge-Kutta**. Haz clic en el método que deseas utilizar.

#### Método de Euler Mejorado

1. Haz clic en el botón **Euler Mejorado**.
2. Completa los campos del formulario:
   - **f(x, y)**: Ingresa la función en términos de `x` y `y`. Ejemplo: `x + y`.
   - **x0**: Ingresa el valor inicial de `x`. Ejemplo: `0`.
   - **y0**: Ingresa el valor inicial de `y`. Ejemplo: `1`.
   - **xn**: Ingresa el valor final de `x`. Ejemplo: `1`.
   - **h**: Ingresa el tamaño del paso. Ejemplo: `0.1`.
3. Haz clic en **Calcular**.
4. Los resultados se mostrarán en una tabla con las columnas `N`, `Xn`, `Yn`, `Yp`, `Yr` y `Error`.

#### Método de Newton-Raphson

1. Haz clic en el botón **Newton-Raphson**.
2. Completa los campos del formulario:
   - **x inicial**: Ingresa el valor inicial de `x`. Ejemplo: `1`.
   - **Función f(x)**: Ingresa la función en términos de `x`. Ejemplo: `x**2 - 2`.
   - **Precisión (decimales)**: Ingresa el número de decimales de precisión. Ejemplo: `6`.
3. Haz clic en **Calcular**.
4. Los resultados se mostrarán en una tabla con las columnas `Iteración`, `x0`, `f(x0)`, `df(x0)` y `x1`. Además, se mostrará la raíz calculada.

#### Método de Runge-Kutta

1. Haz clic en el botón **Runge-Kutta**.
2. Completa los campos del formulario:
   - **f(x, y)**: Ingresa la función en términos de `x` y `y`. Ejemplo: `x + y`.
   - **x0**: Ingresa el valor inicial de `x`. Ejemplo: `0`.
   - **y0**: Ingresa el valor inicial de `y`. Ejemplo: `1`.
   - **xn**: Ingresa el valor final de `x`. Ejemplo: `1`.
   - **h**: Ingresa el tamaño del paso. Ejemplo: `0.1`.
3. Haz clic en **Calcular**.
4. Los resultados se mostrarán en una tabla con las columnas `N`, `Xn`, `Yn`, `K1`, `K2`, `K3`, `K4` y `Yn+1`.

#### Método de Bisección

1. Haz clic en el botón **Bisección**.
2. Completa los campos del formulario:
   - **Función f(x)**: Ingresa la función en términos de `x`. Ejemplo: `x**2 - 4`.
   - **a**: Ingresa el valor inicial del intervalo `a`. Ejemplo: `0`.
   - **b**: Ingresa el valor final del intervalo `b`. Ejemplo: `3`.
   - **Tolerancia**: Ingresa el valor de la tolerancia. Ejemplo: `0.001`.
3. Haz clic en **Calcular**.
4. Los resultados se mostrarán en una tabla con las columnas `Iteración`, `a`, `b`, `c`, `f(c)` y `Error`.

---

### Ejemplos de Funciones

- **Euler Mejorado y Runge-Kutta**:

  - `f(x, y) = x + y`
  - `f(x, y) = x**2 + y**2`
  - `f(x, y) = sin(x) + cos(y)`

- **Newton-Raphson**:
  - `f(x) = x**2 - 2`
  - `f(x) = x**3 - x - 1`
  - `f(x) = exp(x) - 3*x`

---

### Notas Importantes

- Indicar con `*` las multiplicaciones, no se aceptan dos caracteres juntos como `xy`.
  - Ejemplo:
    - **Incorrecto**: `2 * xy`
    - **Correcto**: `2 * x * y`
- Indicar con `**` las potencias, no se aceptan otros caracteres para indicarla como `^`.
  - Ejemplo:
    - **Incorrecto**: `2 * (x ^ 2) * y`
    - **Correcto**: `2 * (x ** 2) * y`
- Indicar con `e**(operación)` el cálculo del número de Euler, no se aceptan `e(operación)`.
  - Ejemplo:
    - **Incorrecto**: `2 * e(x ^ 2 * x) * y`
    - **Correcto**: `2 * e**((x ** 2) * x) * y`
- Indicar con `√(operación)` el cálculo de la raíz, no se aceptan otras formas para calcular raíz.
  - Ejemplo:
    - **Incorrecto**: `2 * √xy`
    - **Correcto**: `2 * √(x * y)`

En el archivo `ejemplos.txt` están algunos ejemplos para probar los 3 métodos.
