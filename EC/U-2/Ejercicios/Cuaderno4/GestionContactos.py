import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Gestion de Contactos")

contactos = []

def validar_contacto():

    try:
        if entry_nombre.get()== "" and entry_email.get() == "" and entry_tlf.get() == "":
            messagebox.showerror("Error", "Rellena todos los campos")
        elif "@" not in entry_email.get():
            messagebox.showerror("Error", "Email no valido")
        elif len(entry_tlf.get()) != 9:
            messagebox.showerror("Error", "Telefono no valido")
            tlf =int(entry_tlf.get())
        else:
            contactos.append(entry_nombre.get()+" | "+entry_email.get()+" | "+entry_tlf.get())
            actualizar_lista_contactos()

            entry_nombre.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_tlf.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Telefono no valido")        

    
    

def actualizar_lista_contactos():
    listbox.delete(0, tk.END)
    for contacto in contactos:
        listbox.insert(0, contacto)

def eliminar_contacto():
    indice  = listbox.curselection()
    if not indice:
        messagebox.showinfo("Advertencia", "No has seleccionado ningun contacto")
    else:
        listbox.delete(indice)

listbox = tk.Listbox(root)
listbox.pack(pady=10, padx=10)

frame_formulario = ttk.Frame(root)
frame_formulario.pack(padx=20, pady=10)

btnAgregar = ttk.Button(root, text="Agregar Contacto", command=validar_contacto)
btnAgregar.pack(pady=10)
btnEliminar = ttk.Button(root, text="Eliminar Contacto", command=eliminar_contacto)
btnEliminar.pack(pady=10)

label_nombre = ttk.Label(frame_formulario, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = ttk.Entry(frame_formulario)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_email = ttk.Label(frame_formulario, text="Email:")
label_email.grid(row=1, column=0, padx=5, pady=5)
entry_email = ttk.Entry(frame_formulario)
entry_email.grid(row=1, column=1, padx=5, pady=5)

label_tlf = ttk.Label(frame_formulario, text="Telefono:")
label_tlf.grid(row=2, column=0, padx=5, pady=5)
entry_tlf = ttk.Entry(frame_formulario)
entry_tlf.grid(row=2, column=1, padx=5, pady=5)


root.mainloop()