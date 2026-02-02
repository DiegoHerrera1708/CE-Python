# Ejercicio 28: Realiza una operación entre un número entero y un número decimal. Muestra el resultado y explica cómo Python maneja la conversión implícita.

print(
    5 + 5.2
)  # Python a veces convierte automáticamente los tipos cuando no hay pérdida de información al hacer la transformación:

# Ejercicio 29: Convierte un número flotante en un número entero utilizando `int()`. ¿Qué sucede con los decimales?

print(int(4.2))  # Quita los decimales y deja el numero entero

# Ejercicio 30: Convierte una cadena que contiene un número a un número entero o flotante utilizando `int()` o `float()`. ¿Qué sucede si la cadena no es un número válido?

a = "10"
b = int(a)
print(b)
a = "11.5"
b = float(a)
print(a)
a = "Hola"
b = int(a)  # ValueError
print(b)


# Ejercicio 31: Realiza una conversión explícita entre tipos `int` o `float` y `str` y muestra los resultados.

a = "11.2"
b = float(a)
print(b)  # float
c = int(b)
print(c)  # int
b = str(c)
print(type(b))  # str
