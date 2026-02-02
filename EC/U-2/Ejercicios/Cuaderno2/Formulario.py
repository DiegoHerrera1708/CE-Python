# Ejercicio 2.5: Crea un formulario de registro que permita al usuario ingresar su nombre, elegir un país de un `ComboBox`, y marcar una casilla de aceptación con un `Checkbutton`. 
# Un botón debe verificar si todos los campos están completos y mostrar un mensaje de éxito o error.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Ejemplo de ComboBox")
root.geometry("300x200")

def submit ():
    if entrada.get() == "":
        messagebox.showerror(message="Nombre vacio", title="Error")
    else:
        messagebox.showinfo(message=f"Bienvenido {entrada.get()}", title="Enhorabuena")

label = tk.Label(root, text="Introduce tu nombre:")
label.pack(pady=10)

entrada = tk.Entry(root)
entrada.pack(pady=10)

# Crear un ComboBox con opciones
opciones = ["España", "Inglaterra", "Francia"]
combo = ttk.Combobox(root, values=opciones)
combo.current(0)
combo.pack(pady=20)

btn = tk.Button(root, text="Submit", command=submit)
btn.pack(pady=10)

root.mainloop()