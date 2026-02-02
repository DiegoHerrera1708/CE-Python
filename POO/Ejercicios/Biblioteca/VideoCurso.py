from RecursoDigital import RecursoDigital

class VideoCurso(RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion_minutos, nivel ):
        super().__init__(titulo, autor, anio)
        self.duracion_minutos = duracion_minutos
        self.nivel = nivel 

    def abrir(self):
        return f"Video-Curso abierto"
    
    def tipo(self):
        return "Video"
    
    def desc(self):
        return f"{super().__str__()}, Duración: {self.duracion_minutos} minutos, Nivel: {self.nivel}"