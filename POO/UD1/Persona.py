class Person:
    def __init__(self, name, age, street):
        self.name = name 
        self.age = age
        self.street = street

    def myfunc(self):
        print("Hello my name is " + self.name)
    

    def datos(self):
        print("Nombre: " + self.name + "\nEdad: " + str(self.age) + "\nCiudad: " + self.street)

    def cambiarNombre(self, nuevo_nombre):
        self.name = nuevo_nombre



if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    ciudad = input("Ingresa tu ciudad: ")

    respuesta = input("Deseas cambiar tu nombre? (si/no): ")

    if respuesta.lower() == "si":
        nuevo_nombre = input("Ingresa tu nuevo nombre: ")
        nombre = nuevo_nombre

    p1 = Person(nombre, edad, ciudad)

    p1.datos()