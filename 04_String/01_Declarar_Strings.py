#🔤Cadenas de texto o strings

"""
Que aprenderas en este parte:
a. Declara un string
b. Uso de las comillas simples, dobles y triples
"""

""" 
Un string contienen información en forma de texto.
En Python, todas las variables que guardan información en formato de texto (letras, palabras o frases), 
deben declararse empleando comillas simple, dobles o triples
"""

#Declaremos un string

#usando comillas simples
saludo = 'Hola, estamos aprendiendo a programar en Python'
print(saludo)

#usando comillas dobles

saludo_dobles = "Python es un buen lenguaje de programacion y fácil del aprender"
print(saludo_dobles)

"""
Aunque se podría decir que el uso de las comillas simples o dobles para guardar los datos de tipo string 
dentro de una variables es irrelevante y su uso depende de quien esté escribiendo el programa. 
🔴Si existen algunas excepciones.
"""

#Usando comillas simples y dobles para guardar los datos de tipo string

saludo_mixto = 'Bienvenido a Python, este es un lenguaje "fácil" si te propones estudiar y practicar con frecuencia'
print(saludo_mixto)

#otra forma de agregar comillas simples y dobles es empleando \'

saludo_mixto2 = 'Bienvenido a Python, este es un lenguaje \"facil\" si te propones estudiar y practicar con frecuencia'
print(saludo_mixto2)

#Las comillas triples se emplean para guardar string de varias lineas

frase = """Este es un string de varias lineas
Puedes usar, las triples comillas cuando quieres declarar 
un variable  con muchas lineas de texto"""
print(frase)

"""
📌Resumen
a. Las comillas simples o dobles se emplean comunmente para declara strings 
que no contienen una gran número de caractéres o sólo comprenden una línea de código

b. Las comillas triples se emplean para guardar string de varias líneas de texto. 
Pueden ser triple comillas simples o dobles. Además las comillas simples o dobles
no son sensibles a los saltos de línea que puede tener un texto de varias líneas
"""

#🔴Los numeros también pueden ser strings 

"""
Todo lo que esté declarado entre comillas simples, dobles o triples 
Python lo entendera como una dato tipo str, incluso si el dato es un número o un espacio en blanco"""

numero_entero = "12345"
print(numero_entero)
numero_decimal = '12.3'
print(numero_decimal)
space = " "
print(space)

#Recuerda que existe la type() con la que podemos corroborar el tipo de dato contenido en una variable. 
#Repasemos esta función con algunos ejercicios

print(type(saludo)) 
print(type(numero_entero))
print(type(numero_decimal))
print(type(space))





