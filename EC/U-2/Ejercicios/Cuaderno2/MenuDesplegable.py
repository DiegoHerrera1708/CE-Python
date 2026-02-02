# Ejercicio 2.2. Menú desplegable para la selección de opciones con un ProgressBar
# Crea una interfaz donde el usuario selecciona una opción de un `Menubutton` (como "Iniciar", "Pausar", "Detener") 
# y luego un `Progressbar` que indique el progreso de una tarea simulada.

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Menu desplegable")
ventana.geometry("300x300")

progreso = None

def iniciar_progreso():
    global progreso
    start = int(progress['value'])

    def step(i):
        global progreso
        progreso = None
        progress['value'] = i
        progreso = ventana.after(50, step, i + 1)

    step(start)

def pausar_progreso():
    global progreso
    if progreso is not None:
        ventana.after_cancel(progreso)
        progreso = None

def detener_progreso():
    global progreso
    if progreso is not None:
        ventana.after_cancel(progreso)
        progreso = None
    progress['value'] = 0

menu_button = ttk.Menubutton(ventana, text="Selecciona una opción", direction="below")
menu = tk.Menu(menu_button, tearoff=False)

menu.add_command(label="Iniciar", command=iniciar_progreso)
menu.add_command(label="Pausar", command=pausar_progreso)
menu.add_command(label="Detener", command=detener_progreso)

menu_button["menu"] = menu


progress = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate", takefocus=False)
progress.pack(pady=20)

menu_button.pack(pady=20)

ventana.mainloop()
