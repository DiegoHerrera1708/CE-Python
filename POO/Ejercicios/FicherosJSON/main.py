from iris_flower import iris_flower
import json
import os

'''
Implementar una rutina en Python que lea el contenido del dataset escogido y lo muestre formateado por pantalla, el formato debe ser una lista con el nombre de cada campo seguido de su valor, algo como esto:
Nombre: Javier
Apellidos: Caselli Fernández
Dirección: Mi casa
Email: jcasfer695@g.educaand.es
Nombre: María
Apellidos: Pérez López
Dirección: Su casa
Email: maria@g.educaand.es

'''

def leer_fichero_json(ruta_fichero):
    with open(ruta_fichero, 'r') as fichero:
        datos = json.load(fichero)
        lista_iris = []
        for item in datos:
            flor = iris_flower(
                sepal_length=float(item['sepal.length']),
                sepal_width=float(item['sepal.width']),
                petal_length=float(item['petal.length']),
                petal_width=float(item['petal.width']),
                variety=str(item['variety'])
            )
            lista_iris.append(flor)
        return lista_iris
    
def mostrar_iris(lista_iris):
    for flor in lista_iris:
        print(f"Sepal Length: {flor.sepal_length}")
        print(f"Sepal Width: {flor.sepal_width}")
        print(f"Petal Length: {flor.petal_length}")
        print(f"Petal Width: {flor.petal_width}")
        print(f"Variety: {flor.variety}")
        print("---------------------------")
        
if __name__ == "__main__":
    ruta_fichero = os.path.join(os.path.dirname(__file__), 'iris.json')
    lista_iris = leer_fichero_json(ruta_fichero)
    mostrar_iris(lista_iris)

    