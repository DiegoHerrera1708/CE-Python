# Ejercicio 2.3: Crea una aplicación con varias "páginas" utilizando el widget `Notebook`. Cada página puede tener un botón que al ser presionado cambia el 
# contenido de un `Label` que muestre información diferente en cada pestaña.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplo de Notebook")

def accion_boton():
    current_tab_id = notebook.select()
    current_index = notebook.index(current_tab_id)
    
    next_index = current_index + 1
    
    if next_index < len(notebook.tabs()):
        notebook.select(next_index)
    else:
        notebook.select(0)

# Crear el widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=20)

# Crear las páginas del Notebook (cada página es un Frame)
pagina1 = ttk.Frame(notebook)
pagina2 = ttk.Frame(notebook)
pagina3 = ttk.Frame(notebook)
pagina4 = ttk.Frame(notebook)
pagina5 = ttk.Frame(notebook)


# Añadir las páginas al Notebook
notebook.add(pagina1, text="Pestaña 1")
notebook.add(pagina2, text="Pestaña 2")
notebook.add(pagina3, text="Pestaña 3")
notebook.add(pagina4, text="Pestaña 4")
notebook.add(pagina5, text="Pestaña 5")


# Añadir contenido a las páginas
label1 = ttk.Label(pagina1, text="Label de la pestaña 1")
button1 = ttk.Button(pagina1, text="Sig. Pag", command=accion_boton)
label1.pack(padx=20, pady=20)
button1.pack()

label2 = ttk.Label(pagina2, text="Label de la pestaña 2")
button2 = ttk.Button(pagina2, text="Sig. Pag", command=accion_boton)
label2.pack(padx=20, pady=20)
button2.pack()

label3 = ttk.Label(pagina3, text="Label de la pestaña 3")
button3 = ttk.Button(pagina3, text="Sig. Pag", command=accion_boton)
label3.pack(padx=20, pady=20)
button3.pack()

label4 = ttk.Label(pagina4, text="Label de la pestaña 4")
button4 = ttk.Button(pagina4, text="Sig. Pag", command=accion_boton)
label4.pack(padx=20, pady=20)
button4.pack()

label5 = ttk.Label(pagina5, text="Label de la pestaña 5")
button5 = ttk.Button(pagina5, text="Sig. Pag", command=accion_boton)
label5.pack(padx=20, pady=20)
button5.pack()

root.mainloop()