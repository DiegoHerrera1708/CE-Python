'''
23. Necesitamos registrar la cantidad de lluvia que se produce cada hora de cada día en cada
provincia de Andalucia a lo largo de un año. Para ello vamos a usar un array tridimensional.
Diseñar una aplicación con un menú con el que podamos:
- Añadir la cantidad de lluvia para una provincia, un día y una hora concreta.
- Opcionalmente se pueden obtener las cantidades de un fichero.
- Mostrar las cantidades de lluvia caídas en una provincia y un día (un dato para cada hora).
- Mostrar la provincia con más lluvias en un día concreto.
- Mostrar la media de lluvia en un día y una hora.
- Dada una provincia listar los días en los que ha llovido
- Calcular la hora del día en la que más ha llovido en cada provincia
'''


print('''
1. Añadir la cantidad de lluvia para una provincia, un día y una hora concreta.
2. Opcionalmente se pueden obtener las cantidades de un fichero.
3. Mostrar las cantidades de lluvia caídas en una provincia y un día (un dato para cada hora).
4. Mostrar la provincia con más lluvias en un día concreto.
5. Mostrar la media de lluvia en un día y una hora.
6. Dada una provincia listar los días en los que ha llovido
7. Calcular la hora del día en la que más ha llovido en cada provincia
8. Salir
      ''')

# [provincias[dias[horas]]]
lluvia = [[[]]]
provincias = ["Cadiz", "Malaga", "Huelva", "Sevilla", "Jaen", "Almeria", "Cordoba", "Granada"]

# p provincia, d dias, h  horas
def anadir_cantidad():
    p = int(input('''Para que provincia:
                      1. Cadiz
                      2. Malaga
                      3. Huelva
                      4. Sevilla
                      5. Jaen
                      6. Almeria
                      7. Cordoba
                      8. Granada''')) - 1
    d = int(input("Para que dia (1-365): ")) - 1
    h =int(input("Para que hora (0-23): "))
    cantidad = float(input("Que cantidad deseas añadir: "))
    lluvia[p][d][h] = cantidad
    print(f"Cantidad añadida a {provincias[p]}, dia {d + 1}, hora {h}")

def mostrar_por_provincia_y_dia(p, d):
    for i in range(len(lluvia[p][d])):
        print(f"Hora {i}: {lluvia[p][d][i]}", end=", ")
    print()

def provincia_con_mas_lluvia(d):
    lista = [sum(lluvia[x][d]) for x in range(len(lluvia))]
    maximo = max(lista)
    indice = lista.index(maximo)
    print(f"La provincia con mas lluvias en el dia {d}, es {provincias[indice]}")

def media_pyh(d, h):
    lista = [lluvia[i][d][h] for i in range(len(lluvia)) ]
    media = sum(lista)/len(lista)
    print(f"La media del dia {d} a la hora {h} es {media}")

def dias_llovidos_por_provincia(p):
    ha_llovido = False
    print("Ha llovido en los dias: ")
    for dias in range(len(lluvia[p])):
        for horas in range(len(lluvia[p][dias])):
            if lluvia[p][dias][horas] > 0.0:
                ha_llovido = True
                return
        if ha_llovido:
            print(lluvia[p][dias], end=", ")
            ha_llovido = False
    print()

while True:
    opcion = int(input("Elige una opcion: "))
    match opcion:
        case 1:
            # Añadir la cantidad de lluvia para una provincia, un día y una hora concreta
            anadir_cantidad()
        case 2:
            # Opcionalmente se pueden obtener las cantidades de un fichero.
            pass
        case 3: 
            # Mostrar las cantidades de lluvia caídas en una provincia y un día (un dato para cada hora).
            p = int(input('''Para que provincia:
                      1. Cadiz
                      2. Malaga
                      3. Huelva
                      4. Sevilla
                      5. Jaen
                      6. Almeria
                      7. Cordoba
                      8. Granada''')) - 1
            d = int(input("Para que dia (1-365): ")) - 1
            mostrar_por_provincia_y_dia(p, d)
        case 4:
            # Mostrar la provincia con más lluvias en un día concreto.
            d = int(input("Para que dia (1-365): ")) - 1
            provincia_con_mas_lluvia(d)
        case 5: 
            # Mostrar la media de lluvia en un día y una hora.
            d = int(input("Para que dia (1-365): ")) - 1
            h =int(input("Para que hora (0-23): "))
            media_pyh(d, h)
            
        case 6: 
            # Dada una provincia listar los días en los que ha llovido
            p = int(input('''Para que provincia:
                      1. Cadiz
                      2. Malaga
                      3. Huelva
                      4. Sevilla
                      5. Jaen
                      6. Almeria
                      7. Cordoba
                      8. Granada''')) - 1
            dias_llovidos_por_provincia(p)
        case 7: 
            # Calcular la hora del día en la que más ha llovido en cada provincia
            pass
        case 8: 
            break
        case _:
            print("Entradad errónea")