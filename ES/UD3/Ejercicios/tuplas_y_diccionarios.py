# 18. Dada una lista de pares (tuplas) (nombre, edad), encuentra la edad máxima.

lista = [("jose", 23), ("mario", 18), ("alejandra", 51), ("maria", 25)]

edadmax = 0
index = None
for i in range(len(lista)):
    if lista[i][1] > edadmax:
        edadmax = lista[i][1]
        index = lista[i]

print(f"La persona que tiene la edad maxima es {index[0]}, con {index[1]} años")

# 19. Dada una tupla de números, crea otra tupla con solo los positivos.

tupla = (2, 3, 5, 2, 6, -2, -1, 4, -2)
positivos = tuple(filter(lambda x: x > 0, tupla))
print(positivos)

# 20. Intercambia los valores de dos variables usando tuplas (sin variable auxiliar).

tupla1 = (1, 2, 3, 4, 5, 6)
tupla2 = (7, 8, 9, 10, 11, 12)
tupla1, tupla2 = tupla2, tupla1
print(tupla1)
print(tupla2)

# 21. Dada una lista de tuplas (producto, precio), ordena por precio sin modificar el formato.

lista = [("producto1", 1.23), ("producto2", 0.99), ("producto3", 2.50), ("producto4", 1.50)]

lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)

'''22. Crear una aplicación que funcione como un diccionario español-inglés. Mostrará un menú con
las siguientes opciones:
-n: pide la palabra en español y la traducción al inglés y las guarda en el diccionario
-t: pide una palabra en español y muestra la traducción al inglés. Si no existe muestra un error
-b: pide una palabra en español y la borra del diccionario. Si la palabra no existe dará un error
(pide confirmación)
-c: modifica una entrada del diccionario pidiendo la palabra en español e inglés. Si la palabra
no existe dará un error
-e: lista todas las palabras en español
-i: lista todas las palabras en inglés
-l: lista en una tabla todas las palabras en español y en inglés
-x: elimina todas las palabras del diccionario (pidiendo confirmación)
-0: sale de la aplicación'''

print('''
-n: pide la palabra en español y la traducción al inglés y las guarda en el diccionario
-t: pide una palabra en español y muestra la traducción al inglés. Si no existe muestra un error
-b: pide una palabra en español y la borra del diccionario. Si la palabra no existe dará un error
(pide confirmación)
-c: modifica una entrada del diccionario pidiendo la palabra en español e inglés. Si la palabra
no existe dará un error
-e: lista todas las palabras en español
-i: lista todas las palabras en inglés
-l: lista en una tabla todas las palabras en español y en inglés
-x: elimina todas las palabras del diccionario (pidiendo confirmación)
-0: sale de la aplicación''')
diccionario = {}
while True:
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "-n":
            palabra_espanol = input("Ingrese la palabra en español: ")
            palabra_ingles = input("Ingrese la traducción al inglés: ")
            diccionario[palabra_espanol] = palabra_ingles
        case "-t":
            palabra_espanol = input("Ingrese la palabra en español: ")
            if palabra_espanol in diccionario:
                print(f"La traducción al inglés de {palabra_espanol} es {diccionario[palabra_espanol]}")
            else:
                print("La palabra no existe en el diccionario.")
        case "-b":
            palabra_espanol = input("Ingrese la palabra en español: ")
            if palabra_espanol in diccionario:
                confirmacion = input(f"¿Está seguro que desea eliminar {palabra_espanol}? (s/n): ")
                if confirmacion.lower() == "s":
                    del diccionario[palabra_espanol]
                    print(f"{palabra_espanol} ha sido eliminada del diccionario.")
                else:
                    print("Operación cancelada.")
            else:
                print("La palabra no existe en el diccionario.")
        case "-c":
            palabra_espanol = input("Ingrese la palabra en español: ")
            if palabra_espanol in diccionario:
                palabra_ingles = input("Ingrese la nueva traducción al inglés: ")
                diccionario[palabra_espanol] = palabra_ingles
                print(f"La traducción de {palabra_espanol} ha sido actualizada a {palabra_ingles}.")
            else:
                print("La palabra no existe en el diccionario.")
        case "-e":
            print("Palabras en español:")
            for palabra in diccionario.keys():
                print(palabra)
        case "-i":
            print("Palabras en inglés:")
            for palabra in diccionario.values():
                print(palabra)
        case "-l":
            print("Palabra en español | Traducción al inglés")
            print("-" * 30)
            for palabra_espanol, palabra_ingles in diccionario.items():
                print(f"{palabra_espanol:20} | {palabra_ingles}")
        case "-x":
            confirmacion = input("¿Está seguro que desea eliminar todas las palabras del diccionario? (s/n): ")
            if confirmacion.lower() == "s":
                diccionario.clear()
                print("Todas las palabras han sido eliminadas del diccionario.")
            else:
                print("Operación cancelada.")  
        case "0":
            print("Saliendo de la aplicación.")
            break   
        case _:
            print("Opción no válida. Por favor, ingrese una opción válida.")