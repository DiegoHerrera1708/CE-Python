# Ejercicio 1:
"""
Escribe tres expresiones numéricas: una que utilice enteros, otra con números decimales,
y otra con una mezcla de ambos. Muestra los resultados de estas expresiones.
"""
x = 200
y = 3.14
z = x * y
print(x, y, z)

# Ejercicio 2:
"""
Crea cadenas utilizando comillas simples, dobles y triples. Muestra cómo funcionan y cuándo es conveniente usarlas. Pregunta: 
¿Qué pasa si usas comillas dobles dentro de comillas dobles o comillas simples dentro de comillas simples?
"""

print("Comillas simples")
print("Comillas dobles")
print(
    """Comillas triples
Permiten múltiples líneas
"""
)

# Ejercicio 3:
"""
Muestra cómo insertar caracteres especiales, como el salto de línea (\n), 
tabulación (\t), y comillas dentro de cadenas. Pregunta: ¿Qué efecto tiene cada uno de los caracteres especiales?
"""

print("Primera línea\nSegunda línea")  # \n crea un salto de línea
print("Columna 1\tColumna 2")  # \t crea una tabulación
print(
    "Comillas simples: ' y comillas dobles: \""
)  # \' y \" permiten incluir comillas dentro de cadenas

# Ejercicio 4:
"""
Demuestra cómo insertar valores en cadenas utilizando f-strings, .format(), y el operador %. Pregunta: ¿Cuál de estos métodos te parece más sencillo de usar? ¿Por qué?
"""

nombre = "Ana"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # f-string
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))  # .format()
print("Mi nombre es %s y tengo %d años." % (nombre, edad))  # operador %

# El método mas sencillo es f-string porque es más legible y directo.

# Ejercicio 5:
"""
Emplea la alineación de texto en cadenas para alinear valores a la izquierda, derecha o centrados. Utiliza .format() o f-strings. 
Pregunta: ¿Cómo puedes cambiar la alineación de las columnas usando los métodos vistos?
"""

palabra = "Python"
print(f"|{palabra:<10}|")  # Alineado a la izquierda
print(f"|{palabra:>10}|")  # Alineado a la derecha
print("|{:^10}|".format(palabra))  # Centrado

# Ejercicio 6:
"""
Realiza ejemplos de formatos de texto con números decimales, enteros, y porcentajes. Usa f-strings o .format(). 
Pregunta: ¿Cómo puedes redondear el precio a un número específico de decimales? ¿Cómo puedes mostrar un número como porcentaje?
"""

a, b, c, d = 4, 50.22789, 0.85, -32

print(f"Decimal: {a}, Binario: {a:b}, Hexadecimal: {a:x}, Octal: {a:o}")
print(f"Con separador de millares: {b:,.2f}")  # Redondea a 2 decimales
print(f"Con signo explícito: {d}")
print(f"Con ceros a la izquierda: {42:06d}")
print(f"Porcentaje: {c:.2%}")
