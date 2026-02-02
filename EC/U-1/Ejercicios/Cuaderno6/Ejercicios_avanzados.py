# Ejercicio 23: Escribe un programa que pida al usuario una lista de números y calcule su media, pero primero debe verificar que todos los números son positivos.
# Si algún número es negativo, lanza una excepción personalizada.


class NumeroNegativoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


listNum = input("Dame una lista de numeros: ").split(",")
listNum = [int(i) for i in listNum]
media = 0
for i in listNum:
    media += i
media /= len(listNum)
print(media)
for i in listNum:
    if i < 0:
        raise NumeroNegativoException("Has pasado un numero negativo")

# Ejercicio 24: Crea una función que reciba una cadena de texto e imprima los caracteres en orden inverso (emplea `cadena[::-1]`).
# Si la cadena contiene más de 10 caracteres (emplea la función `len`), eleva una excepción indicando que es demasiado larga.


class CadenaLargaexception(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def myfunc(cadena):
    if len(cadena) < 10:
        print(cadena[::-1])
    else:
        raise CadenaLargaexception("La cadena es demassiado larga")


# Ejercicio 25: Crea un programa que pida al usuario el nombre de un día de la semana (por ejemplo, 'lunes', 'martes', etc.) y un número del 1 al 7.
# El programa debe verificar si el número corresponde al día que se introdujo (lunes-1, martes-2, etc.). Si el número coincide con el día de la semana,
# imprimirá un mensaje como 'El día que introdujiste es correcto'. Si el número no corresponde al día introducido, imprimirá 'El número no corresponde con el día'.
# Si el número está fuera del rango (menor que 1 o mayor que 7), imprimirá 'Número inválido'. Si el nombre del día introducido no es válido
# (es decir, no es uno de los días de la semana), el programa debe imprimir 'Día inválido'.

dia = input("Dime un dia de la semana: ")
num = int(input("Dime un numero del 1 al 7: "))
diaSemana = dia + "-" + str(num)
diasSemanales = [
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo",
]

if num > 7 or num < 1:
    print("Numero inválido")
else:
    for i in range(1, len(diasSemanales) + 1):
        if dia == diasSemanales[i - 1]:
            if diaSemana == diasSemanales[i - 1] + "-" + str(i):
                print("El dia que introdujiste es correcto")
                break
            else:
                print("El número no corresponde con el día")
                break
    else:
        print("Dia invalido")

# Ejercicio 26: Crea un programa que pida una lista de cadenas de texto. Si alguna de las cadenas tiene menos de 3 caracteres,
# lanzará una excepción personalizada (por ejemplo: `class CadenasDemasiadoCortasError(Exception):` que no hará nada `pass`).
# Si la cadena tiene más de 3 caracteres, la imprimirá, Recorrerá todas las cadenas, debe continuar incluso si se lanza una excepción para algunas cadenas.


class CadenasDemasiadoCortasError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


listTexto = (input("Ingresa unas cadenas de texto: ")).split(" ")
for i in listTexto:
    if len(i) < 3:
        try:
            raise CadenasDemasiadoCortasError("La cadena es deamisado corta")
        except CadenasDemasiadoCortasError as e:
            print(e)
    else:
        print(i)


# Ejercicio 27: Implementa una función recursiva que calcule el factorial de un número. Si el número es negativo,
# lanza una excepción (como `class FactorialNegativoError(Exception):`) indicando que no se puede calcular el factorial de números negativos.


class FactorialNegativoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def factorial_recursivo(n):
    if n < 0:
        raise FactorialNegativoError(
            "No se puede calcular el factorial de numeros negativos"
        )
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


print(factorial_recursivo(5))

# Ejercicio 28: Crea una función que reciba una lista de números y devuelva el mayor número que aparece en la lista. Si la lista está vacía, lanzará una excepción.


def maxNumList(listNum):
    numeroAlto = 0
    if len(numeroAlto) != 0:
        for n in listNum:
            if n > numeroAlto:
                numeroAlto = n
    else:
        raise Exception("La lista esta vacia")
    return numeroAlto


# Ejercicio 29: Crea una clase Producto que tenga un nombre y un precio.
# Luego, implementa una clase Carrito que permita agregar productos al carrito, calcular el total, y eliminar productos.
# Si, al crear un producto, su precio es negativo, lanzará una excepción.

class ValueNegative(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        if precio > 0:
            self.precio = precio
        else:
            raise ValueNegative("El precio es negativo")


class Carrito:
    def __init__(self):
        self.productos = []

    def agregarAlCarrito(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def eliminarProductos(self, productoEliminado):
        for producto in self.productos:
            if producto == productoEliminado:
                self.productos.remove(productoEliminado)


p1 = Producto("Mantequilla", 2.34)
p2 = Producto("Sal", 1.23)

c = Carrito()
c.agregarAlCarrito(p1)
c.agregarAlCarrito(p2)
print("El total del carrito es: ", c.calcularTotal())
c.eliminarProductos(p2)
print("El total del carrito es: ", c.calcularTotal())
p3 = Producto("Azucar", -2)
