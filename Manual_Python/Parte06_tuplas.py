# Tuplas en Python
# Una tupla es una estructura de datos similar a una lista, pero con una diferencia clave:
# sus elementos no se pueden modificar después de ser creados.
# Esto las hace inmutables, a diferencia de las listas, que sí son mutables.

# Cómo crear una tupla:
my_tuple = tuple()     # Forma 1: usando el constructor tuple()
my_other_tuple = ()    # Forma 2: usando paréntesis

# Creamos una tuple
my_tuple = (21, 1.74, "Jonathan", "Villamizar")
print(my_tuple)
print(type(my_tuple))

# Al igual que las listas, las tuplas permiten acceder a sus elementos usando índices.
print(my_tuple[0])    # Primer elemento
print(my_tuple[-1])   # Último elemento
# print(my_tuple[4])   # IndexError: índice fuera de rango
# print(my_tuple[-6])  # IndexError: índice fuera de rango

# Nota: Si nombramos la variable como “tuple”, pero usamos corchetes [],
# Python entenderá que estamos creando una lista, no una tupla.
my_tuple = [21, 1.77, "Jonathan", "Villamizar"]
print(type(my_tuple))

# Restauramos la tupla para los siguientes ejemplos
my_tuple = (21, 1.74, "Jonathan", "Villamizar")

# El método .count() funciona igual en las tuplas que en las listas.
# Sirve para contar cuántas veces aparece un valor dentro de la estructura.
print(my_tuple.count("Jonathan"))

# El método .index() se utiliza para encontrar la posición (índice) de un elemento.
print(my_tuple.index("Jonathan"))
print(my_tuple.index("Villamizar"))

# Nota: Las tuplas son inmutables.
# my_tuple[1] = 1.80  # Python mostrará un error (TypeError)

# Concatenación de tuplas
# Aunque las tuplas no se pueden modificar, podemos unir (concatenar) dos o más para crear una nueva.
my_other_tuple = (1, 2, 3)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# ¡Recordemos! Convertir una tupla en lista
# Como las tuplas son inmutables, no se pueden cambiar directamente.
# Pero Python permite convertir una tupla en lista usando el constructor list().
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "Ilerna"      # Reemplaza el valor
my_tuple.insert(1, "Azul")  # Inserta el elemento "Azul"
print(my_tuple)             # Muestra la lista actualizada

# Una vez realizados los cambios, volvemos a convertirla en tupla
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Operador del
# En las tuplas, la única forma de “borrar” algo es eliminar toda la variable.
# del my_tuple[2]   # Error: 'tuple' object doesn't support item deletion
del my_tuple        # Elimina completamente la tupla