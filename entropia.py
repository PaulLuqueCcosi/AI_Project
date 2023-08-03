import pandas as pd
import numpy as np

def calculate_entropia(data, columna):
    # Contar las ocurrencias de cada valor en la columna objetivo
    cont = data[columna].cont()
    
    # Calcular la proporción de cada valor en la columna objetivo
    proporcion = cont / len(data)
    
    # Calcular la entropía
    entropia = -np.sum(proporcion * np.log2(proporcion))
    return entropia

# Lectura de datos procesados
data = pd.read_csv('datos_procesados.csv')
columna_Resultado = 'Resultado'
entropia = calculate_entropia(data, columna_Resultado)
print("Entropía:", entropia)
