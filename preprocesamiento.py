import pandas as pd

def cargar_diabetes_data(source):
    """
    Carga los datos de diabetes desde una fuente especificada (archivo CSV o conexión a base de datos).
    """
    if source.endswith('.csv'):
        # Cargar desde un archivo CSV
        data = pd.read_csv(source)
    elif source.startswith('database:'):
        # Cargar desde una base de datos (ejemplo: "database:nombre_tabla")
        table_name = source.split(':')[1]
        # Agregar código para conectarse a la base de datos y obtener los datos
        # data = obtener_datos_desde_base_de_datos(table_name)
    elif source.startswith('text:'):
        # Cargar desde un archivo de texto (ejemplo: "text:archivo.txt")
        file_name = source.split(':')[1]
        # Agregar código para leer los datos desde el archivo de texto
        # data = pd.read_txt(file_name)
    else:
        raise ValueError("Fuente de datos no válida. Use un archivo CSV, 'database:nombre_tabla' o 'text:archivo.txt'.")
    
    return data

def preprocesar_diabetes_data(data):
    """
    Realiza el preprocesamiento de los datos de diabetes.
    """
    # Manejo de datos faltantes
    data.dropna(inplace=True)
    
    # Filtrar las filas con más de 4 embarazos
    data = data[data['Embarazos'] <= 4]
    
    return data

if __name__ == "__main__":
    name_file_out = 'datos_procesados.csv'
    # Especificar la fuente de datos (por ejemplo, un archivo CSV)
    data_source = 'diabetes.csv'

    # Cargar los datos de diabetes desde la fuente especificada
    diabetes_data = cargar_diabetes_data(data_source)

    # Realizar el preprocesamiento de los datos
    diabetes_data = preprocesar_diabetes_data(diabetes_data)

    # Guardar los datos procesados en un nuevo archivo CSV
    diabetes_data.to_csv(name_file_out, index=False)