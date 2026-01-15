# Jonathan Villamizar - DAM 2

# Situación : Solo se pueden registrar entre 0 y 12 horas de trabajo al día.

#Instrucciones:
# Crea una variable que represente las horas trabajadas.
# Utiliza el operador lógico (and) para comprobar que el valor esté dentro del rango permitido y muestra un mensaje adecuado.

hours_worked = 8

if hours_worked >= 0 and hours_worked <= 12:
    print("The worked hours are within the allowed range.")
else: 
    print("Error: the number of worked hours is outside the allowed range.")