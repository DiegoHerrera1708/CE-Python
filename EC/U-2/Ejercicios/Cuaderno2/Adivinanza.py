# Ejercicio 2.7: Crea un juego de adivinanza en el que el usuario debe adivinar un número entre 1 y 100. 
# Utiliza un `Spinbox` para permitir al usuario seleccionar un número, un `Button` para hacer la adivinanza y un `Label` para mostrar si la adivinanza fue correcta o no.

import tkinter as tk
import random

root = tk.Tk()

rand = random.randint(1, 100)

def adiviarNumero():
    num = int(spinbox.get())
    if num > rand:
        label.config(text="El numero es menor")
    elif num < rand:
        label.config(text="El numero es mayor")
    else:
        label.config(text="Enhorabuena, numero encontrado")

print(rand)

label = tk.Label(root, text="")
label.pack(pady=10)

# Crear el SpinBox con un rango de 0 a 100
spinbox = tk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=10, padx=20)

btn = tk.Button(root, text="Probar numero", command=adiviarNumero)
btn.pack(pady=10)

root.mainloop()