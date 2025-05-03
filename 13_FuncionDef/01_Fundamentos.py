"""
La funcion def de python
Hasta este punto, ya hemos empleado algunas funciones de python como: len(), type(), str()...
Sin embargo, estas son funciones nativas del lenguaje de programacion. Sin embargo, en python
podemos crear nuestras propias funciones empleando la palabra reservada def.

Sintaxis basica de una funcion

def nombre_funcion(argumentos)
    #codigo a ejecutar
    return
"""
#Ejemplos generales de como definir funciones

def suma(a,b): #definimos la funcion que recibe dos valores
    resultado = a + b #escribimos el bloque de codigo que ejecutara la funcion
    return resultado
print(suma(10, 3))

#📌Esto lo podemos hacer mas complejo para que reciba parametros desde un user? Of course

def suma_user(): #definimos la funcion. No se especifican los parametros porque se van a ingresar desde el teclado
    user_a = float(input("Ingresa un valor numerico: ")) #ingresa el usuario el primer valor
    user_b = float(input("Ingresa otro valor numerico: ")) #ingresa el usuario el segundo valor
    resultado2 = user_a + user_b #se suman y se guardan los valores ingresados en esta variable
    return resultado2 #se devuelve el valor de la variable donde se almaceno la suma
    
print("La sumatoria de los valores ingresados es:", suma_user()) #llama e imprime el resultado

"""
Las funciones nos permiten:
Reutilizar parte del codigo para evitar repetir el codigo
Organizar y estructura el codigo para que sea mas claro y limpio
"""

#Tambien se pueden emplear string 

def mensaje():
    print("Hola, espero que estes bien")
mensaje()

def nombre(name):
    print("Hola ", name)
nombre("Victor")

"""
La manera en que se pasan los argumento de una funcion pueden varias y depende de lo que deseamos que 
ejecute el codigo
"""

#Por argumento: es la forma más básica para pasar los parametros
def resta(a,b): #el primer valor estara en la posicion a y el segundo corresponde a b
    return a - b
print(5,3) #a = 5 y b = 3
print(34-54)
#El numero de valores ingresados debe ser equivalente al numero de parametros establecidos. Sino, dara error

#argumentos por defecto
def dividir(b=45, a=36): #se definieron los valores de los parametros desde la entrada
    return a // b
print(dividir())

"""
Como te has podido dar cuenta una funcion def puede o no tener los parametros definidos. 
📌En los casos en que el codigo debe interactuar con un usuario, tal vez sea mejor no establecer parametros
Veamos cual es la diferencia entre parametros y argumentos con ejemplos practicos.
"""