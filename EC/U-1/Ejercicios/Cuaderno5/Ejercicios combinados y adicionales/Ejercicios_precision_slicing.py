# Ejercicio 35: Usa una lista de cadenas que representen números flotantes, conviértelas a flotantes y muestra los resultados con 3 decimales.

lista = ["1.23413", "4.1234234", "32.2352345"]

listaFloat = [float(n) for n in lista]

for n in listaFloat:
    print(f"{n:.3f}")
