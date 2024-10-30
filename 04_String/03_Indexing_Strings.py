"""
La manipulación de string, no sólo se limitá a unir o concatenar variables de la manera en que se ha estudiado.
A veces se pueden crear subcadenas de caracteres a partir de la informacion contenida en una variable establecida
A veces se requiere extraer ciertos caracteres o determinar si algún elemento está presente dentro del string 
Para esto, usamos los metodos de indexing y slicing 
"""

"""
🔴Indexing
El indexing es una técnica que nos permite extraer elementos de un string.
Estos elementos se encuentran en una posición numérica específica y para esto empleamos indices
"""
lenguaje = "Python es uno lenguaje de programacion facil de aprender"

print(lenguaje[0]) #el output nos mostrara que valor esta almacenado en la posicion 0 
#En python y otros lenguajes de programacion los valores de indice positivo siempre comienzan a contarse desde 0

"""
Hay dos formas de acceder a los caracteres de una cadena de texto. 
Empleando valores de indice positivos (de izquierda a derecha)
Empleando valores de indice negativo (de derecha a izquierda)

"""
print(lenguaje[-1]) #-1 siempre sera el valor de indice que corresponde al caracter que se ubica en la última posición del string 

"""
Los espacios en blanco también cuenta como parte de los caracteres de una cadena de texto. 
Puede ocurrir que ingresemos el valor de indice de un espacio en blanco y el output no muestre nada
🔴 Recueda que todo lo que escribe entre comillas Python lo interpretara como string, incluso los espacios en blanco
"""

print(lenguaje[6])

#Que pasa si colocamos un valor de indice superior al número de caracteres que conforman el string.

print(lenguaje[56]) #Si el valor de indice es superior al número de caracteres que conforman el string, Python lanzara un error de tipo IndexError

#🟢Reto: Declare una variable que contenga un string y de extraiga el primer caracter y el último caracter usando indices

"""
Supongamos que tenemos una cadena de texto
1. Cómo sabemos cuandos caracteres constituyen dicho string?
2. Cómo comprobariamos que un caracter forma parte de la cadena?
3. Qué métodos o funciones usariamos para conocer la posición o el valor de indice de un caracter especifico?
4. Cómo podriamos saber cuantas veces aparece un caracter en una cadena de texto?
"""
#Para responder algunas de estas preguntas, ya hemos visto algunas funciones elementales, pero hagamos un repaso
#Para saber la cantidad de elementos que forman un string podemos usar la funcion len()

cadena = "Hello, Bienvenido a Python con Ale"
print(len(cadena)) #el out devuelve la cantidad de caracteres que constituyen una variable, incluyendo los espacios en blanco en el caso de los string


#otra forma es usando la declaracion de variable 

side =  len(cadena)
print(side)

#Para comprobar que un caracter forma parte de los elementos almacenados en la variable, usamos la funcion in

print("l" in cadena) #Regresa un valor booleano como resultado para indicar si el elemento forma o no parte de la variable

#otra forma seria 

confir = "B" in cadena
print(confir)

"""
Ten en cuenta que en la programacion debemos ser muy precisos. 
Si el caracter que buscas es una letra mayúscula y lo escribes en minúscula
es probable que el output de como respuesta un False
"""

#Para saber la posicion de un caracter dentro de la cadena de texto, usamos la funcion .index() o .find()

print(cadena.index("H"))

busca1 = cadena.index("h")
print(busca1)

#usando .find()

print(cadena.find("e"))

busca2 = cadena.find("A")
print(busca2)

#Para saber cuantas veces aparece un caracter en una cadena de texto debemos usar la funcion count()

print(cadena.count("A"))

contar = cadena.count("e")
print(contar)

"""
Como hemos visto, los caractéres de una cadena de texto son ordenados y ocupan una posicion determinada.
A los caractéres se puede acceder empleando los metodos de indexing y usando los valores de indice correspondientes
Sin embargo, los elementos que componen la cadena pueden desempaquetarse

#Para desempaquetar los caracteres de una cadena de texto, usamos la funcion.split()
"""

#Usando la declaracion de variables:

word = "Aprendizaje"

#primero determinamos cuando elementos componen la cadena almacenada en la variable word

print(len(word)) #el output indica que la cadena se 11 caracteres

a,b,c,d,e,f,g,h,i,j,k = word
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

#o tambien 
print(a,b,c,d,e,f,g,h,i,j,k)

#Otra forma es usar la funcion split() que se encarga de extrar los elementos de una cadena de texto y los retorna en formato de lista

desempaquetar = word.split()
print(desempaquetar)
