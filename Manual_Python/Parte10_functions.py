#  Functions (Funciones) en Python
# Bloque de código reutilizable.

# Definición con def
def my_function():
    print("Esto es una función")

my_function()

# Función con parámetros
# Python acepta los valores sin validar tipos estrictamente (tipado dinámico)
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values("5", "7") # Concatenación de strings

# Funciones con return
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Parámetros con nombre
def print_name(name, surname):
    print(f"{name} {surname}")

# DATOS PERSONALIZADOS
print_name(surname="Villamizar", name="Jonathan")

# Parámetros con valor por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jonathan", "Villamizar")

# Parámetros variables con *args
# Recibe un número indeterminado de argumentos en una tupla.
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Developer")