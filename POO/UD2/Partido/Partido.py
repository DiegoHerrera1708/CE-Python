from Equipo import Equipo
from Jugador import Jugador
import random

class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipos = {
            equipo1.nombre : 0,
            equipo2.nombre : 0
        }
        self.equipo1 = equipo1
        self.equipo2 = equipo2
    
    def anotar_gol(self):
        listaEquipos = [self.equipo1, self.equipo2]
        equipoAnotador = random.randrange(0, 2)
        equipo = listaEquipos[equipoAnotador]
        for i in self.equipos.keys():
            if i == equipo.nombre:
                self.equipos.update({equipo.nombre : (self.equipos[equipo.nombre]+1)})
                if i == self.equipo1.nombre:
                    self.equipo1.goles += 1
                    anotador = random.randrange(5)
                    print(f"Gol de {self.equipo1.jugadores[anotador].nombre}")
                else:
                    self.equipo2.goles += 1
                    anotador = random.randrange(5)
                    print(f"Gol de {self.equipo2.jugadores[anotador].nombre}")

        self.mostrar_resultado()

    def mostrar_resultado(self):
        print(self.equipos)

    def finalizar_partido(self):
        print("Partido Finalizado")
        self.mostrar_resultado()


vinicius = Jugador("Vinicius", 7, "delantero")
lamine_yamal = Jugador("Lamine Yamal", 10, "delantero")
isco = Jugador("Isco", 22, "medio")
pedri = Jugador("Pedri", 8, "medio")
juan_mata = Jugador("Juan Mata", 6, "medio")
kante = Jugador ("Kante", 5, "medio")
sergio_ramos = Jugador("Sergio Ramos", 4, "defensa")
puyol = Jugador("Puyol", 3, "defensa")
kiko_casilla = Jugador("Kiko Casilla", 1, "portero")
kameni = Jugador("Kameni", 13, "portero")

rmadrid = Equipo([vinicius, isco, juan_mata, sergio_ramos, kiko_casilla], "Real de Madrid")
fcbarcelona = Equipo([lamine_yamal, pedri, kante, puyol, kameni], "FC Barcelona")

elClasico = Partido(rmadrid, fcbarcelona)
elClasico.anotar_gol()
elClasico.anotar_gol()
elClasico.anotar_gol()
elClasico.anotar_gol()
elClasico.anotar_gol()
print()
elClasico.finalizar_partido()


print(elClasico.equipo1.goles)
