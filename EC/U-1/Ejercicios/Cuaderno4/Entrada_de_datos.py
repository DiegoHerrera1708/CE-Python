# Ejercicio 7:
# Solicita el nombre del usuario y muéstralo en pantalla.

nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")

# Ejercicio 8:
# Solicita al usuario dos números, realiza operaciones matemáticas con ellos y muestra el resultado.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# Ejercicio 9:
"""
Solicita al usuario que introduzca varios números separados por comas, 
luego convierte esa entrada en una lista de números y muestra la suma de esos números (emplea la función 'sum').
"""

entrada = [input("Introduce varios números separados por comas: ")]
numeros = [int(num) for num in entrada[0].split(",")]
print(f"Números introducidos: {numeros}")
print(f"Suma de los números: {sum(numeros)}")

# Ejercicio 10:
"""
Solicita al usuario una frase y convierte esa frase en una lista de palabras. 
Luego, muestra la longitud de la lista y la palabra más larga. Emplea la función 'max(palabras, key=len)'.
"""

frase = input("Introduce una frase: ")
palabras = frase.split()
print(f"Número de palabras: {len(palabras)}")
print(f"Palabra más larga: {max(palabras, key=len)}")
