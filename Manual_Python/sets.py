# Crear un set
frutas = {"manzana", "pera", "banana"}
print(frutas)

# Agregar un elemento al set
numeros = {1, 2, 3}
numeros.add(4)
print(numeros)   # {1, 2, 3, 4}

# Eliminar un elemento (remove)
colores = {"rojo", "verde", "azul"}
colores.remove("verde")  # Si no existe → error
print(colores)

# Unión de dos sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}

# Intersección de dos sets
x = {10, 20, 30}
y = {20, 30, 40}
print(x.intersection(y))  # {20, 30}
