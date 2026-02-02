# Ejercicio 1.1:
# Crea una variable llamada edad y asigna tu edad como valor. Luego, usa la función type() para verificar el tipo de la variable

edad = 25
print(type(edad))

# Ejercicio 1.2:
# Crea una variable llamada nombre y asigna tu nombre como valor. ¿De qué tipo es esta variable? Utiliza type() para verificarlo

nombre = "Diego"
print(type(nombre))

# Ejercicio 1.3:
# Asigna el valor True a una variable llamada es_estudiante. Usa la función type() para confirmar su tipo

es_estudiante = True
print(type(es_estudiante))

# Ejercicio 1.4:
# Crea una variable pi y asígnale el valor de pi con una precisión de 3 decimales (de forma manual). ¿Qué tipo tiene esta variable?

pi = 3.142
print(type(pi))

# Ejercicio 1.5:
# Crea una variable temperatura y asigna el valor 25. Usa del() para eliminar la variable y luego intenta imprimirla. ¿Qué error aparece?

temperatura = 25
del temperatura
# print(temperatura)  NameError: name 'temperatura' is not defined

# Ejercicio 1.6:
# Crea tres variables 'x', 'y', 'z' y asígnales valores. Luego, elimina la variable 'y' usando del() y verifica si puedes imprimir su valor

x, y, z = 10, 20, 30
del y
# print(y)  NameError: name 'y' is not defined
