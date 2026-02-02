# Ejercicio 32: Convierte una lista de números en una cadena utilizando `join()`. Luego, convierte la cadena de nuevo en una lista de enteros.

lista = [1, 2, 3, 4, 5, 2]
cadena = "".join([str(n) for n in lista])

print(cadena)

listaEnteros = []
for x in str(cadena):
    listaEnteros.append(int(x))

print(lista)

# Ejercicio 33: Convierte un diccionario en una lista de claves y luego en una lista de valores. Puedes utilizar los métodos .keys() y .values().
# Ambos métodos devuelven vistas del diccionario, que son iterables, y puedes convertirlos fácilmente en listas utilizando la función list().

dict = {"nombre": "Pablo", "edad": 12, "ciudad": "Malaga"}
print(dict)

lista_claves = list(dict.keys())
print(lista_claves)

lista_valores = list(dict.values())
print(lista_valores)
