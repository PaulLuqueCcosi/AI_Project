import pandas as pd

def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)

# Lectura de datos procesados
data = pd.read_csv("datos_procesados.csv")

# Seleccion de la columna Edad
edades = data["Edad"]

# Definicion del rango
edad_min = 25
edad_bajo_riesgo = 35
edad_alto_riesgo = 50
edad_max = 65

# Calcular el grado de pertenencia a cada conjunto difuso para cada edad
joven = edades.apply(lambda x: trapezoidal(x, edad_min, edad_bajo_riesgo, edad_bajo_riesgo, edad_alto_riesgo))
adulto = edades.apply(lambda x: trapezoidal(x, edad_bajo_riesgo, edad_alto_riesgo, edad_alto_riesgo, edad_max))
adulto_mayor = edades.apply(lambda x: trapezoidal(x, edad_alto_riesgo, edad_max, 100, 100))

# Mostrar el grado de pertenencia para cada edad ingresada
for i, edad in enumerate(edades):
    print(f"Edad: {edad}, Grado de pertenencia a 'joven': {joven.iloc[i]}, Grado de pertenencia a 'adulto': {adulto.iloc[i]}, Grado de pertenencia a 'adulto_mayor': {adulto_mayor.iloc[i]}")
