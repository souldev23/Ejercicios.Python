# Por especificación las variables compuestas se definen separando con guión medio y usando minusculas.
nombre_variable = 'Mi primer varible'
""" 
Las constantes usadas en otros lenguajes, en Python no existen así que solo para indicar que es contsante
se colocan con todos sus caracteres en mayuscula.
"""
SOY_CONSTANTE = "No deberían cambiar mi valor"

# Para asignar un valor desde linea de comandos se declara así:

entrada_de_teclado = input("Escribe algo:\n")
print("Usted escribió: \n" + entrada_de_teclado)

# Para declarar más de una variable en una linea:
var1, var2, var3 = 1, "valor 2", '3'
print(var1, var2, var3)

# Para obtener el tipo de una variable:
print(type(var1), type(var2), type(var3))

# Para cambiar entre tipos de datos se usa lo siguiente:
edad = int(input("Escribe tu edad: "))
estatura = float(input("Escribe tu estatura: "))
mayor_de_edad = edad >= 18

print("Tu edad es:\n",edad)
print("Mides:\n",estatura)
print("¿Eres mayor de edad?\n" + str(mayor_de_edad))
