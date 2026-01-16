#  Conditionals en Python
# Los condicionales permiten que un programa tome decisiones (if, elif, else).

# Crear una condición if
my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")
print("La ejecución continúa")

# Nota: Indentación es obligatoria en Python.

# Else
# Si la condición del if NO es verdadera, ejecuta lo que está dentro del else.
my_condition = 5 * 2

if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

# Operadores lógicos (and, or, not)
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

# Strings vacíos en condicionales
# Una cadena vacía ("") se considera False.
my_string = ""
if not my_string:
    print("Mi cadena de texto es vacía")