# String (cadena de texto) 

#Hola mundo
print("Hola Python")
print('Hola Python')



#Números en Python 

# Enteros (Integer)
# Flotantes (Float) números decimales
# Complejos (Complex) Números con parte real y parte imaginaria (la imaginaria se indica con j) Ejemplo: 1 + j, 2 + 4j
 


# Booleanos

# True or False \ T or F (Mayúsculas)



#Lista

# Colección ordenada y mutable de elementos (Números, cadenas, booleanos, incluso otras listas).
# Se definen con [] y los elementos se separan con comas.

mi_lista = [1, "hola", True, 3.5, [2,4]]
# Permite duplicados



#Tupla (Tuple)

# Colección ordenada pero inmutable.
# Se definen con () y los elementos separados con comas.

mi_tupla = (1, "hola", True, 3.5)
#Permite duplicados



#Conjunto (Set)

#Es igual una colección de elementos pero a diferencia de las anteriores NO TIENE ORDEN ESPECÍFICO
# No permite duplicados (Solo valores únicos)
# Se definen con {}

mi_conjunto = {1,2,3,4}
print(mi_conjunto) #Resultado: {1,2,3,4}



# Función type()

# Se usa para conocer el tipo de dato de un valor o de una variable

print(type("hola python")) #'str'
print(type(5)) #'int'
print(type(1.5)) #'float'
print(type(True)) #'bool'
print(type(3 + 1j)) #'complex'
