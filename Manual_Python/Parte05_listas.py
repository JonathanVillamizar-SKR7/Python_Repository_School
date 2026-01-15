# Una lista en Python
# es una estructura de datos que permite almacenar varios elementos dentro de una sola variable.
# A diferencia de los tipos de datos base (int, float, bool, str), una lista no es un tipo simple, sino un contenedor que puede guardar muchos valores.

my_list = list() #Forma 1
my_other_list = [] #Forma 2 (Más común)


# Conocer la cantidad de elementos que contiene una lista len()
print(len(my_list))


#Posiciones (Indices) en una lista comienzan en 0.

my_list= [35,24,61,46,24,67,12]  
print(my_list)
print(len(my_list))


my_other_list = [21, 1.74, "Jonathan", "Villamizar"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[3])

print(my_other_list[-1])
print(my_other_list[-2])



print(my_other_list.count("Jonathan"))
print(my_list.count(24))


#Desempaquetado
age, height, name, surname = my_other_list

#Desempaquetado de listas
age, height, name, surname = my_other_list[2], my_other_list[1],my_other_list[0], my_other_list[3]

print(age)
print(name)


#Concatenación
print(my_list + my_other_list)


#Operador .append : Es un método propio de las listas en Python que se utiliza para agregar un elemento al final de una lista existente.
my_other_list.append("Ilerna")
print(my_other_list)



#Operador .insert : Inserta un elemento en una posición especifica dentro de una lista
my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)




# Operador .remove() Elimina el primer elemento que coincida con el valor indicado dentro de la lista
my_list.remove(24)
print(my_list)



#Operador .pop() se utiliza para eliminar elementos de una lista pero a diferencia de .remove(), trabaja con el indice (posicion) del elemento y devuelve el valor eliminado.
print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)



#Operador del : se utiliza en python para eliminar elementos de una lista indicando su posición (índice)
del my_list[2]
print(my_list)


# Operador .clear() se utiliza para vaciar completamente una lista, es decir, elimina todos sus elementos pero mantiene la lista creada.
my_list.clear
print(my_list)



# Metodo .copy() permite duplicar listas sin modficar la original
my_new_list = my_list.copy()


#Método .reverse() se utiliza para invertir el orden de los elementos de una lista existente.
#No crea una nueva lista sino que modifica directamente la original
my_new_list.reverse()
print(my_new_list)



# Método .sort() se utiliza para ordenar los elementos de una lista
my_new_list.sort()
print(my_new_list)

