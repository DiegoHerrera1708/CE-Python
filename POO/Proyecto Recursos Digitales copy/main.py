from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital
from persistence.json_manager import cargar_recursos, guardar_recursos
from persistence.sqlite_manager import init_db

RUTA_JSON = "POO/Proyecto Recursos Digitales copy/data/recursos.json"
RUTA_DB = "POO/Proyecto Recursos Digitales copy/data/recursos.db"

# Muestra el menú por pantalla
def mostrar_menu()-> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 2 - JSON) ===")
    print("1. Listar recusos")
    print("2. Añadir recursos (demo)")
    print("3. Guardar en JSON")
    print("4. Cargar desde JSON (reemplaza la lista actual)")
    print("5. Salir")

# Prueba de creación de recurso
init_db(RUTA_DB)
