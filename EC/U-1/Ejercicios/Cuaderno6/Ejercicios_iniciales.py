# Ejercicio 1: Lee un número entero desde la entrada estándar y determina si es positivo, negativo o cero.

numero = int(input("Ingresa un numero para saber si es positivo o negativo: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

# Ejercicio 2: Escribe un programa que pida un número y determine si es divisible entre 3, 5, o ambos.

numero = int(
    input("Ingresa un numero para saber si es divisible entre 3, 5, o ambos: ")
)

if (numero % 5 == 0) and (numero % 3 == 0):
    print("El numero es divisible entre ambos")
elif numero % 5 == 0:
    print("El numero es divisible entre 5")
elif numero % 3 == 0:
    print("El numero es divisible entre 3")
else:
    print("El numero no es divisible entre 5 ni entre 3")

# Ejercicio 3: Verifica si un número es par o impar usando un condicional ternario.

numero = int(input("Ingresa un numero para saber si es par o impar: "))
mensaje = "El numero es par" if numero % 2 == 0 else "El numero es impar"
print(mensaje)

# Ejercicio 4: Determina si una persona es mayor de edad (18 años o más) con un condicional ternario.

numero = int(
    input("Ingresa un numero para saber si una persona es mayor de edad o no: ")
)
mensaje = "Es mayor de edad" if numero > 17 else "Es menor de edad"

# Ejercicio 5: Imprime los números del 1 al 10 utilizando un bucle for con un rango.
for i in range(1, 11):
    print(i)

# Ejercicio 6: Imprime todos los números del 1 al 50 que sean divisibles por 4 utilizando un bucle for con un rango.

for i in range(1, 51):
    if i % 4 == 0:
        print(i)

# Ejercicio 7: Escribe un programa que pida al usuario un número positivo y luego calcule la suma de todos los números del 1 hasta ese número utilizando un bucle while.

numero = int(input("Ingresa un numero positivo: "))
suma = 0
cont = 1

while cont < numero:
    suma += cont
    cont += 1

print(suma)

# Ejercicio 8: Implementa un programa que pida una contraseña y se repita (con un bucle while) hasta que el usuario introduzca la contraseña correcta.

pswd = input("Ingresa una contraseña: ")
while pswd != "administrador":
    print("Contraseña incorrecta, por favor", end=" ")
    pswd = input("ingresa una contraseña: ")

# Ejercicio 9: Crea un bucle for que imprima números del 1 al 10, pero que detenga el bucle al llegar al número 6 utilizando break.

for i in range(1, 10):
    print(i)
    if i == 6:
        break

# Ejercicio 11: Escribe un programa que imprima los números del 1 al 10, pero que omita el número 5 utilizando continue.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Ejercicio 12: Crea una función que reciba un número y eleve una excepción si el número es negativo, utilizando raise.

numero = int(input("Ingresa un numero: "))
if numero < 0:
    raise ValueError("El numero es negativo")
else:
    print("El numero es positivo")
