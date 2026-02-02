# Ejercicio 5.1:
# Crea un programa que pida al usuario su nombre y su edad, los guarde en variables y luego imprima un mensaje que diga
# "Hola, [nombre]. Tienes [edad] años". Escribe un comentario de una sola línea que describa el propósito de tu código.

# Este programa solicita al usuario su nombre y edad, y luego muestra un mensaje personalizado.
nombre = input("Por favor, ingresa tu nombre: ")
edad = input("Por favor, ingresa tu edad: ")
print(f"Hola, {nombre}. Tienes {edad}  años.")

# Ejercicio 5.2:
# Crea tres variables: una con un valor booleano, otra con un número y otra con una cadena de texto. Usa print() para
# mostrar los tres valores en una sola línea, separados por un guion. Escribe un comentario de varias líneas en el que expliques qué hace el código.

"""
Este código crea tres variables con diferentes tipos de datos: un booleano, un número y una cadena de texto.
Luego, utiliza la función print() para mostrar los valores de estas variables en una sola línea,
separados por un guion.
"""
booleano, num, text = True, 42, "Hola Mundo"
print(booleano, num, text, sep=" - ")

# Ejercicio 5.3:
# Realiza una operación matemática con variables que hayas asignado anteriormente y usa print() para mostrar el resultado
# de la operación. Comenta temporalmente una línea de código que imprima un valor para evitar que se ejecute.

valor1 = 10
# valor2 = 5
print(valor1 + valor2)
