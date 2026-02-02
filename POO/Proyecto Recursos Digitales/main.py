from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital
from .persistence.json_manager import cargar_recursos, guardar_recursos

RUTA_JSON = "data/recursos.json"

# Muestra el menú por pantalla
def mostrar_menu()-> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 2 - JSON) ===")
    print("1. Listar recusos")
    print("2. Añadir recursos (demo)")
    print("3. Guardar en JSON")
    print("4. Cargar desde JSON (reemplaza la lista actual)")
    print("5. Salir")

#Prueba de creación de recurso
def alta_demo(biblio: BibliotecaDigital) -> None:
    nuevo = Podcast(
        titulo="Python en producción",
        autor="CE DALP",
        anio=2026,
        num_episodios=1,
        tema="Programación"
    )
    biblio.agregar_recurso(nuevo)
    print("Recurso añadido:", nuevo)

if __name__ == "__main__":
    biblio = BibliotecaDigital()

    #Carga automática al iniciar la aplicación
    recursos = cargar_recursos(RUTA_JSON)
    biblio.reemplazar_todos(recursos)
    print(f"Cargados {len(recursos)} recursos desde {RUTA_JSON}")


    # Crear algunos recursos
    libro1 = LibroDigital("Python desde cero", "Ana López", 2022, 350, "PDF")
    video1 = VideoCurso("POO en Python", "Javier Caselli", 2023, 90, "Intermedio")
    podcast1 = Podcast("Tecnología hoy", "Laura Gómez", 2021, 24, "Innovación")

    # Crear la biblioteca y añadir recursos
    biblio = BibliotecaDigital("Biblioteca FP Informática")
    biblio.agregar_recurso(libro1)
    biblio.agregar_recurso(video1)
    biblio.agregar_recurso(podcast1)

    # Listar recursos
    biblio.listar_recursos()
    print()

    # Abrir todos los recursos
    biblio.abrir_todos()
    print()

    # Probar la encapsulación: cambiar el año de un recurso
    print("Cambiando el año del libro...")
    libro1.anio = 2024
    print("Cambiando el nivel del vídeo...")
    video1.nivel = "Avanzado"
    print()
    biblio.listar_recursos()
