# Dicts en Python (Diccionarios)
# Estructura de datos que almacena información mediante pares clave–valor.

# Crear un dict
# 1. Usando el constructor dict()
my_dict = dict()
print(type(my_dict))

# 2. Usando llaves {}
my_other_dict = {}
print(type(my_other_dict))

# Creación con DATOS PERSONALIZADOS
# Python permite usar claves de distintos tipos.
my_other_dict = {
    "Nombre": "Jonathan",
    "Apellido": "Villamizar",
    "Edad": 21,
    1: "Python"
}

# ¿Podemos crear una clave cuyo valor sea un set? Sí.
my_dict = {
    "Nombre": "Jonathan",
    "Apellido": "Villamizar",
    "Edad": 21,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
}

# Evitar confusiones al contar elementos con len()
# len() cuenta cuántas claves tiene el diccionario.
print(len(my_other_dict))
print(len(my_dict))

# Acceder a un valor usando su clave
print(my_dict["Nombre"])

# Modificar un valor en un diccionario
my_dict["Nombre"] = "Pedro" # Ejemplo de modificación
print(my_dict["Nombre"])

# Agregar una nueva clave con su valor
my_dict["Calle"] = "Calle nou"
print(my_dict)

# Eliminar un elemento concreto (del)
del my_dict["Calle"]
# Si no especifico la clave, borro el diccionario entero: del my_dict

# ¿Qué pasa si usamos in en un diccionario? Busca por CLAVE.
print("Nombre" in my_dict) # True

# Más Métodos de los diccionarios
print(my_dict.items())   # devuelve pares clave–valor
print(my_dict.keys())    # devuelve solo las claves
print(my_dict.values())  # devuelve solo los valores

# Nota sobre el método fromkeys()
# Crea un diccionario nuevo desde cero.
my_new_dict = dict.fromkeys(my_dict) # Crea claves sin valores (None)
print(my_new_dict)

# Asigna valor por defecto "Jonathan" a todas las claves
my_new_dict = dict.fromkeys(my_dict, "Jonathan") 
print(my_new_dict)