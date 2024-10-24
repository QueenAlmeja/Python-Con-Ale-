"""
Hemos visto que existen distintos tipos de datos, pero ¿Se podría transformar un dato de tipo str en un int?

Aunque la pregunta parece algo extraño, debemos recordar que todo dato declarado entre comillas simples, dobles o triples es un
string, así que si, podemos encontrar numeros que sean cadena de texto y no funciones correctamente si queremos hacer operaciones. 
Pero ¿cómo saber que tipo de dato está contenido en una variable?
"""

#Antes de explicar la transformación de datos, recordemos una de la funciones básicas de python.
#type() es una función que nos ayuda al determinar que tipo de dato está almacenado en una variable. Ejemplos:

name = "Estefania"
age = 34
money = 23.4 
datos_personales = {"Profesion":"Comediante", "Programa":"El cuartico Podcast", "Pais":"Venezuela", "Amigos": 4}

#Usamos la funcion type() en conjunto con print()

print(type(name)) #str
print(type(age)) #int
print(type(money)) #float
print(type(datos_personales)) #dict

#Tranformemos datos

#De string a int

num1 = "342"
print(int(num1))

#otra forma

camb_num = int(num1)
print(camb_num)

#Si queremos comprobar que el valor de la variable num1 cambio, podemos usar la funcion type.

print(type(int(num1)))
print(type(camb_num)) 

#De int a str. 

num2 = 128
print(str(num2))

camb_num2 = str(num2)
print(camb_num2) 

#Que pasa si intenamos sumar los valores de las variables num1 y num2 una vez que hemos hecho em cambio?

#suma_num = camb_num + camb_num2
#print(suma_num)

"""
Python nos dira el siguiente error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
Esto se debe a que los valores de la variable no corresponden al mismo tipo de dato y Python no puede sumar o concatenar la informacion
Esto es parte del pensamiento logico que debemos ir desarrollando mientras aprendemos a programar.

🔴Las operaciones deben realizarse entre variables que contengan tipos de datos iguales. 
"""

#De str a float

num3 = "23.45"
print(float(num3))

camb_num3 = float(num3)
print(camb_num3)

#De float a str

num4 = 34.56
print(str(num4))

camb_num4 = str(num4)
print(camb_num4)

#🔴No todas las cadenas de texto se pueden transformar en numeros. Ejm:

name = "José"
#print(int(name))
#Python nos indicará que hay un error
#Lo ideal es que cuando hagamos estas tranformaciones, el contenido de str que queremos modificar, sea un valor numerico.

#Sobre las cadena de texto si podemos hacer otras transformaciones.

#De str a list
print(list(name))

lista = list(name)
print(lista)

#De list a str

lista_2 = ["Nombre", "Apellido", "Edad"]

print(str(lista_2))

cosas = str(lista_2)
print(cosas)

#De str a tuple

last_name = "Echeverria"
print(tuple(last_name))

#De tupla a str

tupla = ("comida", "peliculas", "libros", "pizza")
print(str(tupla))

#De str a set 

name2 = "Maria"
print(set(name2))

#De set a str

set = {"cosa1", "cosa2", "cosa3"}
print(str(set))

#🟢Reto: ¿Cómo comprobarias que los cambios del tipo de dato efectuados en los ultimos ejercicios se realizaron correctamente?