class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        if porcentaje > 0 and porcentaje < 100:
            return porcentaje * self.precio / 100
        else:
            return print ("El descuento no entra dentro del 0-100%")
    
    @classmethod
    def desde_texto(cls, texto):
        producto = texto.split(",")
        return cls(producto[0], float(producto[1]))
    
    @staticmethod
    def es_precio_valido(precio):
        if precio > 0:
            return True
        else: 
            return False
        
p = Producto("lata", 21.23)
print(p.aplicar_descuento(60))
print(Producto.desde_texto("coche,23.1"))
print(Producto.es_precio_valido(12))