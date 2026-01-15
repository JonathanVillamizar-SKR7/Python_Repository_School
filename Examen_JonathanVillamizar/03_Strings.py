# Jonathan Villamizar
# DAM 2

# Pide al usuario una frase y muestra cuántas veces aparece la letra 'a' usando el metodo .count()
# Pide una palabra y conviertela a:
# · Mayúscula = .upper()
# · Minúscula = .lower()
# · Capitalizada = .capitalize()



# Uso el input() para pedir la frase, y dentro del segundo print uso la funcion str para convertir el .count() en str y no de error al momento de imprimir.
frase = input("Dame una frase: ")
print(frase)
print("La letra 'a' se repiten: "
      + str(frase.count("a")) + " veces")

# Pido una palabra al usuario
palabra = input("Dame una palabra: ")

# Mayúscula
print(palabra.upper)

# Minúscula
print(palabra.lower)

# Capitalizada
print(palabra.capitalize)
