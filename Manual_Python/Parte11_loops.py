# Loops (Bucles)
# Repiten un bloque de código.

#  Bucle While 
# Repite mientras una condición sea verdadera.

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    # El else se ejecuta cuando el bucle termina de forma natural
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

# Detener un bucle while con break
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

# Bucle FOR
# Permite recorrer elementos de una colección.

# Lista con tus datos y números del ejemplo
my_list = [21, 1.74, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

# Set con tus datos
my_set = {"Jonathan", "Villamizar", 21}
for element in my_set:
    print(element)

# Tupla con tus datos
my_tuple = (21, 1.74, "Jonathan", "Villamizar")
for element in my_tuple:
    print(element)    

# Dict con tus datos
my_dict = {"Nombre": "Jonathan", "Apellido": "Villamizar", "Edad": 21, 1: "Python"}

# Por defecto recorre las claves
for element in my_dict:
    print(element)

# Para recorrer valores
for element in my_dict.values():
    print(element)

# Continue
# Salta a la siguiente iteración.
for element in my_dict:
    if element == "Edad":
        continue
    print(element)
else:
    print("El bucle for para diccionario ha finalizado")