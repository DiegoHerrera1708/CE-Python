# Ejercicio 1: Crear una ventana que tenga un botón. Al presionar el botón, se cambia el color de fondo de la ventana. 
# Utiliza tres colores diferentes: red, blue y green. Cuando se presiona el botón, cambia el color de fondo entre estos colores de forma cíclica. 
# Puedes obtener el color de fondo de la ventana con `ventana.cget("bg")` y establecerlo con `ventana.config(br="mi_color")`.

import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

def saludar(): # secuencia rojo-blue-green
    color_actual = ventana.cget("bg")
    if color_actual == "red":
        ventana.config(bg="blue")
    elif color_actual == "blue":
        ventana.config(bg="green")
    else:
        ventana.config(bg="red")

boton = tk.Button(ventana, text="Haz clic aquí para cambiar de color", command=saludar)
boton.pack()

ventana.mainloop()