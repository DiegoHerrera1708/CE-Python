# Ejercicio 11:
"""
Formatear la salida de una tabla. Solicita al usuario varias entradas para crear una tabla de datos. Por ejemplo, nombre, edad y ciudad, y luego alinea las columnas.
"""

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
ciudad = input("Introduce tu ciudad: ")

print(f"|{'Nombre':^16}|{'Edad':^6}|{'Ciudad':^16}|")
print(f"|{nombre:^16}|{edad:^6}|{ciudad:^16}|")

# Ejercicio 12:
"""
Cálculo de una media. Solicita al usuario una lista de números separados por comas, 
luego calcula y muestra la media de esos números. Emplea las funciones 'sum' y 'len' para calcular la media.
"""

numeros = input("Introduce una lista de números separados por comas: ")
lista_numeros = [int(num) for num in numeros.split(",")]
media = sum(lista_numeros) / len(lista_numeros)
print(f"La media de los números es: {media}")
