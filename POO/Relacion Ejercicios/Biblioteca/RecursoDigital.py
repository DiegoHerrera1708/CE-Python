class RecursoDigital:
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    def get_anio(self):
        return self.__anio  
    
    def set_anio(self, anio):
        self.__anio = anio

    def descripcion_basica(self):
        print(f"Título: {self.__titulo}, autor: {self.__autor}, año: {self.__anio}")

    def abrir(self):
        print("Recurso digital abierto")
    
    def tipo(self):
        return f"Recurso genérico"
    
    def __str__(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}"