# Ejercicio 22: Accede al primer, último y un elemento intermedio de una cadena utilizando índices.

c = "Python"

print(c[0])
print(c[-1])

# Ejercicio 23: Intenta acceder a un índice fuera del rango y maneja el error con un `try`-`except`. La excepción a manejar sería `IndexError`.

try:
    print(c[9])
except IndexError:
    print("Indice fuera de rango")
