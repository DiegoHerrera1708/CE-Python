class Usuario:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

    def presentacion(self):
        print(f"Soy {self.__nombre} y mi correo es {self.__email}")

class Alumno(Usuario):
    def __init__(self, nombre, email, curso, nota_media ):
        super().__init__(nombre, email)
        self.curso = curso
        self.nota_media = nota_media

    def presentacion(self):
        print(f"Soy {self.getNombre()}, estudiante de {self.curso}, con una nota media es {self.nota_media}.")

    
class Profesor(Usuario):
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self.especialidad = especialidad

    def presentacion(self):
        print(f"Soy el profesor {self.getNombre()}, especialista en {self.especialidad}.")


if __name__ == "__main__":

    usuario1 = Usuario("Ana", "ana@example.com")
    alumno1 = Alumno("Luis", "luis@example.com ", "Matemáticas", 8.5)
    profesor1 = Profesor("María", "maria@example.com", "Física")

    lista = [usuario1, alumno1, profesor1]
    
    for i in lista:
        i.presentacion()