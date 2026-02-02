# Ejercicio 24: Utiliza slicing para obtener una subcadena de una cadena original. Intenta obtener los primeros 3 y últimos 3 caracteres de una cadena.

c = "concatenar"
print(c[:3])
print(c[-3:])

# Ejercicio 25: Realiza un slicing inverso de una cadena (es decir, invertir la cadena).

cadena_inversa = ""

for i in range(1, len(c) + 1):
    cadena_inversa += c[-i]

print(cadena_inversa)
