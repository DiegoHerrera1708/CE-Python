expresion = "(())()("
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
