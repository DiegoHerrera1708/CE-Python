'''
Haz una lista con los atributos que podría tener la clase caballo. A continuación haz una lista con los posibles métodos (acciones asociadas a los caballos). 
Hecho esto implementa la clase Caballo y pruébala creando instancias y aplicándole algunos métodos.
Ejemplo:
Hola, me llamo Babieca
Tocotoc tocotoc tocotoc
Hiiiiiiieeeeee
Hola, yo soy Lykos
Ñam ñam ñam
Tocotoc tocotoc tocotoc
'''

class Caballo:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")
    
    def relinchar(self):
        print("Hiiiiiiieeeeee")
    
    def galopar(self):
        print("Tocotoc tocotoc tocotoc")

caballo1 = Caballo("Babieca", "Pura Raza Española")
caballo1.saludar()
caballo1.galopar()
caballo1.relinchar()
