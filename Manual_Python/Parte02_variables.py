#Nombrar variable así

my_string_variable= "my string variable"
print(my_string_variable)

# Así es incorrecto

#first-name
#first@name
#first$name
#num-1
#1num

#Estilo recomendado ESTILO snake_case -> Todo en minúsculas con guiones bajos

Myvariable = "My string variable"
print(Myvariable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)


#Convertimos el tipo int a String
my_int_to_str_variable= str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


#Función len()

#Para contar cuántos elementos tiene un objeto.
print(len(my_string_variable))


#Declarar y asignar varias variables en una sola línea.
name, surname, alias, age = "Jonathan", "Villamizar", "JonathanSKR7", "21"
print("Me llamo: ", name, surname, ". Mi edad es: ", age, " y mi nickname es: ", alias)



#Función input()
# Se utiliza para recibir datos del usuario a través del teclado.
# El valor introducido siempre se guarda como una cadena de testo (str)

first_name = input("Cuál es tu nombre?: ")
age = input("Cuál es tu edad?: ")

print(first_name)
print(age)


"""first_name = input("Cuál es tu nombre?: ")
age = input("Cuál es tu edad?: ")

print(first_name)
print(age)"""


#Cambiamos su tipo

name = 21
age = "Jonathan"


# Forzamos el tipo
addres = str("Mi dirección")
addres = 32
addres = True
addres = 2.2
print(type(addres))




