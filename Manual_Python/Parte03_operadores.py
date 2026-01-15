# Operadores
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)



# Operador Módulo (%) 
# Devuelve el residuo (resto) de una división entre dos números

print(3 % 4)
print(10 % 3)



# Operación una división entera (//) también llamada floor division
print(10 // 3)

# El operador // divide el número de la izquierda entre el de la derecha, pero descarta la parte decimal, quedándose solo con la parte entera del resultado



# Operador de potenciación (**)

print(2**3)


# El operador (+) entre cadenas de texto (strings) las concatena, es decir, las unes
print("hola"+"python")


# Sin embargo, no todos los signos u operadores pueden ejecutarse en
# cualquier contexto.
#Por ejemplo, los operadores - y * funcionan correctamente con números, pero

# si los usamos con texto u otros tipos de datos no compatibles, Python
# mostrará un error.
print ("hola"+"python")
print ("hola"-"python")
print ("hola"*"python")
print("Hola"+"Python"+ "¿Qué tal?")

# No se puede mezclar str con números
print("Hola"+5)


#Pero así
print("Hola" +str(5))


# Con el signo * también funcioná para multiplicar strings
print("Hola " * 5)


print("hola"* 2.5) #Error


my_float = 2.5 * 2
print("Hola" *int(my_float))



# Operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)


#Cómo funcionan las comparaciones entre strings
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Hola")
print("aaaa" > "abaa") # Ordenación alfabética
print(len("aaaa") > len("abaa"))# Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

#Cuando comparas cadenas en Python:
#- Se comparan carácter por carácter según su valor Unicode (ASCII).
#- Las mayúsculas y minúsculas no son iguales: 'H' (72)
# 'P' (80)

# Por eso "Hola < "Python" → True (porque 'H' tiene un valor
# menor que 'P').



# Operadores lógicos
# AND, OR Y NOT
# Se utilizan para combinar o modificar condiciones que devuelven valores booleanos (True o False)

# AND (Y lógico) : Devuelve True solo si ambas condiciones son verdaderas
print(3>2 and 5>4)

# OR (O lógico) : Devuelve True si al menos una condición es verdadera.
print (3>2 or 5<4)

# NOT (Negación lógica) : Invierte el valor lógico: True pasa a False y viceversa 
print(not(3 > 2)) #false


# Operador and - or  
print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 > 4 and "Hola" < "Python")
print (3 < 4 or "hola" > "Python")


# Prioridad general de operadores lógicos en Python
# Python sigue un orden fijo sin precedencia, es decir, decide que partes evaluar primero:
# 1. Parentesis () -> Todo lo que esté dentro se evalúa primero
# 2. not -> Se evalúa despues de los paréntesis, ya que niega el valor lógico.
# 3. and -> Se evalúa después de not
# 4. or -> Se evalúa al final
print(3<4 or ("Hola" > "Python" and 4 == 4))


# Paréntesis primero
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
# → (True or (False and True)) → (True or False) → True


# Uso de not antes que and
print(not 3 > 4 and 2 == 2)
# → (not False and True) → (True and True) → True


# Paréntesis + not + or
print((not (5 == 5)) or (10 > 2))
# → (not True or True) → (False or True) → True


# and se evalúa antes que or
print(True or False and False)
# → True or (False and False) → True or False → True


# Expresión más compuesta
print((3 > 2 and not (4 < 2)) or (7 == 8))
# → ((True and not False) or False) → (True and True) or False → True or False → True



# Operador not
# Lógica buliana
# El operador not se utiliza para negar o invertir el valor lógico de una expresión
# Convierte un valor True en False, y un valor False en True
# Se utiliza para expresar "lo contrario" de una afirmación.
print(not(3 > 4)) # Primero evalúa la expresión dentro de la paréntesis (False) luego actúa el not (False->True)


print(not (5 > 3))   # False -> porque 5 > 3 es True, y not True = False

print(not (2 == 10)) # True -> porque 2 == 10 es False, y not False = True

print(not ("hola" == "adiós"))  # True -> porque "hola" == "adiós" es False, y not False = True

activo = True
print(not activo)    # False -> porque activo es True, y not True = False

edad = 20
mayor_de_edad = edad >= 18
print(not mayor_de_edad)  # False -> porque edad >= 18 es True, y not True = False

