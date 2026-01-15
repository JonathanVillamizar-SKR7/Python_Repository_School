my_stringg = "My String"
my_other_string = 'My another String'

print(len(my_stringg))
print(len(my_other_string))

print(my_stringg + my_other_string)
print(my_stringg + "" + my_other_string)


my_tab_strings = "\tEste es un String con Tabulación"
print(my_tab_strings)

my_scape_string = "\tEste es un String \n escapado"
print (my_scape_string)

my_scape_stringg = "\\t Este es un String \\n escapado"
print(my_scape_stringg)

name, surname, age = "Jonathan", "Villamizar", 21
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

print("Mi nombre es %s %s  y mi edad es %d" % (name,surname,age))

language = "Python"

a, b, c, d, e, f = language

print(a) #Muestra P
print(e) #Muestra o


# División (SLICING) de cadenas
# (Rebanado o división)

language_slice = language[1:3]
print(language_slice)
"""Toma los caracteres desde el índice 1 hasta 2 (el 3 no se
incluye).
Resultado: "yt";"""


language_slice = language[1:]
print(language_slice) #Desde el 1 hasta el final

language_slice = language[-2:]
print(language_slice)


# Reverse invertir una cadena en Python
# Reversed con un Slicing

reversed_language = language[::-1]
print(reversed_language)

print(language.capitalize())  # 1. Primera letra en mayúscula
print(language.upper()) # 2. Todo en mayúsculas
print(language.count("t"))  # 3. Cuenta cuántas veces aparece "t"
print(language.isnumeric()) # 4. Verifica si todos los caracteres son numéricos
print("1".isnumeric())  # 5. Ejemplo: True porque "1" es un número
print(language.lower()) # 6. Todo en minúsculas
print(language.upper().isupper()) # 7. Comprueba si está en mayúsculas
print(language.startswith("py")) # 8. Este método verifica si la cadena
# almacenada en la variable language no empieza con el texto "py";.


#Actividad
# Pedir una palabra al usuario
palabra = input("Ingresa una palabra: ")

# Mostrar en mayúsculas
print("En MAYÚSCULAS:", palabra.upper())

# Mostrar en minúsculas
print("En minúsculas:", palabra.lower())

# Mostrar con la primera letra en mayúscula
print("Capitalizada:", palabra.capitalize())


# ==== Segunda parte: pedir una frase ====
frase = input("\nIngresa una frase: ")

# Contar cuántas veces aparece la letra 'a'
cantidad_a = frase.count("a")
print("La letra 'a' aparece:", cantidad_a, "veces")

# Verificar si la frase contiene solo números
print("¿La frase contiene solo números?:", frase.isdigit())

# Verificar si la frase está completamente en mayúsculas
print("¿La frase está en MAYÚSCULAS?:", frase.isupper())


# ==== Tercera parte: verificar formato de una palabra ====
nueva_palabra = input("\nIngresa otra palabra para analizar su formato: ")

# Ver si está toda en mayúsculas
if nueva_palabra.isupper():
    print("¡Muy formal!")
# Ver si está toda en minúsculas
elif nueva_palabra.islower():
    print("¡Muy relajado!")
# Ver si está capitalizada (primera letra mayúscula y resto minúsculas)
elif nueva_palabra.istitle():
    print("¡Perfecta presentación!")
# Cualquier otra cosa
else:
    print("Formato mixto.")


#Actividad 2
# Guardamos una palabra en la variable language
language = "palabra"   # Puedes cambiarla para probar

# 1. Primera letra en mayúscula
print("1. Capitalizada:", language.capitalize())

# 2. En mayúsculas
print("2. En MAYÚSCULAS:", language.upper())

# 3. Cuántas veces aparece la letra "t"
print("3. Número de 't':", language.count("t"))

# 4. Si la palabra está formada solo por números
print("4. ¿Solo números?:", language.isnumeric())

# 5. Comprobación numérica usando el texto "1"
print("5. ¿'1' es numérico?:", "1".isnumeric())

# 6. La palabra en minúsculas
print("6. En minúsculas:", language.lower())

# 7. Si la palabra está completamente en mayúsculas
print("7. ¿Está en MAYÚSCULAS?:", language.isupper())

# 8. Si la palabra comienza con "py"
print("8. ¿Comienza con 'py'?:", language.startswith("py"))
