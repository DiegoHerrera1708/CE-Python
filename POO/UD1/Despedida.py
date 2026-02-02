class Despedida:
    def __init__(self, nombre, hora = 12):
        self.nombre = nombre
        self.hora = hora

    def mostrar_despedida(self):
        if self.hora < 12:
            print(f"¡Que tengas una excelente mañana, {self.nombre}!")
        elif self.hora > 11 and self.hora < 21:
            print(f"¡Que tengas una buena tarde, {self.nombre}!")
        else:
            print(f"¡Que tengas una buena noche, {self.nombre}!") 

    @classmethod
    def desde_texto(cls, texto):
        d = texto.split(",")
        return cls(d[0], int(d[1]))
    
    @staticmethod
    def es_hora_valida(hora):
        if hora >= 0 and hora < 24:
            return True
        else:
            return False
        
d = Despedida("Diego")
d.mostrar_despedida()
d = Despedida.desde_texto("Jose,21")
d.mostrar_despedida()
print(Despedida.es_hora_valida(0))
print(Despedida.es_hora_valida(32))