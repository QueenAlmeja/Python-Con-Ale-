"""
⚙️ Funciones elementales de Python

Python es un lenguaje de programación que nos permite crear funciones para ejecutar bloques de código que efectuan una
función específica. Esto se realiza empleando la palabra reservada def seguida del nombre de la funcion que desarrollaremos.
Pero! antes de llegar a este concepto y como usarlo, vamos a comenzar hablando de la funciones incorporadas que tiene Python 🐍

Las funciones integradas o incorporadas están disponible de manera global dentro del paquete del lenguaje. Estas no requieren de una 
configuración o declaración previa para poder ser empleadas una vez que comenzamos a desarrollar un programa. La más elemental y tal vez
la más conocida es la funcion print()

"""
#El print()

print("Hola, Bienvenidos a Aprende con Ale 💓")
print(234)

"""
La función print es elemental ya que imprime o muestra los elementos o datos contenidos dentro de los parentesis o que forman parte de una variable.

Si embargo, el tipo de dato contenido en una variable o en los parentesis puede variar. En Python existe varios tipos de datos entre los que destacan:

- Cadenas de texto (str)

- Enteros (int)

- Flotantes (float)

- Boolean (bool)

Para saber que tipo de datos conforman una variable o que están dentro de los parentesis de la funcion print, empleamos la funcion type()

"""

#Función type()

print(type("Hola, Bienvenidos a Aprende con Ale 💓"))
print(type(234))

"""
Otra función muy importante y elemental es la funcion in que nos permite consultar si un dato forma parte de los elementos que componen una variable 
o declarados dentro de la funcion print()
"""

#Función in
print("a" in "Hola, Bienvenidos a Aprende con Ale 💓")
print("z" in "Hola, Bienvenidos a Aprende con Ale 💓")

""""
in es una función que regresa un resultado booleano, es decir un True or False.
Si el elemento consultado esta dentro de los elementos que conforman la variable obtendremos un True, en caso de que el elemento no
no forme parte de la variable, el resultado que se obtendra será un False.

Una variable o el mensaje contenido en un print() está compuesto por un número finito de caracteres o elementos. Para saber cuantos elementos forman parte 
de una variable o el mensaje podemos emplear la funcion len()

La función len() regresa un número entero que representa la cantidad de caracteres o elementos que forman parte de una variable o mensaje.
Esta función toma en cuenta los esapcio que separen a las palabras dentro un cadena de texto.
"""
#Función len()

print(len("Hola, Bienvenidos a Aprende con Ale 💓"))


"""
Cuando construimos un programa, gran parte de código lo iremos diseñando en función de lo que esperamos que se ejecute.
En programación a veces nuestro código requerira que un usuario ingrese información, en estos casos, empleamos la funcion input()

La función input recoge el dato ingresado por el usuario, que en principio es una cadena de texto o string. Sin embargo, el código puede solitar la información
de un valor númerico para poder ejecuter el código
"""

#Función input

print(input("Escribe tu nombre: ")) 

#Si necesitaramos que el usuario ingrese un valor númerico podemos interponer la función int() o float() antes de escribir la función input()

print(int(input("Dinos tu edad: ")))


"""
Existen funciones que nos permiten transformar un tipo de dato en otro. Por ejemplos

La funcion str() permite tranformar los datos de una variable en cadena de texto
La funcion int() permite tranformar el valor de una variable en numeros enteros
La funcion float() permite tranformar el valor de una variable en valores decimales 
La funcion bool() permite tranformar el valor de una variable en un booleanos que son estados de verdadero o falso

Pero... 

¿Qué es una variable y cómo podrían emplearse las función antes mencionadas?
Tranquilxs, aquí vamos paso a paso porque programar es divertido y la idea es aprender las bases para avanzar a ejercicios más complejos

Encontras respuestas a estas preguntas y ejemplos de como emplear cada concepto en el material de esta carpeta

Espero que disfrutes aprender conmigo y comparte con quien creas que pueda interesar 💓
"""





