# Proyecto Recursos Digitales 📚

Un sistema de gestión de biblioteca digital en Python que permite almacenar, organizar y gestionar diferentes tipos de recursos digitales como libros, videos y podcasts.

## 📋 Descripción

Este proyecto implementa una **Biblioteca Digital** capaz de gestionar múltiples tipos de recursos digitales. Cada recurso tiene propiedades comunes (título, autor, año) y comportamientos específicos según su tipo.

## 🏗️ Estructura del Proyecto

```
Proyecto Recursos Digitales/
├── main.py                  # Archivo principal con ejemplos de uso
├── README.md               # Este archivo
├── data/
│   └── recursos.json       # Almacenamiento de datos en JSON
├── models/
│   ├── __init__.py
│   ├── RecursoDigital.py   # Clase base para todos los recursos
│   ├── BibliotecaDigital.py# Gestión de la biblioteca
│   ├── LibroDigital.py     # Implementación de libros
│   ├── Podcast.py          # Implementación de podcasts
│   ├── VideoCurso.py       # Implementación de videos/cursos
│   └── __pycache__/
└── persistence/
    ├── __init__.py
    └── json_manager.py     # Gestor de persistencia en JSON
```

## 🎯 Características Principales

### Clases Disponibles

- **RecursoDigital**: Clase base que define la estructura común de todos los recursos
  - Atributos: título, autor, año
  - Métodos: getters/setters, descripción, abrir, tipo

- **BibliotecaDigital**: Gestiona la colección de recursos
  - Añadir recursos
  - Listar todos los recursos
  - Abrir todos los recursos

- **LibroDigital**: Tipo específico de recurso (hereda de RecursoDigital)
  - Propiedades adicionales: número de páginas, tipo de encuadernación

- **VideoCurso**: Tipo específico de recurso (hereda de RecursoDigital)
  - Propiedades adicionales: duración en horas, nivel de dificultad

- **Podcast**: Tipo específico de recurso (hereda de RecursoDigital)
  - Propiedades adicionales: duración en minutos, categoría

## 🚀 Instalación

No hay dependencias externas. Solo necesitas Python 3.6 o superior.

```bash
# Clonar o descargar el proyecto
cd "Proyecto Recursos Digitales"

# Ejecutar la aplicación
python main.py
```

## 💻 Ejemplo de Uso

```python
from models.BibliotecaDigital import BibliotecaDigital
from models.LibroDigital import LibroDigital
from models.Podcast import Podcast
from models.VideoCurso import VideoCurso

# Crear recursos
libro = LibroDigital("El mago", "Joel Lopez", 1992, 234, "Normal")
video = VideoCurso("Top 10 Equipos de futbol", "Josegamer888", 2024, 12, "Intermedio")
podcast = Podcast("Las leyes de Newton", "Newton", 1970, 10, "Ciencia")

# Crear biblioteca y agregar recursos
biblioteca = BibliotecaDigital()
biblioteca.añadir_recurso(libro)
biblioteca.añadir_recurso(video)
biblioteca.añadir_recurso(podcast)

# Listar y abrir todos los recursos
biblioteca.listar_recursos()
biblioteca.abrir_todos()

# Modificar propiedades
video.set_autor("Manolo77")
print(video.get_autor())
```

## 📦 Módulos

### models/
Contiene todas las clases del modelo de datos:
- Estructura orientada a objetos con herencia
- Encapsulamiento de datos privados
- Polimorfismo en métodos como `abrir()` y `tipo()`

### persistence/
Gestión de persistencia de datos:
- `json_manager.py`: Manejo de almacenamiento en JSON

### data/
Directorio para archivos de datos:
- `recursos.json`: Base de datos de recursos

## 🔧 Requisitos

- Python 3.6+
- No hay dependencias externas requeridas

## 📝 Notas

- Los recursos se almacenan en memoria durante la ejecución
- La persistencia en JSON está preparada para futuras implementaciones
- El sistema usa encapsulamiento con atributos privados (`__atributo`)

## 🎓 Propósito Educativo

Este proyecto es una aplicación educativa que demuestra:
- Programación Orientada a Objetos (POO)
- Herencia de clases
- Polimorfismo
- Encapsulamiento
- Gestión de colecciones

## 📄 Licencia

Proyecto educativo sin licencia específica.

---

**Última actualización**: Enero 2026
