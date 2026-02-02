# Ejercicio 2.8: Crea una ventana emergente usando el widget `Toplevel` que aparezca cuando el usuario haga clic en un botón. 
# Dentro de esa ventana, utiliza un `Label` y un `Checkbutton` para pedir al usuario una confirmación (por ejemplo, "¿Estás seguro de que quieres continuar?").

import tkinter as tk

def continuar():
    if var1.get():
        root.destroy()


def abrir_ventana():
    # Crear una nueva ventana Toplevel
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Ventana Secundaria")

    # Agregar un mensaje a la nueva ventana
    tk.Label(ventana_secundaria, text="¿Estas seguro de que quieres continuar?").pack()


    # Puedes añadir más widgets a la ventana secundaria si lo necesitas
    tk.Checkbutton(ventana_secundaria, text="Continuar", variable=var1, command=continuar).pack()

root = tk.Tk()
root.title("Ventana Principal")


# Variables para almacenar el estado de cada CheckButton
var1 = tk.IntVar()

# Botón para abrir la ventana secundaria
boton = tk.Button(root, text="Abrir ventana secundaria", command=abrir_ventana)
boton.pack(padx=25, pady=25)

root.mainloop()