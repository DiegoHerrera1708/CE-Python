# Ejercicio 2.4: Crea una interfaz donde el usuario puede ajustar el tamaño de la fuente de un `Label` mediante un `Scale` (barra deslizante). 
# Añade un botón que permita restablecer el tamaño de la fuente a su valor predeterminado

import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Ejemplo de Scale")

TAMANO_PREDETERMINADO = 12

def ajustar_tamanio(valor_escala):
    nuevo_tamano = int(float(valor_escala))
    fuente_personalizada.configure(size=nuevo_tamano)

fuente_personalizada = tkFont.Font(family="Helvetica", size=TAMANO_PREDETERMINADO)
label = tk.Label(root, text="Ajusta el tamaño de fuente", font=fuente_personalizada)
label.pack(pady=10)

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command = ajustar_tamanio)
scale.pack(pady=20)

root.mainloop()