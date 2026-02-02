"""
Ejercicio 34: Crea un programa que pida al usuario unos números separados por comas.
Luego, convierte esa lista en una lista de enteros, calcula la suma y el promedio, y verifica si el promedio está en la lista.
Puedes obtener una lista a partir de los números separados por coma con la función `split(',')` aplicada sobre la cadena de caracteres.
Después puedes convertir cada elemento de la lista en un entero, bien recorriendo la lista elemento a elemento, bien usando una función `map(int, lista)`.
Puedes sumar los elementos de la lista con la función `sum(lista)`. Cuida de calcular el promedio solo si la longitud de la lista es mayor que cero.
"""

numeros = input("Dame unos numeros separados por comas: \n")
lista = [int(n) for n in numeros.split(",")]
suma = sum(lista)
promedio = sum(lista) / len(lista)
if promedio in lista:
    print("el promedio esta en la lista")
else:
    print("El promedio no esta en la lista")
