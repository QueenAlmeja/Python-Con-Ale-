"""
No toda la informacion alamecenada en las variables se emplean de la misma forma. Un nombre, frase o palabra 
no se interpreta de la misma forma que un número.

En python los tipos de datos almacenados en las variables se pueden clasificar en dos tipos:
a. Variables con datos simples
b. Variables con datos complejos
"""

#Las variables con datos simples son:

#Las cadenas de texto o string. 
#Toda la informacion almacenada en formato de texto y declarado entre comillas simples, dobles o triples sera un String
print("Esto es una cadena de texto o string\n")
name = 'Laura'
print("The name is", name)
last_name = "Moron"
print("The last name is", last_name)
sentence = "Hoy es un buen dia para aprender algo nuevo"
print("This is a sentence", sentence)
letra = 'g'
print(letra)

lyrics_song = """They can't love me like you do
I triend to find somebody new
Baby, they ain't got a clue
"""
print("This is the lyrics of a band\n", lyrics_song)

#No te precopes, que mas adelante te enseñaré como y cuando usar comillas simples, dobles o triples. Vamos paso a paso.

#Los datos numericos: int, float, complex
print("Estos son datos numericos")

age = 90
print("Age: ", age)
GRAVITY = 9.8
print("The value of gravity is:", GRAVITY)
complex = 3 + 1j
print("This is a complex number: ", complex)

"""
Los datos de tipo int comprenden números enteros que van desde los negativos a los positivos ('5, 0, 5)
Los datos de tipo float comprenden nnúmeros con apreciacion decimal como la constante de la gravedad. En python todos los numeros decimales se escriben empleando el .
Los datos de tipo complex comprenden números que forman parte de analisis con álgebra y para este curso basico no los vamos a emplear demasiado, pero si es importante 
mencionar que existen
"""

#Los datos booleanos corresponde a estados de verdadero o falso y se designan empleado las palabaras True o False

is_frendly = True
print("La variable 'is_frendly' contiene un dato tipo boolean: ", is_frendly)
is_single = False
print("La variable 'is_single' contiene un dato tipo boolean: ", is_single)


"""
La sintaxis en Python es increiblemente importante, cuando declaramos una variable con un dato tipo boolean, la palabra False o True 
debe empezar con letra mayúscula sino, python lo tomara como un error y no podra ejecutar el codigo. 
ej: 
is_girl = false
No es una forma correcta de declara la variable que contiene un valor booleano
"""

#Variables con datos complejos: listas, tuplas, diccionarios, conjuntos
"""
Las variables complejas de Python permiten almacenar elementos de diversos tipos. Cada una de estas variables tiene caracteristicas bien definidas.
Su uso, puede variar y muchas veces son aplicadas dependiendo de la necesidad que requiera el programa. 

En este parte, nos limitares a explicarte como declarar estas variables y la estructura basica de los datos que pueden almacenar, 
más adelante aprenderas a usarlas mucho mejor.
a. Listas = []
b. Matrices = [[]]
c. Tuplas = ()
d. Diccioanrios = {clave:valor}
e. 	Set o Conjuntos = {}
"""

print("Estos son variables con datos complejos")
lista = ["Alejandra", True, 23, ["Elementos de quimica", "Reglas de Matematica"], 34.6, "Venezuela"]
print("Esto es una lista", lista)
matriz = [["Alejandra", "Gabriela", "Laura"], [12,13,9], [34.5, 23.5, 44.7]]
print("Esto es una matriz", matriz)
tupla = ("nombre", 23, ["cosa 1", "cosa2"])
print("Esto es una tupla", tupla)
diccionario = {"Alejandra":30, "Gabriela":28, "Laura":63, "Patas":11}
print("Esto es un diccionario", diccionario)
set = {"Alejandra", 34, True, 45.6}
print("Esto es un set", set)