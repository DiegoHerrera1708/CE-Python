from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital
from persistence.sqlite_manager import init_db, cargar_recursos

RUTA_JSON = "POO/proyectoBibliotecaDigitalSQLite/data/recursos.json"
RUTA_DB = "POO/proyectoBibliotecaDigitalSQLite/data/recursos.db"

#1 Muestra el menú por pantalla
def mostrar_menu() -> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 3 - SQLite)===")
    print("1. Listar Recursos")
    print("2. Añadir recursos")
    print("3. Borrar recurso")
    #print("4. Guardar en la base de datos")
    #print("5. Cargar desde la base de datos (reemplaza la lista actual)")
    print("6. Salir")

#2 Listar recursos
def listar_recursos(biblioteca: BibliotecaDigital) -> None:
    recursos = biblioteca.listar_recursos()
    if not recursos:
        print("No hay recursos en la biblioteca.")
        return

    print("\n---LISTADO DE RECURSOS---")
    for recurso in recursos:
        print(recurso)

#3 Añadir recursos 
def anadir_recurso(biblioteca: BibliotecaDigital) -> None:
    recurso = crear_recurso_desde_teclado()

    if recurso is None:
        return

    biblioteca.agregar_recurso(recurso)
    print("Recurso añadido correctamente.")

#3.1 Obtiene informacion del usuario para crear un nuevo recurso
def crear_recurso_desde_teclado() -> RecursoDigital :
    print("\n---CREAR NUEVO RECURSO---")
    tipo = input("Tipo (LibroDigital, VideoCurso, Podcast): ").strip()

    if tipo not in ["LibroDigital", "VideoCurso", "Podcast"]:
        print("Tipo no válido. Debe ser 'LibroDigital', 'VideoCurso' o 'Podcast'.")
        return None

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = int(input("Año de publicación: ").strip())

    if tipo == "LibroDigital":
        isbn = input("ISBN: ").strip()
        num_paginas = int(input("Número de páginas: ").strip())
        formato = input("Formato (PDF, EPUB, etc.): ").strip()
        return LibroDigital(id=None, titulo=titulo, autor=autor, anio=anio,
                            isbn=isbn, num_paginas=num_paginas, formato=formato)

    elif tipo == "VideoCurso":
        duracion = int(input("Duración en minutos: ").strip())
        nivel = input("Nivel (Principiante, Intermedio, Avanzado): ").strip()
        return VideoCurso(id=None, titulo=titulo, autor=autor, anio=anio,
                          duracion=duracion, nivel=nivel)

    elif tipo == "Podcast":
        episodio = int(input("Número de episodio: ").strip())
        url = input("URL del podcast: ").strip()
        return Podcast(id=None, titulo=titulo, autor=autor, anio=anio,
                       episodio=episodio, url=url)

def borrar_recurso(biblioteca: BibliotecaDigital) -> None:
    recursos = biblioteca.listar_recursos()
    if not recursos:
        print("No hay recursos para borrar.")
        return

    print("\n---BORRAR RECURSO---")
    for recurso in recursos:
        print(recurso)

    try:
        id_borrar = int(input("Ingresa el ID del recurso a borrar: ").strip())
    except ValueError:
        print("ID no válido. Debe ser un número entero.")
        return

    if biblioteca.borrar_recurso(id_borrar):
        print(f"Recurso con ID {id_borrar} borrado correctamente.")
    else:
        print(f"No se encontró ningún recurso con ID {id_borrar}.")

def main() -> None:
    #1 Crear esquema si no existe
    init_db(RUTA_DB)
    
    # Crear biblioteca digital (almacenamiento en memoria)
    biblioteca = BibliotecaDigital("Mi Biblioteca Digital")

    #2 Muestra el menú
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        match opcion:
            case "1":
                listar_recursos(biblioteca)
            case "2":
                anadir_recurso(biblioteca)
            case "3":
                borrar_recurso(biblioteca)
            # case "4":
            #    pass
            # case "5":
            #     recursos = cargar_recursos(RUTA_DB)
            #     biblioteca.reemplazar_todos(recursos)
            #     print(f"Cargados {len(biblioteca.listar_recursos())} recursos desde la base de datos.")
            case "6":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, por favor selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()