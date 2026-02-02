import datetime
class Persona:
    def __init__(self, dni, nombre, apellidos, fechaNacimiento):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fechaNacimiento = datetime.datetime(fechaNacimiento)

    def getDni(self):
        return self.dni

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Fecha de nacimiento: {self.fechaNacimiento}"
    
class Modulo:
    def __init__(self, nombre, horas):
        self.nombre = nombre
        self.horas = horas
    
    def getNombre(self):
        return self.nombre
    
    def getHoras(self):
        return self.horas
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Horas: {self.horas}"
    

class Calificacion(Modulo):
    def __init__(self, modulo):
        self.modulo = modulo
        self.notaFinal = 0

    def getModulo(self):
        return self.modulo

    def getNotaFinal(self):
        return self.notaFinal
    
    def setNotaFinal(self, nota):
        self.notaFinal = nota

class Alumno(Persona, Calificacion):
    def __init_(self, dni, nombre, apellidos, fechaNacimiento, ciclo):
        super().__init__(dni, nombre, apellidos, fechaNacimiento)
        self.ciclo = ciclo
        self.calificaciones = []

    def matricular(self, modulo):
        c = Calificacion(modulo)
        self.calificaciones.append(c)

    def calificar(self, modulo, nota):
        for m in self.calificaciones:
            if m.getModulo().getNombre() != modulo.getNombre():
                c = Calificacion(modulo)
                self.calificaciones.append(c)
                m.setNotaFinal(nota)
            else:
                print("El modulo ya esta añadido")

    def promociona(self):
        result = False
        suma_horas_modulos = 0
        total_horas = 0
        
        for c in self.calificaciones:
            if c.getNotaFinal()>4:
                suma_horas_modulos+= c.getModulo().getHoras()
            total_horas += c.getModulo().getHoras()
        
        if suma_horas_modulos>= (total_horas/2):
            result = True

        return result
    
    def getNotaMedia(self):
        nota_total = 0
        for c in self.calificaciones:
            nota_final += c.getNotaFinal()
        return nota_total/len(self.calificaciones)
    
    def __str__(self):
        return super().__str__()+f", Nota media: {self.getNotaMedia:.2f}"
