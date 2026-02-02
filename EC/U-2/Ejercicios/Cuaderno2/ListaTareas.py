# Ejercicio 2.1: Crea una aplicación de lista de tareas. El usuario podrá añadir tareas a una `Listbox` y marcar cada tarea como completada utilizando un `Checkbutton`. 
# Añadir un botón para eliminar tareas completadas.

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista Tareas")
ventana.geometry("400x500")

lista_valores = []
lista_widgets = []

def addTask():
    varBoolean = tk.BooleanVar(value=False)
    button = tk.Checkbutton(frame_lista, text=input.get(), variable=varBoolean)
    button.pack()
    lista.insert(tk.END, button)
    input.delete(0, tk.END)
    lista_valores.append(varBoolean)
    lista_widgets.append(button)

def deleteTask():
    for i in range(len(lista_valores) -1, -1, -1):
        if lista_valores[i].get():
            lista_widgets[i].destroy()
            lista_valores.pop(i)
            lista_widgets.pop(i)


lista = tk.Listbox(ventana, selectmode=tk.MULTIPLE)
input = ttk.Entry(ventana)
btnAddTask = ttk.Button(ventana, text="Añadir tarea", command=addTask)
btnDelTask = ttk.Button(ventana, text="Eliminar tarea", command=deleteTask)
frame_lista = tk.Frame(lista)

lista.pack()
frame_lista.pack()
input.pack(pady=15)
btnAddTask.pack(pady=5)
btnDelTask.pack()

ventana.mainloop()