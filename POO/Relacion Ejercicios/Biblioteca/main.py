from BibliotecaDigital import BibliotecaDigital
from LibroDigital import LibroDigital
from Podcast import Podcast
from VideoCurso import VideoCurso

def main():
    libro = LibroDigital("El mago", "Joel Lopez", 1992, 234, "Normal")
    video = VideoCurso("Top 10 Equipos de futbol", "Josegamer888", 2024, 12, "Intermedio")
    podcast = Podcast("Las leyes de Newton", "Newton", 1970, 10, "Ciencia")
    biblioteca = BibliotecaDigital()
    biblioteca.añadir_recurso(libro)
    biblioteca.añadir_recurso(video)
    biblioteca.añadir_recurso(podcast)

    biblioteca.listar_recursos()
    print()
    biblioteca.abrir_todos()

    video.set_autor("Manolo77")
    print(video.get_autor())

main()