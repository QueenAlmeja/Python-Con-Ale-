"""
Cuando se definen funciones, podemos encontrar varias formas de emplear los parametros.
Pero como se emplean los parametros y los argumentos la momento de declara una funcion?

Aunque al momento de diseñar de una función se deben tomar en cuenta los parametros y argumentos
no todas la funciones declaradas deben tener prestablecidos parametros

def greetings():
    print("Bienvenido a Pythonland")

greetings()
"""

#📌Los parametros seran las variables definidas dentro de la funcion declarada
#📌Los argumento seran los valores que se pasan a la funcion


#Definiendo funciones: Parametros y Argumentos

#1. Posicional: Se pasa en el orden que se han definido
def saludo(nombre, apellido): #nombre y apellido son los parametros de entrada
    print(f"Hola {nombre}, Tu apellido es {apellido}?")
saludo("Alejandra", "Sanchez") #Alejandra y Sanchez son los argumentos 

#2. Con nombre: Los argumentos se pasaran usando el nombre del parametro al que se quiere asignar el valor
def saludo(nombre, edad):
    print(f"Hola {nombre}, Tu edad es {edad}?")
saludo(edad=40, nombre="Alejandra") 

"""
Si a una funcion se le dan mas o menos argumento que los parametros que han sido definido, 
puede generarse un error, sin embargo pueden existir parametros con valores preestablecidos
⬇️
"""
#3 Predeterminados: Uno de los parametros tiene un valor predeterminado que se puede emplear si no se le proporciona argumento

def suma(a, b=6):
    resultado = a + b
    return resultado
print(suma(3)) #como te das cuenta, aqui solo se le proporciono el argumento del parametro a

#4 args: acepta un numero variable de parametros posicionales
def numeros_sumatoria(*args):
    contador = 0
    for i in args:
        contador += i
    return contador
print(f"La sumatoria de los parametros es: {numeros_sumatoria(1,45,6,78,9,46,23,12)}")

#5  **kwargs: acepta un numero variable de parametros con nombre

def numero_contados(**kwargs):
    a = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        a += value
    return a
numero_contados(x=34, y=12, z=56)

"""
Algo muy importante dentro de uso de funciones es el uso del return
"""