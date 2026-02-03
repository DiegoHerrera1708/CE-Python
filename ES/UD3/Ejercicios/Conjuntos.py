# 12. Dados 2 conjuntos calcula la unión, intersección y diferencia

lista1 = {1, 2, 3, 4, 5}
lista2 = {3, 4, 5, 6, 7}

print (lista1 | lista2) # Union
print (lista1 & lista2) # Interseccion
print (lista1 - lista2) # diferencia 

# 13. Dada una lista de números, cuenta cuántos valores distintos hay usando un conjunto.

lista1 = [1, 3, 2, 4, 3, 2, 5, 6, 3]
set1 = set(lista1)
print(f"Hay {len(set1)} valores distintos")

#14. Dadas dos listas, elimina de la primera los elementos que aparezcan en la segunda usando sets.

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

lista1 = set(lista1)
lista2 = set(lista2)

lista1 = list(lista1-lista2)

print(lista1)
