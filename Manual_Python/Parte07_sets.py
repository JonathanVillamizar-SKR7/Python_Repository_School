# Sets en Python (Conjuntos)
# Los sets o conjuntos en Python son estructuras de datos que permiten almacenar valores únicos.
# No admiten elementos repetidos y no mantienen un orden definido.

# Nota importante:
# Si usás llaves {} vacías, Python interpreta que estás creando un diccionario.
# Para crear un set vacío, siempre tenés que usar set().

my_set = set()      # crea un conjunto vacío
my_other_set = {}   # Crea un diccionario vacío
print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

# DATOS PERSONALIZADOS
my_other_set = {"Jonathan", "Villamizar", 21} # crea un conjunto
print(type(my_other_set))

# Usamos len para mirar cuantos objetos tenemos dentro del set.
print(len(my_other_set))

# Diferencias: Los sets NO mantienen orden.
my_other_set.add("Jonathan") # Un set NO reconoce elementos repetidos
print(my_other_set) 
# Cada ejecución puede mostrar un orden diferente.

# Comprobar existencia (in)
# Los set son muy rápidos para buscar elementos.
print("Jonathan" in my_other_set)
print("Villamizar" in my_other_set)

# Eliminar elementos de un set (.remove)
my_other_set = {"Python", "Jonathan", "Developer"}
my_other_set.remove("Jonathan")
print(my_other_set)

# Vaciar un set completo (.clear)
my_other_set.clear()
print(my_other_set)

# Eliminar por completo un set (del)
del my_other_set

# Convertir un set en list
# Ahora puedes usar índices (my_list[0]), cosa que los set no permiten.
my_set = {"Jonathan", "Villamizar", 21}
my_list = list(my_set)
print(my_list)
print(my_list[0])

# Unir conjuntos con el método union()
# Une conjuntos, elimina duplicados automáticamente y devuelve un nuevo conjunto.
my_other_set = {"java", "php", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# Diferencia - Intersección en set
# Elementos que están en my_new_set pero NO en my_set
print("Diferencia:", my_new_set.difference(my_set))

# Elementos que están en ambos conjuntos
print("Intersección:", my_set.intersection(my_other_set))