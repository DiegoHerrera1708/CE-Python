# Ejercicio 4: Crea una interfaz con tres botones que al ser presionados cambien el tamaño de la ventana. 
# Ofrece tres opciones: pequeño, mediano y grande, usando un `match-case` para cambiar el tamaño de la ventana según la selección.

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Tamaños Ventana")
ventana.geometry("800x600")

def cambiarVentana(event):
    boton = event.widget['text']

    match boton:
        case "Ventana Pequeña":
            ventana.geometry("400x300")
        case "Ventana Mediana":
            ventana.geometry("800x600")
        case "Ventana Grande":
            ventana.geometry("1200x800")


btnPequeño = ttk.Button(ventana, text="Ventana Pequeña", command=cambiarVentana)
btnPequeño.bind("<Button-1>", cambiarVentana)
btnMediano = ttk.Button(ventana, text="Ventana Mediana", command=cambiarVentana)
btnMediano.bind("<Button-1>", cambiarVentana)
btnGrande = ttk.Button(ventana, text="Ventana Grande", command=cambiarVentana)
btnGrande.bind("<Button-1>", cambiarVentana)


btnPequeño.pack(pady=15)
btnMediano.pack(pady=15)
btnGrande.pack(pady=15)

ventana.mainloop()