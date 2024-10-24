
"""
Variables:

En el mundo de la programacion, una variable es un espacio en memoria con un nombre o etiqueta  especifico donde almacenamos informacion. 
Las variables suelen interpretartese como cajas 📦 donde guardamos la informacion que puede ser diferentes tipos de datos (letras, numeros, listas, conjuntos... entre otros)
Las variables se declaran empleando el simbolo de la igualdad = y suelen llevar por nombre alguna palabra que relacione la informacion alamacenada en la variable
 
"""

#Declaremos una variable:

name = "Sabrina"
print(name)
age = 20
print(age)

"""
La variable name y age, almacenan el nombre y la edad de una persona. 
Las palabras empleadas estan directamente relacionadas con la informacion guardada en cada una de las variables declaradas.
"""

#🟢Reto 
#Declara una variable que tenga tu nombre, tu apellido, el nombre de un familiar, el nombre de un amigo y la edad de cada uno

"""
Reglas y recomendaciones para nombrar variables en Python 

1. El nombre de una variable debe comenzar con una letra o el simbolo underscore (_).
    a. En python no esta permitido iniciar el nombre de una variable empleando numeros. 
        
2. No se pueden usar caracteres especiales como .,!, @, #, $, %, ^, &, *, (, ), -, +, =, [ ], { }, |, \, :, ;, ', ", <, >, ?, /, ~, `

3. Las variables no pueden contener espacios en blanco ni utilizar palabras reservadas de Python (como print, if, else, while, etc.)
    a. En caso de querer generar un espacio entre las palabras que contituyene el nombre de la variable, se puede emplear el simbolo _
    Ejemplo: my_name_is, my_age_is, entre otros
    
4. Las variables son sensibles a mayúsculas y minúsculas. 
    Ej: my_name = "Gabriel" y My_Name = "Tony". Aunque ambas etiquetas emplean las mismas palabras, el uso de mayusculas en una
    hará que Python interprete que son variables distintas. 

5. Se recomienda usar nombres descriptivos y que representen la información que contienen.
"""
#🟢Reto

"""
Cual de las siguientes variable estaran mal declaradas:
_my_color = "red"
my.color = "red"
mycolor = "red"
MYCOLOR = "red"
myColor = "red"
1mycolor = "red"
my-color = "red"
my color = "red"
my_color = "red"
my1color = "red"
my_color1 = "red"
my_color = red
my@color = "red"
"""

#Formas de declara variables:

"""
Existen dos formas de declara variables. 
1. Declaracion directa: Cada variable declarada empleando una linea de codigo. Ejemplo
    name = "Sabrina"
    age = 20

2. Declaracion en una linea: Las variables y sus valores son escritos en la misma linea de codigo y los argumentos estarán separados por ,
Ejem:
name, age = "Sabrina", 20

Para este caso es muy importante tener en cuenta que el orden en que escribamos las variables, debe coindicir con el orden en que escribamos 
la informacion que deseamos asignarles, sino somos cuidadosos, podriamos asignar de formar erronea un la informacion de una variable.
"""

my_birth, my_favourite_num, my_colour, my_element, is_single = "12 de Agosto", 8, "yellow", "fire", False
print(my_birth, my_favourite_num, my_colour, my_element)

"""
En Python, cuando declaramos variables que son valores constante como el valor de pi o la grave, es una buena prácticar
escribir todo el nombre en letras mayúsculas. Ejemplo
"""
print("Declarando valores constantes\n")
PI = 3.14
print(PI)
GRAVITY = 9.81
print(GRAVITY)


#🟢Reto
#en una sola linea declara 4 variables que contenga el nombre de tu libro, tu estacion favorita, tu comida favorita, un hobbit. 