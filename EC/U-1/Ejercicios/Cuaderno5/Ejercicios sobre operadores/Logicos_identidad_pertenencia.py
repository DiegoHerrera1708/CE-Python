# Ejercicio 8: Usa los operadores lógicos `and`, `or` y `not` para comprobar las condiciones en una variable booleana.

print("True and False:", True and False)
print("True or False:", True or False)
print("not False", not False)
print("not True", not True)

# Ejercicio 9: Crea dos listas con los mismos elementos y verifica si son la misma referencia de objeto usando `is` y `is not`. Explica el comportamiento.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(
    lista1[1] is lista2[1]
)  # Da True debido a que lista1[1] es el mismo numero que lista2[1]
print(
    lista1[2] is not lista2[2]
)  # Da False debido a que lista1[2] no es el mismo numero que lista2[2]

# Ejercicio 10: Crea una lista de números del 1 al 10 y verifica si el número 5 está dentro de esa lista usando el operador `in`.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if 5 in lista:
    print("El numero 5 esta en la lista")
else:
    print("No se encuentra el numero")

# Ejercicio 11: Verifica si una cadena contiene una subcadena utilizando `in`. ¿Qué sucede si la subcadena no existe?

a = "Hola mundo"


if "a m" in a:
    print("La subcadena se encuentra en la cadena")
else:
    print("No se encuentra la subcadena dentro de la cadena")

if "t" in a:
    print()
else:
    print("No se encuentra")  # La cadena returna False
