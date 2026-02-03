# 15. Dada una expresión con paréntesis, verifica si están balanceados usando una pila.

expresion = "((2-3)"
lista = [x for x in expresion]
esta_balanceado = False
cont = 0

while lista != []:
    s = lista.pop()
    if s == ")":
        cont += 1
        esta_balanceado = False
    if s == "(":
        if cont == 0:
            break
        cont -= 1
    if cont == 0:
        esta_balanceado = True

print(f"La expresion { "si" if esta_balanceado else "no"} esta balanceada")



'''16. Crear una aplicación que simule una pila de libros. Se mostrará el siguiente menú:
n: Pide por pantalla el nombre del libro y lo añade a la cima de la pila
p: Se extrae el libro que está en la cima de la pila y se muestra por pantalla
l: Muestra un listado de la pila de libros
b: Borra todos los libros (pidiendo confirmación)
x: Sale de la aplicación'''

pila = []

while True:
    resp = input('''
n: Pide por pantalla el nombre del libro y lo añade a la cima de la pila
p: Se extrae el libro que está en la cima de la pila y se muestra por pantalla
l: Muestra un listado de la pila de libros
b: Borra todos los libros (pidiendo confirmación)
x: Sale de la aplicación
    
Elige una opción: ''').lower()


    match resp:
        case "n":
            libro_nuevo = input("Nombre del libro: ")
            pila.append(libro_nuevo)
        case "p":
            ultimo = pila.pop()
            print(f"Libro extraido: {ultimo}")
        case "l":
            print(pila)
        case "b":
            conf = input("¿Estas seguro que quieres borrar todos los libro S/N?")
            if conf.lower() == "s":
                pila.clear()
                print("Libros borrados")
        case "x":
            break
        case _:
            print("ERROR al introducir opcion\n")




'''17. Crear una aplicación que simule un sistema de turnos (médico): se atiende al primero y se
añade uno nuevo si llega. Se mostrará el siguiente menú:
n: Pide por pantalla el nombre del paciente y lo añade como nueva cita
a: El médico atiende al paciente al que le toca, se muestra por pantalla en nombre del
paciente y se saca de las citas pendientes
l: Muestra un listado de las citas pendientes
b: Borra todas las citas pendientes (pidiendo confirmación)
x: Sale de la aplicación'''

from collections import deque

cola = deque()

while True:
    resp = input('''
n: Pide por pantalla el nombre del paciente y lo añade como nueva cita
a: El médico atiende al paciente al que le toca, se muestra por pantalla en nombre del
paciente y se saca de las citas pendientes
l: Muestra un listado de las citas pendientes
b: Borra todas las citas pendientes (pidiendo confirmación)
x: Sale de la aplicación

Ingresa una opción: ''')
    match resp:
        case "n":
            paciente = input("Nombre del paciente: ")
            cola.append(paciente)
        case "a":
            atendido = cola.popleft()
            print(f"Paciente: {atendido}")
        case "l":
            print("Citas pendientes: ", list(cola))
        case "b":
            conf = input("¿Estas seguro que quieres borrar todas las citas S/N?")
            if conf.lower() == "s":
                cola.clear()
                print("Citas borradas")
        case "x":
            break
        case _:
            print("ERROR al introducir opcion\n")
