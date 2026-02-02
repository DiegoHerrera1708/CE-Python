# Ejercicio 20: Usa la función `len()` para obtener la longitud de una cadena.

c = "hola mundo"
print(len(c))

# Ejercicio 21: Crea una función que calcule la longitud de una cadena sin usar `len()`.

contador = 0
for x in c:
    contador += 1

print(contador)
