from LibroDigital import LibroDigital


class BibliotecaDigital:
    def __init__(self):
        self.__recursos = []

    def añadir_recurso(self, recurso):
        self.__recursos.append(recurso)

    def listar_recursos(self):
        for recurso in self.__recursos:
            print(f"{recurso.tipo()} - {recurso.desc()}")

    def abrir_todos(self):
        for recurso in self.__recursos:
            print(recurso.abrir())