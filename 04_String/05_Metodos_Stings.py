"""
Las cadenas de texto, no solo se pueden manipular empleando los valores de indices donde se ubica cada caracter.
Exiten métodos que nos permiten cambiar ciertos caractéres, dependiendo de la necesidad que tengamos o requeramos efectuar

Ya conocemos algunas de las más elementales como:
a. le() nos permite conocer el tamaño o la cantidad de caracteres
b. index() y find() nos permite conocer el valor o indice de un caracter determinado
c. count() nos ayuda a determinar cuantas veces aparece un caracter dentro del conjunto de elementos almacenados en una variable
d. in nos ayuda a comprobar si un caracter forma parte de una cadena de texto
e. split() nos ayuda a extraer los elementos de una cadena de texto
Sin embargo, existen otros métodos que son importante estudiar
"""
print("Estos son ejercicios usando el método capitalize()\n")

#El método capitalize() cambia el primer caracter de la cadena de texto global por una letra mayúscula. 
#Empleando el metodo capitalize(), solo la primera letra de la cadena de texto sera mayúscula.

oracion = "estamos aprendiendo a programar en Python"
print(oracion.capitalize())

#otra forma sería
primera_letra = oracion.capitalize()
print(primera_letra)

print("\nEsto son ejercicios usando los métodos startswith() y endswith()\n")

#El metodo startswith() y endswith()

oracion = "estamos aprendiendo a programar en Python"
print(f"Estamos usando el metodo startswith para comprobar que la cadena de texto empieza con la la subcadena 'estamos' {oracion.startswith("estamos")}")
print(f"Estamos usando el metodo endswith para comprobar que la cadena de texto finaliza con la la subcadena 'aprendiendo' {oracion.endswith("aprendiendo")}")

"""
Los metodo startswith y endswith comprueban si una cadena de texto global comienza y finaliza con una subcadena especifica.
El output obtenido daran un resultado booelano, True o False
🔴Recuerda que estos métodos son sensible al uso de mayúsculas o minúsculas
"""

print("\nEsto son ejercicios usando los métodos upper() y lower()\n")

#Los métodos upper() y lower() nos permiten colocar todos los elementos de forman parte de una cadena en mayúsculas o minúsculas

pelicula = "Call me by your name"
print(pelicula.upper())
print(pelicula.lower())

print("\nEsto son ejercicios usando los métodos isupper() y islower()\n")
#Los métodos isupper() y islower() comprueban si todos las subcadenas que forman parte del string global comienza con una letra mayúsculas o minúsculas.

serie1 = "Se presume inocente"
serie2 = "when they see us"
print(serie1.isupper())
print(serie2.islower())

print("\nEste es un ejercicio usando el método title()\n")
#El método title() nos permite cambiar por una letra mayúscula cada letra inicial de las subcadenas de texto de la str global

oracion = "estamos aprendiendo a programar en Python"
print(oracion.title())

print("\nEstos son ejercicios usando el método rfind()\n")
#El método de rfind() indica el último valor de indice en que aparece un caracter especifica:
print(oracion.rfind("o"))
print(oracion.rfind("a"))

#Tanto el método find() y rfind() devuelven -1 en el output cuando un caracter no se encuentra dentro del string. Ejemplo

print(oracion.find("x"))
print(oracion.rfind("x"))

print("\nEste es un ejercicio usando el método rindex()\n")

#El método rindex() devuelve en el output el valor de indice mas alto en el que se encuentra un caracter en una cadena de texto.Ejemplo

print(oracion.rindex("t"))

print("\nEste es un ejercicio usando el método swapcase()\n")

#El metodo swapcase() nos modificará las lestras mayúsculas por minúsculas y las minúsculas por mayúsculas

idea = "Esta Es Una Oracion Muy Corta"
print(idea.swapcase())

print("\nEste es un ejercicio usando el método strip()\n")

#El metodo strip() remueve todos los caracteres dados entre parentesis desde el inicio hasta el final de una cadena 
print(idea.strip("ta"))

print("\nEste es un ejercicio usando el método replace()\n")

#El metodo replace() permite modificar una subcadena 

oracion = "estamos aprendiendo a programar en Python"
print(oracion.replace("programar", "desarrollar"))

#📌el uso de la coma para serpar los argumentos es importante en estos casos

print("\nEstos son ejercicios usando el método isalnum()\n")

"""
El metodo isalnum() comprueba si todos los caracteres que forman un string son elementos alfanumericos
en caso de que haya espacios en la cadena, el output dara como resultado un False
"""
oracion = "estamos aprendiendo a programar en Python"
oracion2 = "estamosaprendiendoaprogramarenPython"
print(oracion.isalnum())
print(oracion2.isalnum())

print("\nEstos son ejercicios usando los métodos isalpha() y isdecimal()\n")

"""
Los metodos isalpha() y isdecimal() corroboran si todos los elementos que forman parte de una cadena de caractéres 
son elementos alfabeticos o números enteros. En caso de que haya espacios en la cadena, el output dará como resultado un False
"""

ejemplo1 = "Llevo 3 dias aprendiendo python"
print(ejemplo1.isalpha())
print(ejemplo1.isdecimal())

print("\nEstos son ejercicios usando el método isnumeric()\n")

#El metodo isnumeric() comprueba si los caractéres que forman parte de la cadena corresponde a un valor númerico.

ejemplo2 = "2" #numero dos escrito en forma de string
print(ejemplo2.isnumeric())
ejemplo3 = "3.4"
print(ejemplo3.isnumeric())

"""🟢Reto busca el concepto y uso de los siguientes metodos:
a. isidentifier() 
b. join()
c. expandtabs()
"""
