import time
import tkinter as tk

def actualizar_hora():
    nueva_hora = time.strftime("%H:%M:%S")
    reloj.config(text=nueva_hora)
    reloj.after(200, actualizar_hora)
 
root = tk.Tk()
root.title("Reloj")
root.geometry("400x300")

reloj = tk.Label(root, font=('times', 30, 'bold'), bg='yellow')
reloj.pack(fill="both", expand=1)

actualizar_hora()

root.mainloop()