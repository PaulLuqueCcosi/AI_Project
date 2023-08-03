import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def curva_Aprendizaje(estimator, X, y):
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=10, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 9))

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, 'o-', color='r', label='Puntuación de entrenamiento')
    plt.plot(train_sizes, test_mean, 'o-', color='g', label='Puntuación de validación cruzada')
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color='r')
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1, color='g')
    plt.xlabel('Tamaño del conjunto de entrenamiento')
    plt.ylabel('Puntaje')
    plt.title('Curva de aprendizaje')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

def calculo_sesgo(precision_entrenamiento, precision):
    print("Sesgo:", precision_entrenamiento - precision)

# Lectura de datos procesados
data = pd.read_csv('datos_procesados.csv')
X = data.drop('Resultado', axis=1)
Y = data['Resultado']

X_entrenamiento, X_test, Y_entrenamiento, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 20)

# Entrenamiento del modelo
clf = DecisionTreeClassifier()
clf.fit(X_entrenamiento, Y_entrenamiento)

# Predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo en los datos de entrenamiento
precision_entrenamiento = accuracy_score(Y_entrenamiento, clf.predict(X_entrenamiento))

# Realizar la validación cruzada
score = cross_val_score(clf, X, Y, cv = 10)

# Precisión del modelo en los datos de prueba
precision = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", precision)

# Resultados de la validación cruzada
print("Puntuaciones de la validación cruzada:", score)
print("Precisión promedio de la validación cruzada:", score.mean())
calculo_sesgo(precision_entrenamiento,precision)

# Grafica de la curva de aprendizaje
curva_Aprendizaje(clf, X_entrenamiento, Y_entrenamiento)