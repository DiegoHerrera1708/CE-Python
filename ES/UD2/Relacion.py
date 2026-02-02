'''
1. Realizar un programa que muestre un menú con las siguientes opciones:
1 Suma
2 Resta
3 Multiplicación
4 División
0 Salir
A continuación solicitará 2 números y mostrará el resultado de la elegida.
El programa se repetirá continuamente hasta que el usuario seleccione la opción de salir
'''

while True:
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))

    print(
'''
Realizar un programa que muestre un menú con las siguientes opciones:
1 Suma
2 Resta
3 Multiplicación
4 División
0 Salir
'''
    )
    eleccion = int(input("Elige una opcion del menu: "))

    match eleccion:
        case 0:
            break
        case 1:
            print(num1+num2)
        case 2:
            print(num1-num2)
        case 3:
            print(num1*num2)
        case 4:
            print(num1/num2)
        case _: 
            break


# 2. 2. Realizar un programa que convierta grados Celsius a Fahrenheit
# (0 °C × 9 / 5) + 32 = 32 °F

gc = 24

grados_a_celsius = (gc + 9 / 5) + 32 

print(f"24 grados celsius a fahrebheit son {grados_a_celsius}")


'''
3. Suponiendo que tu nombre está en una variable llamada nombre, realiza solo una llamada a
la función print para obtener los siguientes resultados
a) Hola, me llamo <nombre>
b) <nombre> repetido 5 veces separadas por el caracter "*"
'''

nombre = "Diego"

print(f"Hola, me llamo {nombre}")
print(f"{nombre}", f"{nombre}", f"{nombre}", f"{nombre}", f"{nombre}", sep="*" )


'''
4. Imprimir por pantalla las siguientes cadenas de caracteres:
a) I'm a student
b) "I'm a student"
c) Es difícil escribir 'una cadena con el carácter" '
'''
print("I'm a student")
print('"I\'m a student"')
print("Es difícil escribir 'una cadena con el carácter\" '")

# 5. Verifica si un número introducido es mayor que 10

num = int(input("Introduce un numero"))

if num > 10:
    print("El numero es mayor a 10")
else:
    print("El numero es menor a 10")

# 6. Pide una edad y comprueba si la persona es mayor de edad y no supera 65

edad = int(input("Introduce una edad"))

if edad > 17 and edad <65:
    print("Mayor de edad y menor a 65 años")
else:
    print("Rango de edad fuera de los limites (18-65)")

'''
7. Escribe una expresión que determine si una contraseña es válida cuando:
• Tiene más de 8 caracteres
• Contiene la letra "@"
• No contiene espacios
'''

paswd = input("Escribe una contraseña: ")
if len(paswd) > 8 and "@" in paswd and " " not in paswd:
    print("Contraseña establecida")
else:
    print("Contraseña no válida")

'''
8. Dada la cadena "pythonista":
• Muestra la primera letra
• Muestra la última
• Muestra la letra con índice 4
'''

c = "pythonista"
print(c[0])
print(c[-1])
print(c[4])

'''
9. Pide una cadena de caracteres por teclado e imprímela en 2 líneas dividida por la mitad. No
se pueden usar bucles. Por ejemplo, la cadena "casa" daría como resultado
ca
sa
Y la cadena "remar" daría
rem
ar
'''

c = input("Escribe una cadena: ")

mitad = len(c)//2
c1 = c[:mitad]
c2 = c[mitad:]

'''
10. Toma una frase y crea una nueva cadena donde las letras en índice par estén en minúscula y
as de índice impar en mayúscula.
'''

c = "holamundo"

for i in range(len(c)):
    if i % 2 == 0:
        print(c[i].lower(), end = "")
    else:
        print(c[i].upper(), end = "")


'''
11. Declara variables de todos los tipos que hemos estudiado y muestra por pantalla para cada
una de ellas:
La variable <nombre de la vble> vale <valor de la vble> y es de tipo <tipo de la vble>'''

entero = 2
string = "hola"
flotante = 2.3
boleano = True

print(f"La variable entero vale {entero} y es de tipo {type(entero)}")
print(f"La variable string vale {string} y es de tipo {type(string)}")
print(f"La variable flotante vale {flotante} y es de tipo {type(flotante)}")
print(f"La variable boleano vale {boleano} y es de tipo {type(boleano)}")

# 12. Dado un valor en segundos, usa variables para calcular horas, minutos y segundos

tiempo = 7456
horas, minutos, segundos = 0, 0, 0

if tiempo >= 60:
    minutos = tiempo // 60
    segundos = tiempo % 60
else:
    segundos = tiempo

if minutos >= 60:
    horas = minutos // 60
    minutos = minutos % 60

print(f"Horas: {horas}, minutos: {minutos}, segundos: {segundos}")

'''
13. Calcula si un año introducido por teclado es bisiesto (los divisibles por 4 excepto los que
también sean divisibles por 100 o por 400)
'''

anio = int(input("Introduce un año: "))

if anio % 4 == 0:
    if anio % 400 != 0 or anio % 100 != 0:
        print("Año bisiesto")
    else:
        print("Año no bisiesto")
else:
        print("Año no bisiesto")

# 14. Dado un número, comprueba si su valor absoluto es mayor que 10 sin usar abs()

num = 10.23
num = round(num)
print(num)

# 15. Compara tres números y determina cuál es el mayor usando solo operadores relacionales

a, b, c = 4, 5, 7

if a > b:
    if a > c:
        print(f"La variable a es la mas grande con: {a}")
    else:
        print(f"La variable c es la mas grande con: {c}")
else:
    if b > c: 
        print(f"La variable b es la mas grande con: {b}")
    else:
        print(f"La variable c es la mas grande con: {c}")

# 16. Comprueba si un número es par o múltiplo de 5 usando or

num = 15

if num % 2 == 0 or num % 5 == 0:
    print(f"el numero {num} es par o multiplo de 5")

'''
17. Escribe un programa que pregunte si llueve y si tienes paraguas, y determine si puedes salir
(usa lógica)
'''

respuesta = input("Esta lloviendo ? ")


if respuesta.lower() == "si":
    respuesta = input("Tienes paraguas ? ")
    if respuesta.lower() == "si":
        print("Puedes salir")
    else:
        print("No puedes salir")
else:
    print("Puedes salir")



# 18. Realiza un desplazamiento a la izquierda: calcula 7 << 2 y explica el resultado

print( 7 << 2 )
print('''7 -> 111
      << 2
      11100 -> 28
      se desplazan 2 posiciones a la derecha a nivel binario añadiendo dos ceros
      y se calcula el decimal
      ''')

# 19. Realiza un desplazamiento a la derecha: calcula 20 >> 3

print(20 >> 3)
print('''20 -> 10100
      00010 -> 2
      se desplazan 3 posiciones a la izquierda eliminando las 3 ultimas posiciones para dejar la misma cantidad de bits ''')

'''
20. Aplica el operador NOT (~) a 0b1010 y muestra el resultado en binario usando una máscara
de 4 bits
'''

n = 0b1010
bits = 4

mask = (1 << bits) - 1
r = ~n & mask

print(f"{r:b}")


'''
21. Escribe un programa que determine si el bit menos significativo de un número es 1 (el menos
significativo es el que está más a la derecha)
'''

n = 0b10011010
if n & 1 == 1:
    print("El bit significativo es 1")
else:
    print("El bit significativo es 0")