# Sets en Python (Conjuntos)
# Son estructuras de datos que permiten almacenar valores únicos, es decir, no admiten repetidos. Además no mantienen un orden definido.

# Si usas llaves {} vacías, Python interpreta que estás creando un diccionario, no un set.
# Para crear un set vacío siempre hay que usar set().
# Pero si el set tiene elementos si puedes usar {}


# Sets
my_set = set() # Crea un conjunto vacío
my_other_set = {} #Crea un diccionario vacío

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Jonathan", "Villamizar", 21} #Crea un conjunto
print(type(my_other_set))


print(len(my_other_set))



#Cuándo se añade un elemento a un set, no garantiza que aparezca al final, ni en un lugar concreto.
my_other_set.add("Guaido")
print(my_other_set)

#Si un elemento aparece dos veces, solo se guarda una vez
