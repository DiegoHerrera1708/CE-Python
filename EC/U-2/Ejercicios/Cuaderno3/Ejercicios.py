from tkinter import *
from collections import deque
from tkinter import messagebox


class Window:
    def __init__(self, master):
        self.master = master

        self.Main = Frame(self.master)

        self.stack = deque(maxlen=10)
        self.stackcursor = 0

        self.L1 = Label(self.Main, text="This is my NotePad")
        self.L1.pack(padx=5, pady=5)

        self.T1 = Text(self.Main, width=80, height=20)
        self.T1.pack(padx=5, pady=5)

        self.menu = Menu(self.Main)
        self.menu.add_command(label="Print", command=self.print_stack)
        self.menu.add_command(label="Undo", command=self.undo)
        self.menu.add_command(label="Redo", command=self.redo)
        self.menu_colores = Menu(self.Main, tearoff=0)
        self.menu.add_cascade(label="Fondo", menu=self.menu_colores)
        self.menu_colores.add_command(label="Blanco", command=lambda: self.cambiarColor("Blanco"))
        self.menu_colores.add_command(label="Negro", command=lambda: self.cambiarColor("Negro"))
        self.menu_colores.add_command(label="Azul", command=lambda: self.cambiarColor("Azul"))



        self.master.config(menu=self.menu)

        self.B1 = Button(self.Main, text="Print", width=8, command=self.display)
        self.B1.pack(padx=5, pady=5, side="left")

        self.B2 = Button(self.Main, text="Clear", width=8, command=self.clear)
        self.B2.pack(padx=5, pady=5, side="left")

        self.B3 = Button(self.Main, text="Undo", width=8, command=self.undo)
        self.B3.pack(padx=5, pady=5, side="left")

        self.B4 = Button(self.Main, text="Redo", width=8, command=self.redo)
        self.B4.pack(padx=5, pady=5, side="left")

        self.Main.pack(padx=5, pady=5)

    def display(self):
        print(self.T1.get("1.0", "end"))

    def clear(self):
        respuesta = messagebox.askyesno("Clear","¿Desea limpiar el texto?")
        if respuesta:
            self.T1.delete("1.0", "end")
        else:
            pass

    def stackify(self):
        texto = self.T1.get("1.0", "end - 1c")
        if texto.lower() == "error":
            print("Palabra reservcada en pantalla")
        else:
            self.stack.append(self.T1.get("1.0", "end - 1c"))
            if self.stackcursor < 9: self.stackcursor += 1
        if len(texto) < 50:
            self.T1.config(width=80, height=20)
        elif len(texto) >50 and len(texto) < 200:
            self.T1.config(width=120, height=30)
        else:
            self.T1.config(width=160, height=40)

    def undo(self):
        if self.stackcursor != 0:
            self.clear()
            if self.stackcursor > 0: self.stackcursor -= 1
            self.T1.insert("1.0", self.stack[self.stackcursor])

    def redo(self):
        if len(self.stack) > self.stackcursor + 1:
            self.clear()
            if self.stackcursor < 9: self.stackcursor += 1
            self.T1.insert("1.0", self.stack[self.stackcursor])

    def print_stack(self):
        for i, stack in enumerate(self.stack):
            print(f"{i} {stack}")
    
    def cambiarColor(self, color):
        if color =="Blanco":
            self.T1.config(bg="white")
        elif color =="Negro":
            self.T1.config(bg="black")
        else:
            self.T1.config(bg="blue")



root = Tk()
window = Window(root)
root.bind("<Key>", lambda event: window.stackify())
root.mainloop()