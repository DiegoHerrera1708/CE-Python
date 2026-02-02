class Vehiculo:
    VehiculosCreados = []
    kilometrosTotales = 0
    def __init__(self, kilometrosRecorridos):
        self.kilometrosRecorridos = kilometrosRecorridos

class Bicicleta(Vehiculo):
    def __init__(self, kilometrosRecorridos):
        super().__init__(kilometrosRecorridos)
    
    def hacerElCaballito(self):
        print("¡Estoy haciendo el caballito!")

class Coche(Vehiculo):
    def __init__(self, kilometrosRecorridos):
        super().__init__(kilometrosRecorridos)
    
    def quemarRueda(self):
        print("¡Estoy quemando rueda con el coche!")


bici = Bicicleta(0)
coche = Coche(0)
Vehiculo.VehiculosCreados = [bici, coche]

while True:
    print('''\nElige una opcion para hacer:
        1. Anda con la bicicleta
        2. Haz el caballito con la bicicleta
        3. Anda con el coche
        4. Quema rueda con el coche
        5. Ver kilometraje de la bicicleta
        6. Ver kilometraje del coche
        7. Ver kilometraje total
        8. Salir''')
    respuesta = int(input(""))

    match respuesta:
        case 1:
            kilometrosRecorrer = int(input("¿ Cuántos kilómetros quiere recorrer ? "))
            bici.kilometrosRecorridos += kilometrosRecorrer
            bici.kilometrosTotales += kilometrosRecorrer
        case 2:
            bici.hacerElCaballito()
        case 3:
            kilometrosRecorrer = int(input("¿ Cuántos kilómetros quiere recorrer ? "))
            coche.kilometrosRecorridos += kilometrosRecorrer
            coche.kilometrosTotales += kilometrosRecorrer
        case 4:
            coche.quemarRueda()
        case 5:
            print(f"La bicicleta lleva recorridos {bici.kilometrosRecorridos} kilometros")
        case 6:
            print(f"El coche lleva recorridos {coche.kilometrosRecorridos} kilometros")
        case 7:
            for i in Vehiculo.VehiculosCreados:
                Vehiculo.kilometrosTotales += i.kilometrosRecorridos
            print(f"Los vehiculos llevan recorridos: {Vehiculo.kilometrosTotales}")
        case 8:
            print("¡Hasta la proxima!")
            break
        case _: 
            print("Número introducido no valido")