# Ejercicio 5: Crear un menú con cuatro entradas (Rojo, Verde, Azul y Amarillo) para cambiar el fondo de la ventana. 
# Cambia el fondo de la ventana cuando el usuario seleccione una opción.

import tkinter as tk

def cambiarColor(color):
    match color:
        case "Rojo":
            ventana.config(bg="red")
        case "Verde":
            ventana.config(bg="green")
        case "Azul":
            ventana.config(bg="blue")
        case "Amarillo":
            ventana.config(bg="yellow")

ventana = tk.Tk()
ventana.title("Menu colores")
ventana.geometry("500x500")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_colores = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Colores", menu=menu_colores)

menu_colores.add_command(label="Rojo", command=lambda: cambiarColor("Rojo"))
menu_colores.add_command(label="Verde", command=lambda: cambiarColor("Verde"))
menu_colores.add_command(label="Azul", command=lambda: cambiarColor("Azul"))
menu_colores.add_command(label="Amarillo", command=lambda: cambiarColor("Amarillo"))

ventana.mainloop()

