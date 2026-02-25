# Classes (Clases) en Python
# Permiten crear objetos a partir de un molde.

# Clase vacía
class MyEmptyPerson:
    pass


# Definición de una clase con constructor
class Person:

    # Constructor (__init__)
    # Se ejecuta automáticamente al crear un objeto
    def __init__(self, name, surname):
        # self representa la instancia del objeto
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

    # Método (acción del objeto)
    def walk(self):
        print(f"{self.full_name} está caminando")


# Crear un objeto (instancia)
my_person = Person("Jonathan", "Villamizar")

# Acceder a atributos
print(my_person.name)
print(my_person.surname)
print(my_person.full_name)

# Ejecutar método
my_person.walk()


# Modificar un atributo directamente
# En Python los atributos son públicos por defecto
my_person.full_name = "Jonathan El Pro"

print(my_person.full_name)
my_person.walk()