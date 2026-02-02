"""
Crea las clases Animal, Mamifero, Ave, Gato, Perro, Canario, Pinguino y Lagarto. Crea, al menos, tres métodos específicos de
cada clase y redefine el/los método/s cuando sea necesario. Prueba las clases creadas en un programa en el que se instancien objetos y se les apliquen métodos
"""

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

class Mamifero(Animal):
    def amamantar(self):
        print(f"{self.nombre} está amamantando a sus crías.")
    
    def caminar(self):
        print(f"{self.nombre} está caminando.") 
    
    def jugar(self):
        print(f"{self.nombre} está jugando.")

class Ave(Animal):
    def volar(self):
        print(f"{self.nombre} está volando.")
    
    def cantar(self):
        print(f"{self.nombre} está cantando.")
    
    def construir_nido(self):
        print(f"{self.nombre} está construyendo un nido.")

class Gato(Mamifero):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Miau!")
    
    def rascar(self):
        print(f"{self.nombre} está rascando el sofá.")
    
    def cazar(self):
        print(f"{self.nombre} está cazando un ratón.")

class Perro(Mamifero):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Guau!")
    
    def traer(self):
        print(f"{self.nombre} está trayendo la pelota.")
    
    def cavar(self):
        print(f"{self.nombre} está cavando un hoyo.")

class Canario(Ave):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Pío Pío!")
    
    def volar_alto(self):
        print(f"{self.nombre} está volando alto en el cielo.")
    
    def cantar_melodias(self):
        print(f"{self.nombre} está cantando melodías.")

class Pinguino(Ave):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Honk Honk!")
    
    def nadar(self):
        print(f"{self.nombre} está nadando en el agua.")
    
    def deslizarse(self):
        print(f"{self.nombre} se está deslizando sobre el hielo.")

class Lagarto(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido sibilante.")
    
    def tomar_sol(self):
        print(f"{self.nombre} está tomando el sol.")
    
    def mudar_piel(self):
        print(f"{self.nombre} está mudando su piel.")

gato = Gato("Misi", 3)
gato.hacer_sonido()
perro = Perro("Rex", 5)
perro.hacer_sonido()
canario = Canario("Piolín", 1)
canario.hacer_sonido()
pinguino = Pinguino("Pingu", 4)
pinguino.hacer_sonido()
lagarto = Lagarto("Rango", 2)
lagarto.hacer_sonido()  
