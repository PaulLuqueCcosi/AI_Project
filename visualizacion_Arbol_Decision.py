import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pydotplus
from IPython.display import Image

# Lectura de datos procesados
data = pd.read_csv('datos_procesados.csv')
X = data.drop('Resultado', axis = 1)
y = data['Resultado']

# Entrenamiento del modelo
ent_modelo = DecisionTreeClassifier()
ent_modelo.fit(X, y)

# Guardar el árbol de decisión en un archivo de imagen
graph_data = tree.export_graphviz(ent_modelo, out_file = None, feature_names = X.columns)
graph = pydotplus.graph_from_gra(graph_data)
graph.write_png('arbol_decision.png')
Image(graph.create_png())