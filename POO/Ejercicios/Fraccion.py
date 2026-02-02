"""
Crea la clase Fraccion. Los atributos serán numerador y denominador. Y algunos de los métodos pueden ser invierte, simplifica, multiplica, divide, etc. 
Prueba la clase creada en un programa en el que se instancien objetos y se les apliquen métodos.
"""

from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def invertir(self):
        self.numerador, self.denominador = self.denominador, self.numerador
    
    def simplificar(self):
        divisor = gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor
    
    def multiplicar(self):
        return self.numerador * self.denominador
    
    def dividir(self):
        return self.numerador / self.denominador
    
fraccion1 = Fraccion(8, 12)
print(f"Fracción original: {fraccion1.numerador}/{fraccion1.denominador}")
fraccion1.simplificar()
print(f"Fracción simplificada: {fraccion1.numerador}/{fraccion1.denominador}")
fraccion1.invertir()
print(f"Fracción invertida: {fraccion1.numerador}/{fraccion1.denominador}")
print(f"Multiplicación: {fraccion1.multiplicar()}")
print(f"División: {fraccion1.dividir()}")