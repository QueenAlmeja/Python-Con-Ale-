#Las strings se pueden concatenar de diferentes maneras:

#La principal forma de concatenar Strings es usando el simbolo +. Veamos ejemplos:

name = "Alejandra"
last_name = "Sanchez"
fullname = name + last_name
print(fullname) 

#🟢Reto: Como agregaria un espacio para separa las dos palabras que se concatenan en la variable fullname?

"""
Los valores de dos variables se puedieron agrupan en una sola variable empleando el método de concatenacion
Sin embargo, debemos tener cuidado al momento de emplear este método ya que, Python sólo puede concatenar variables
que poseen datos del mismo tipo. En caso contrario, se producira un error: 
"""

name = "Alejandra"
age = 30
#information = name + age
#print(information) 
"""
Al ejecutar el print(information), Python indicará que se ha producido un 
TypeError: can only concatenate str (not "int") to str, por ello lo dejamos como un comentario
"""

"""
Otro operador matemático que podemos emplear con los strings es el símbolo de la multiplicación *
Vamos con ejemplos
"""

#Multiplicando una cadena de texto por un número

word = "Mariposa"
print(word * 2)

#Formatos para manipular los strings

"""
Aunque la concatenación de variables con datos tipo string permite agrupar la informacion de varias variables en una sola,
existen métodos que facilitan la manipulacion de las variables que almacenas cadenas de texto y que ademas permiten agrupar
las variables que almacenan strings con variables que poseen datos númericos, conjuntos u otros elementos 
"""


#Empleando el simbolo %
"""
El operador % seguido de la letra s (%s) permite modificar o manipular variables que contienen datos de tipo str.
"""
#usando las variables ya declaradas creamos una nueva variable donde agrupamos la informacion del nombre, el apellido y la edad.

temple1 = "Mi nombre es %s, mi apellido es %s y actualmente tengo %d"%(name, last_name, age)
print(temple1)
#si quisieramos realizar el mismo ejercicio, pero desde la funcion print, la manera seria basimente la misma:
print("Mi nombre es %s, mi apellido es %s y actualmente tengo %d"%(name, last_name, age))

#el orden de las variables escrita entre los () debe corresponder a la manera en que esperamos que aparezcan en nuestro temple

"""
📌
para agregar el la variable de la edad, se empleo %d ya que el dato contenido el variable age, es un int
para agregar una variable que contenga un float, se emplearia %f 
Y para agregar un flotante con presion fija seria empleando %.number of digitsf. Veamos esto, con un ejemplo sencillo

Ejemplo

"""
number = 3.14159
ejemplo = "El numero es %.2f"%number #el 2 antes de la f indica que solo se veran reflejados en el output, los dos primeros decimales
print(ejemplo)

#Empleando la funcion format()
#Este estilo es muy parecido al anterior, salvo que en vez de emplear % dentro de la linea de codigo, usado {}. Vamos con un ejemplo

temple2 = "Mi nombre es {}, mi primer apellido es {} y actualmente tengo {}".format(name, last_name, age)
print(temple2)
#dentro de la funcion print, seria:
print("Mi nombre es {}, mi primer apellido es {} y actualmente tengo {}".format(name, last_name, age))

#Finalmente, el último formato permite incluir las variables dentro del la linea de codigo

temple_3 = f"Mi nombres es {name}. Mi primer apellido es {last_name} y actualmente tengo {age}"
print(temple_3)
#Dentro de la funcion print, este seria la forma correcto de escribir:
print(f"Mi nombres es {name}. Mi primer apellido es {last_name} y actualmente tengo {age}")
