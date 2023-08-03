from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

app = Flask(__name__, static_url_path = '/static')

# Lectura de datos procesados
data = pd.read_csv('datos_procesados.csv')
X = data.drop('Resultado', axis=1)
Y = data['Resultado']

# Datos en conjuntos de entrenamiento 70% y prueba 30% 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Cargar el metodo del algoritmo de decision
ent_modelo = DecisionTreeClassifier()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los valores ingresados por el usuario
        embarazos = int(request.form['embarazos'])
        glucosa = int(request.form['glucosa'])
        presion_arterial = int(request.form['presion_arterial'])
        grosor_piel = int(request.form['grosor_piel'])
        insulina = int(request.form['insulina'])
        imc = float(request.form['imc'])
        diabetes_genealogia = float(request.form['diabetes_genealogia'])
        edad = int(request.form['edad'])

        # Entrenamiento del modelo
        ent_modelo.fit(X_train, Y_train)

        # Realizar la predicción utilizando el modelo
        features = [[embarazos, glucosa, presion_arterial, grosor_piel, insulina, imc, diabetes_genealogia, edad]]
        prediction = ent_modelo.predict(features)

        # Realizar predicciones en los datos de prueba
        y_pred = ent_modelo.predict(X_test)

        # Calcular la precisión del modelo en los datos de prueba
        error_margin = accuracy_score(Y_test, y_pred)
        error_margin = round(abs(error_margin - 1) * 100,0)

        # Mostrar el resultado
        if prediction[0] == 0:
            result = "No tiene diabetes."
        else:
            result = "Tiene diabetes."
        return render_template('index.html', result = result, error_margin = error_margin)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
