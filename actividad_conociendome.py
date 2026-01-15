# Datos personales
# ____________________________________________________________________________________________

# Se crea tres variables para guardar: nombre (str), edad (int), si es estudiante (bool)
nombre_completo = "Jonathan José Villamizar Guaido"
edad = 21
es_estudiante = True

#Imprimo los datos 

print("Mis datos personales\n")
print("Hola muy buenasss")
print(f"Soy {nombre_completo} y tengo {edad} años.")
print(f"¿Soy actualmente estudiante? {es_estudiante}")
print("Estoy estudiando DAM en Ilerna :)\n")

#Ahora se verifican los tipos de datos
print("Verificación de Tipos")
print("'nombre_completo':", type(nombre_completo))  
print("'edad':", type(edad))                     
print("'es_estudiante':", type(es_estudiante))  

#Modifico la variable edad para ver que sucede al cambiar un dato
es_estudiante = False
print("\nModificando...")
print("¿Soy estudiante ahora? : ", es_estudiante)


# Gustos personales
# ____________________________________________________________________________________________

#Pregunto al usuario sus gustos personales
print("\nGustos Personales")
print("Quiero que me digas 3 cosas que te gustan\n")
gusto_1 = input("Escribe tu primer gusto: ")
gusto_2 = input("Escribe tu segundo gusto: ")
gusto_3 = input("Escribe tu tercer gusto: ")

#Guardo sus 3 gustos en una lista llamada "gustos"

gustos = [gusto_1, gusto_2, gusto_3]


#Imprimo la lista
print("\nTu lista de gustos:", gustos)
#Ahora imprimo la cantidad de elementos que tiene la lista
print("La lista 'gustos' tiene", len(gustos), "elementos.")

#Creo una lista más pero con los elementos duplicados
gustos_modificados = gustos * 2
#Y la imprimo:
print("Lista de gustos repetidos (gustos * 2):", gustos_modificados)

# Cuando se multiplica una lista por un número entero, el resultado es una nueva lista que repite todos los elementos de la lista original 
# tantas veces quieras porque las listas son mutables.


# Comidas favoritas
# ____________________________________________________________________________________________

# Se crea una tuple llamada comidas_favoritas con tres comidas
comidas_favoritas = ("Sushi", "Pizza", "Grill")

# Enseñar tuple
print("\nComidas Favoritas (Tupla)")
print("Mi tupla de comidas favoritas es: ", comidas_favoritas)

# Ahora se intenta modificar algun dato de la tuple solo por experimento
# Intento de modificación (esta línea causará un error):

# comidas_favoritas = "Empanadas"

# Si se descomenta la línea 'comidas_favoritas = "Empanadas"', el programa generará un error de tipo (TypeError) en tiempo de ejecución.
# Esto pasa porque las tuplas son inmutables, y una vez creada ya no se puede modificar.


# Conteo de cantidad de comidas que hay.
print("La tupla 'comidas_favoritas' tiene", len(comidas_favoritas), "elementos.")


# Conjunto de números
# ____________________________________________________________________________________________

print("\nConjunto de Números (Set)")

# Se crea un conjunto SET con algunos números repetidos, este se llamará:
numeros = {10, 20, 30, 30, 40, 50, 50}

# Se muestra por pantalla el resultado de la lista, y se verá que no se repiten los datos.
print("Conjunto 'numeros':", numeros) 

# Ahora se reescribe la variable colocando otro número
# El operador | realiza la operación de unión entre conjuntos.
numeros = numeros | {60}

# Se vuelve a enseñar el conjunto
print("Conjunto 'numeros' después de añadir {6}:", numeros)

# Comentario explicando por qué los valores repetidos no aparecen más de una vez.

# Los valores repetidos no aparecen más de una vez en el conjunto 'numeros'
# porque la principal característica de los Conjuntos (Set) en Python es que NO
# permiten duplicados. Solo almacenan valores únicos.



# Tipos de datos y resumen
# ____________________________________________________________________________________________

print("\nTipos de Datos y Resumen")

# Se muestra el tipo de dato con type()
print("Tipo de 'nombre_completo':", type(nombre_completo))      # Debe ser str
print("Tipo de la lista 'gustos':", type(gustos))              # Debe ser list
print("Tipo de la tupla 'comidas_favoritas':", type(comidas_favoritas)) # Debe ser tuple
print("Tipo del conjunto 'numeros':", type(numeros))            # Debe ser set

# Se crea una lista (resumen) con todo lo que se ha hecho 
resumen = [gustos, comidas_favoritas, numeros]

print("Contenido de la lista 'resumen':", resumen)

#Observación:
#La lista 'resumen' puede contener elementos de diferentes tipos de datos,
#incluyendo otras colecciones completas (la lista 'gustos', la tupla
#'comidas_favoritas' y el conjunto 'numeros').



# Reto de lógica
# ____________________________________________________________________________________________

print("\nReto de Lógica")

# Se usa la edad guardada de la parte 1, en este caso sería (21).

# Escribe un bloque de código que imprima un mensaje diferente según la edad, usando if, elif, else y operadores lógicos.
if edad < 18:
    # Si la edad es menor a 18 (True o False)
    print("Resultado de la lógica:", "Eres menor de edad.")
elif edad >= 18 and edad <= 30:
    # Condición combinada con 'and'. Debe ser mayor o igual a 18 Y menor o igual a 30.
    print("Resultado de la lógica:", "Eres joven adulto.")
else:
    # Si no se cumplen las dos condiciones anteriores
    print("Resultado de la lógica:", "Eres adulto.")

# 4. Explica en un comentario qué hace tu código y por qué.

# El código utiliza una estructura condicional (if, elif, else) para tomar una
# decisión lógica basada en el valor numérico de la variable 'edad'.

# a. El 'if' evalúa la primera condición (edad < 18).

# b. Si esa es falsa, el 'elif' evalúa la segunda condición, que utiliza el operador
# lógico 'and' para asegurarse de que la edad esté estrictamente en el rango de 18 a 30.

# c. Si ambas condiciones fallan, el bloque 'else' se ejecuta por defecto, indicando
# que la edad es mayor de 30.
