# Ejercicio 26: Usa un bucle `for` para imprimir cada carácter de una cadena por separado.

c = "Hola mundo"

for x in c:
    print(x)

# Ejercicio 27: Escribe una función que cuente cuántas veces aparece un carácter específico en una cadena.

contador = 0

for x in c:
    if x == "o":
        contador += 1

print("La letra 'o' esta:", contador, "veces en", c)
