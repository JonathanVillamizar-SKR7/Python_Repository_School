# Jonathan Villamizar
# DAM 2


#Solicita al usuario su nombre, edad y ciudad:
# Usa input() para pedir cada dato.
#Convierte la edad a entero con int()
#Guarda los datos en una lista llamada datos_usuario
# Muestra la lista completa
# Muestra un mensaje formateado usando f-strings, por ejemplo:
#"Me llamo____, tengo___ años y vivo en _____"
# Muestra cuántos elementos tiene la lista usando len()



#Solicito datos al usuario

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
ciudad = input("Dime en qué ciudad vives: ")

#Convierto la edad a int
edad_int = int(edad)

# Guardo los datos en una lista
datos_usuario = [nombre, edad, ciudad]


#Muestro la lista completa
print(datos_usuario)


# Mensaje:
print("Hola mi nombre es " + nombre + ", tengo " + edad + " años de edad y vivo en " + ciudad)


# len()

print(len(datos_usuario))