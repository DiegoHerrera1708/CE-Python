# Ejercicio 3: Crear un formulario que valide la entrada de datos del usuario. Si la entrada es incorrecta, muestra un mensaje de error. 
# Crea un formulario con campos para el nombre y el correo electrónico. Validemos que el nombre no esté vacío y que el correo electrónico contenga un @. 
# Si la entrada no es válida, muestra un mensaje de error. Puedes emplear `messagebox.showerror("Tu mensaje de error")`. 
# No olvides importar el componente: `from tkinter import messagebox`.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("300x200")

def comprobacion():

    if len(nombre.get()) == 0:
        messagebox.showerror(message="Nombre vacio", title="Error")
    elif '@' not in email.get():
        messagebox.showerror(message="Falta '@' en el email", title="Error")
    else:
        messagebox.showinfo(message="Datos enviados correctamente", title="Enviado")
        ventana.destroy()

textNombre = ttk.Label(ventana, text="nombre:")
nombre  = ttk.Entry(ventana)
textEmail = ttk.Label(ventana, text="email:")
email = ttk.Entry(ventana)
boton = ttk.Button(ventana, text="Enviar", command=comprobacion)

textNombre.pack(pady=10)
nombre.pack(pady=10)
textEmail.pack()
email.pack(pady=10)
boton.pack(pady=10)

ventana.mainloop()