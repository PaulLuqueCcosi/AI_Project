import pandas as pd

# Lectura de datos SIN procesar
data = pd.read_csv('diabetes.csv')

# Eliminar las filas con más de 4 embarazos
data = data[data['Embarazos'] <= 4]

# Guardar datos procesados
data.to_csv('datos_procesados.csv', index = False)