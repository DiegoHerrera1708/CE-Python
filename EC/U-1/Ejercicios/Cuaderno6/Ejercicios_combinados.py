# Ejercicio 13: Escribe un programa que pida una lista de números separados por comas y luego determine cuál es el mayor número par de la lista.
# Si no hay ningún número par, debe indicar que no existe ninguno.

listNum = (input("Dame una lista de numeros separados por comas: ")).split(",")
listNum = [int(n) for n in listNum]
numeroAlto = 0
for n in listNum:
    if n % 2 == 0 and n > numeroAlto:
        numeroAlto = n
if numeroAlto == 0:
    print("No existe ningun numero par")
else:
    print(numeroAlto)

# Ejercicio 14: Pide al usuario que introduzca una lista de números y, utilizando un bucle for y condicionales, imprima los números negativos y positivos por separado.

listNum = (
    input("Dame una lista de numeros positivos y negativos separados por comas: ")
).split(",")
listNum = [int(n) for n in listNum]
listPositivos = []
listNegativos = []

for n in listNum:
    if n > 0:
        listPositivos.append(n)
    else:
        listNegativos.append(n)

print("Numeros positivos: ", listPositivos)
print("Numeros negativos: ", listNegativos)

# Ejercicio 15: Imprime los números impares del 1 al 200 utilizando un bucle for con un rango que tenga paso de 3.

for i in range(1, 200, 3):
    if i % 2 != 0:
        print(i)

# Ejercicio 16: Escribe un programa que imprima todos los múltiplos de 3 del 1 al 100, pero solo hasta el primer múltiplo mayor que 50.

for n in range(1, 100):
    if n % 3 == 0:
        if n > 50:
            break
        print(n)


# Ejercicio 17: Crea una función que reciba el nombre de un mes (como "enero", "febrero", etc.) y devuelva la estación del año correspondiente usando match-case.

estacion = input("Ingresa un mes del año: ")
match estacion:
    case "enero", "febrero", "marzo":
        print("Estamos en invierno")
    case "abril", "mayo", "junio":
        print("Estamos en primavera")
    case "julio", "agosto":
        print("Estamos en verano")
    case "octubre", "noviembre", "diciembre":
        print("Estamos en otoño")

# Ejercicio 18: Escribe un programa que reciba una cadena de texto representando un día de la semana y te diga si es fin de semana o día laborable utilizando match-case.

dia = input("Dime un dia de la semana: ")
match dia:
    case "lunes", "martes", "miercoles", "jueves", "viernes":
        print(f"El {dia}, es un dia laboral")
    case "sabado", "domingo":
        print(f"El {dia} es un din de semana")
    case _:
        print("No has ingresado un dia de la semana")

# Ejercicio 19: Escribe un programa que busque un número en una lista utilizando un bucle for.
# Si lo encuentra, imprime "Número encontrado", y si no, imprime "Número no encontrado", utilizando else en el bucle.

listNum = [12, 2, 324, 14, 23, 5, 74]
num = input("Dime un numero para buscarlo en la lista: ")
for n in listNum:
    if n == num:
        print("numero encontrado")
        break
    else:
        print("Numero no encontrado")

# Ejercicio 20: Implementa un programa que recorra una lista de nombres y determine si algún nombre tiene más de 5 caracteres.
# Si se encuentra uno, el bucle debe finalizar con break, y si no se encuentra ninguno, imprime "Ningún nombre largo" al final.

listNombres = ["sol", "luna", "mar", "Diego", "jose"]
for n in listNombres:
    if len(n) > 4:
        break
else:
    print("Ningún nombre largo")

# Ejercicio 21: Crea una función que reciba un número como argumento y si el número es negativo, lance una excepción de tipo ValueError
# con un mensaje como "Error: número negativo".


def myfunc(num):
    if num < 0:
        raise ValueError("Error: número negativo")


myfunc(-1)

# Ejercicio 22: Modifica la solución anterior para que el usuario pueda intentar introducir un nuevo número si se lanza una excepción. Tendrá un número de intentos infinito.


def myfunc(num):
    while num < 0:
        try:
            num = int(input("Introduce un numero numero pero esta vez positivo: "))
        except ValueError:
            print("Error: Numero negativo")
        finally:
            continue


num = int(input("Introduce un numero: "))
myfunc(num)
