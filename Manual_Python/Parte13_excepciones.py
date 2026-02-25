# Exceptions (Excepciones) en Python
# Permiten controlar errores y evitar que el programa se detenga.

number_one = 5
number_two = "1"

# try - except básico
try:
    print(number_one + int(number_two))
    print("No se ha producido un error")
except:
    print("Se ha producido un error")


# try - except - else - finally
try:
    print(number_one + number_two)  # Esto produce TypeError
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
else:
    print("La ejecución continúa correctamente")
finally:
    print("Fin del bloque de control de excepciones")


# Capturar el error en una variable
try:
    print(number_one + number_two)
except Exception as error:
    print("Se ha producido un error:")
    print(error)