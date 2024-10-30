"""
Las variables o datos del tipo boolean sólo poseen dos estados: True or False
En python cuando creamos variables que contienen datos booleanos, la primera letra de la
palabra True y False 📌SIEMPRE debe ir en mayúscula.

Vamos con ejemplos:
"""

is_girl = True
print(is_girl)
is_kind = True
print(is_kind) 
is_pet = False
print(is_pet)
is_kids = False
print(is_kids)


"""
Un valor booleano no sólo se obtienen como lo hemos declarado o almacenado en una variable, también
los podemos encontrar cuando hacemos comparaciones de datos, desarrollamos bloques de código con los
condicionales, entre otros. 

Ejem: Hagamos una comparacion de cadenas y valores numericos
"""
flor1 = "Rosa"
flor2 = "Margarita"
print(f"La palabara 'Rosa' posee más letras que la palabra 'Margarita' : {flor1 == flor2}")

#empleando números

num1 = 345.6
num2 = 54
print(f"El número {num1} es mayor que el número {num2}: {num1 > num2}")

print(f"Alejandra es una chica: {is_girl}")

"""
🟢 Reto

a. Crea 4 variables con características que puedan describirte como las declaradas en el primer ejemplo
b. Crear variables que contengan valores strings y/o númericos y compara dichas variables para 
comprobar que valor booleano obtendras

Pregunta⚡

Qué resultado arrojaria Python si comparas una variable que contiene un dato del tipo int con una
variable que guarda un dato del tipo str?
""" 
