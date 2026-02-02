# Ejercicio 2.6: Crea una aplicación que utilice un `Treeview` para mostrar una estructura jerárquica (por ejemplo, categorías y subcategorías de productos). 
# Al hacer clic en un nodo, el `Label` debe actualizarse para mostrar detalles sobre la selección.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplo de Treeview con Jerarquías")

# Crear el Treeview
tree = ttk.Treeview(root)

# Definir las columnas (sin contar la columna de ID interna)
tree["columns"] = ("Nombre", "Descripción")

# Configurar las cabeceras de las columnas
tree.heading("#0", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Descripción", text="Descripción")

# Configurar las columnas para que tengan un tamaño adecuado
tree.column("#0", width=50)
tree.column("Nombre", width=150)
tree.column("Descripción", width=200)

# Insertar categorías principales (nodos de nivel 1)
categoria1 = tree.insert("", "end", text="1", values=("Electrónica", "Productos electrónicos"))

# Insertar subcategorías (nodos de nivel 2)
categoria1_1 = tree.insert(categoria1, "end", text="1.1", values=("Smartphones", "Teléfonos móviles"))
categoria1_2 = tree.insert(categoria1, "end", text="1.2", values=("Computadoras", "Laptops y PCs"))

# Insertar más subcategorías (nodos de nivel 3)
tree.insert(categoria1_1, "end", text="1.1.1", values=("iPhone", "Teléfonos Apple"))
tree.insert(categoria1_1, "end", text="1.1.2", values=("Samsung Galaxy", "Teléfonos Samsung"))
tree.insert(categoria1_2, "end", text="1.2.1", values=("MacBook", "Computadora portátil Apple"))
tree.insert(categoria1_2, "end", text="1.2.2", values=("Dell Inspiron", "Computadora portátil Dell"))

# Empacar el Treeview en la ventana
tree.pack(pady=20)

root.mainloop()