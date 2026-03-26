# Modules (Módulos) en Python
# Permiten reutilizar código en diferentes archivos sin duplicarlo.

# Ejemplo sin módulos (mala práctica)
def sum_two_values(a, b):
    print(a + b)

sum_two_values(5, 3)


# Si copiamos esta función en muchos archivos:
# Problema: código duplicado
# Difícil de mantener
# Si hay errores, hay que arreglarlos en todos lados


# Uso de módulos (buena práctica)

# Supongamos que tenemos un archivo llamado my_module.py
# con funciones dentro

# Importar todo el módulo
import my_module

# Acceder a sus funciones usando nombre_modulo.funcion()
print(my_module.suma(5, 3, 8))
my_module.saludar("Jonathan")


# Importación específica

# Importar solo funciones concretas
from my_module import suma, saludar

print(suma(10, 5, 2))
saludar("Python")


# Error común: nombre de módulo inválido

# Esto daría error:
# import 10_functions

# Python no permite nombres de módulos que empiecen por números


# Uso de módulos integrados (math)
import math

# Constante pi
print(math.pi)

# Potencia: 2^8
print(math.pow(2, 8))


# Importación específica desde math
from math import pi
print(pi)


# Uso de alias (renombrar)
from math import pi as PI_VALUE
print(PI_VALUE)