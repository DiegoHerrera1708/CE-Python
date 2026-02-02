# escribe una cadena al reves

c = "hola_mundo"

for i in range(1, len(c)+1):
    print(c[-i], end="")

print()

for i in range(len(c)-1, -1, -1):
    print(c[i], end="")

print()

for i in range(len(c)):
    print(c[9-i], end="")

print()


# dada una cadena imprimir las letras impares en mayuscula y las pares en minuscula 

c = input("Dame una cadena de texto: ")

par = False

for i in range(len(c)):
    if par:
        print(c[i].lower(), end="")
    else:
        print(c[i].upper(), end="")
    par = not par
