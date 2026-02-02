class Punto: 
    def __init__(self, x=0, y=0): 
        self.x = x 
        self.y = y
        self.constante = 5

    def __str__(self):
        return f"Punto x: {self.x}, Punto y: {self.y}, Constante: {self.constante})"

p = Punto(2, 3)
print(p.__str__())