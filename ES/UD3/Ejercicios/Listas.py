# 1. Crea una lista con 10 enteros y calcula la suma total sin usar sum().

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma = 0 

for i in lista:
    suma += i 

print(suma)

# 2. Dada una lista de nombres, cuenta cuántos empiezan por vocal.

vocales = [ 'a', 'e', 'i', 'o', 'u']
lista = ["Pablo", "Ana", "Jose", "Oscar"]
cont = 0
for nombre in lista:
    if nombre[0].lower() in vocales:
        cont += 1

print("Existen", cont, "nombres que empiezan por vocal")


# 3. Dada una lista de números, crea otra lista con solo los pares

lista = [2, 3, 4, 5, 6, 7234, 43]
pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
        
print(pares)

# 4. Elimina de una lista todas las apariciones de un valor dado (ej. borrar todos los 0).

lista = [2, 0, 3, 2, 4, 5, 1, 2, 7, 1, 2]

# Queremos eliminar los 2
while 2 in lista:
    indice = lista.index(2)
    del lista[indice]

print(lista)

# 5. Dada una lista, rota sus elementos 1 posición a la derecha (el último pasa a ser el primero).

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, lista[-1])
del lista[-1]

print(lista)

# 6. Genera una lista con los primeros n múltiplos de 3.

n = int(input("Introduce un numero: "))

lista = [ (num + 1) * 3 for num in range(n)]
print(lista)

'''
7. Dada una lista con números repetidos, crea una lista que conserve el orden pero sin
repetidos.
'''

lista = [1, 2, 3, 42, 6, 3, 7, 4, 8, 9, 9, 2]
lista_sin_repetidos = []

for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)

print(lista_sin_repetidos)

# 8. Dada una lista, obtén una sublista con los elementos del índice 3 al 7 (incluido 7).

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista = lista[3:8]
print(sublista)

# 9. Dada una lista, obtén los 5 últimos elementos usando slicing.

sublista = lista[-5:]
print(sublista)

# 10. Dada una lista, crea una sublista con un salto de 3 en 3 elementos.

sublista = lista[::3]
print(sublista)

# 11. Dada una lista, reemplaza con 0 el tramo entre índices 4 y 8 usando slicing.

sublista = lista
for i in range(len(lista)):
    if i>3 and i<9:
        sublista[i] = 0
print(sublista) 
