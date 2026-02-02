'''
Docstring for Relacion Ejercicios.Biblioteca
Se quiere informatizar una biblioteca. Crea las clases Publicacion, Libro y Revista. Las clases deben estar implementadas con la jerarquía correcta. 
Las características comunes de las revistas y de los libros son:
El código ISBN
El título
El año de publicación. 

Los libros tienen, además, un atributo que indica si está o no prestado. Cuando se crean los libros, no están prestados. 
Las revistas tienen un número. 
La clase Libro debe implementar un Protocolo Prestable que tiene los métodos presta(), devuelve() y estaPrestado().
Hacer un método “main” para probar lo implementado
'''

class Publicacion:
    def __init__(self, isbn, titulo, anio_publicacion):
        self.isbn = isbn
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion

class Libro(Publicacion):
    def __init__(self, isbn, titulo, anio_publicacion):
        super().__init__(isbn, titulo, anio_publicacion)
        self.prestado = False

    def presta(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devuelve(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def estaPrestado(self):
        return self.prestado
    
class Revista(Publicacion):
    def __init__(self, isbn, titulo, anio_publicacion, numero):
        super().__init__(isbn, titulo, anio_publicacion)
        self.numero = numero


if __name__ == "__main__":
    libro1 = Libro("123-456-789", "El Quijote", 1605)
    revista1 = Revista("987-654-321", "Revista de Ciencia", 2021, 42)

    libro1.presta()
    print(f"¿Está prestado el libro? {libro1.estaPrestado()}")
    libro1.devuelve()
    print(f"¿Está prestado el libro? {libro1.estaPrestado()}")