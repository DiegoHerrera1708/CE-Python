# Ejercicio 16: Crea dos cadenas, `cadena1` y `cadena2`, y concaténalas para formar una nueva cadena.

cadena1 = "Hola "
cadena2 = "Mundo"
cadenaFinal = cadena1 + cadena2
print(cadenaFinal)

# Ejercicio 17: Concatenar varias cadenas usando un bucle for y el operador `+`. Prueba también la función `join()`

palabras = ["Hola", "Mundo", "Python"]

palabra_final = ""
for p in palabras:
    palabra_final += p + " "

print(palabra_final)

palabra_final = ""

palabra_final = " ".join(palabras)

print(palabra_final)
