import tkinter as tk

class TimerApp:
    def __init__(self):
        self.tiempo_inicial = 10
        self.running = False
        self.tiempo_restante = self.tiempo_inicial
        self.label = tk.Label(font=("Arial", 24), text=f"Tiempo: {self.tiempo_inicial}")
        self.label.pack(pady=20)
        self.btn = tk.Button(text="Iniciar/Pausar", command=self.toggle_timer)
        self.btn.pack()

    def toggle_timer(self):
        if self.running:
            self.running = False
        else: 
            if self.tiempo_restante < 0:
                self.tiempo_restante = self.tiempo_inicial
                self.label.config(text=f"Tiempo: {self.tiempo_inicial}")
            self.running = True
            self.countdown()
            
    def countdown(self):
        if self.running and self.tiempo_restante >= 0:
            self.label.config(text=f"Tiempo: {self.tiempo_restante}")
            self.tiempo_restante -= 1
            bucle = self.label.after(1000, self.countdown)

        if self.tiempo_restante < 0 and self.running:
            self.label.config(text="¡Tiempo agotado!")
            self.running = False
            self.label.after_cancel(bucle)

        if not self.running:
            self.label.after_cancel(bucle)

        



            

ventana = tk.Tk()
ventana.title("Temporizador")
ventana.geometry("500x400")

t = TimerApp()

ventana.mainloop()