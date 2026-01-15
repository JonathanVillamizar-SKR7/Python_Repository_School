# Una Tupla 
# Es una estructura de datos similar a una lista, pero con una diferencia clave: No se pueden modificar sus elementos después de ser creados. INMUTABLES

my_tuple = tuple() #Forma 1
my_other_tuple = () #Forma 2

my_tuple = (21, 1.74, "Jonathan", "Villamizar")
print(my_tuple)
print(type(my_tuple))


# Tupla accediendo a sus elementos usando índices
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Jonathan"))


# .index() se utiliza para encontrar la posición (indice) de un elemento dentro de la dupla
print(my_tuple.index("Jonathan"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)



# Convertir una tupla en lista
# con list()

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "Ilerna"
#Ahora si se puede modificar. Deja de ser inmutable
print(my_tuple)


#Se Convierte de nuevo en tuple
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


# del elimina completamente la tupla
del my_tuple
