class Curso:

    usuarios = []
    calificaciones = []
    calificacion_promedio = 0.0

    def __init__(self, titulo, instructor, precio, clases):
        self.titulo = titulo
        self.instructor = instructor
        self.precio = precio
        self.clases = clases 

    def __str__(self):
        return f"Curso: {self.titulo}, Instructor: {self.instructor}, Precio: {self.precio}, Clases: {self.clases}, Usuarios: {len(self.usuarios)}, Calificaciones: {self.calificaciones}, Calificación Promedio: {self.calificacion_promedio}"
    
    def new_user_enrolled(self, usuario):
        Curso.usuarios.append(usuario)
    
    def received_a_rating(self, calificacion):
        Curso.calificaciones.append(calificacion)
        Curso.calificacion_promedio = sum(self.calificaciones) / len(self.calificaciones)

    def show_details(self, titulo):
        if self.titulo == titulo:
            print(f"Curso: {self.titulo}, Instructor: {self.instructor}, Precio: {self.precio}, Clases: {self.clases}")
        else:
            print("Curso no encontrado.")