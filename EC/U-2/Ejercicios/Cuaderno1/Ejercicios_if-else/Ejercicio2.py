# Ejercicio 2: Crear una calculadora básica empleando una interfaz con botones para los números (0-9), las operaciones (+, -, *, /), 
# y un botón de igual (=) para calcular el resultado. Conforme se van presionando botones, 
# vamos escribiendo una expresión en un widget de tipo Entry (capturamos lo que había, lo borramos y volvemos a escribir la expresión añadiendo lo nuevo). 
# No obstante, si el botón presionado es `=` entonces habrá que evaluar la expresión del Entry (`eval(entry.get())`... que podría arrojar excepciones), 
# después borramos lo escrito y escribimos el resultado (o un mensaje de error si se produjo). Opcionalmente, 
# podríamos desplegar los botones en el Frame empleando una lista de tuplas (con todos los botones) y recorriéndola con un bucle.

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

entrada = tk.Entry(ventana)
entrada.config(state="readonly")
entrada.pack(padx=10, pady=100)

tupla = (1, 2, 3, "+", "-", 6, 7, 8, "*", "/", 4, 5, 9, 0, "=")
cont = 0

frame = ttk.Frame(ventana)
frame.pack()

textoEntrada = ""

def boton_seleccionado(event):
    global textoEntrada
    entrada.config(state="normal")
    nombre = event.widget["text"]

    if nombre == "=":
        try:
            resultado = str(eval(textoEntrada))
            entrada.delete(0, tk.END)
            entrada.insert(0, resultado)
            textoEntrada = resultado
            textoEntrada = ""
        except Exception as e:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Error")
            textoEntrada = ""
    else:
        textoEntrada += nombre
        entrada.delete(0, tk.END)
        entrada.insert(0, textoEntrada)

    entrada.config(state="readonly")


for filas in range(3):
    for columnas in range(5):
        if cont < len(tupla):
            button = ttk.Button(frame, text=tupla[cont], width=5)
            button.grid(row=filas, column=columnas, padx=3, pady=3,)
            button.bind("<Button-1>", boton_seleccionado)
            cont += 1

ventana.mainloop()