"""
Los diccionarios son tipo de dato que al igual que las listas, los set o tuplas, se puede almacenar
un conjunto de informacion, sin embargo, la sintaxis de los diccionarios opera bajo la modalidad de
clave-valor, donde cada elemento o caracter corresponde a un valor determinado. Ejm:
"""
usuarios = {"Alejandra": "Anime", "Antonela": "Romance", "Patricia": "Sci-Fic"}
print(f"Esto es un diccionario en python {usuarios}")

#diccionario_python = {"clave":"valor"}

"""
Los diccionarios pueden contener datos de distintos tipos, incluso podemos tener diccionarios dentro de
un diccionario. Ejem:
"""
animales = {"Mamiferos":["Leon", "Oso", "Caballo", "Perro"], "Reptiles":("Serpientes", "Caimanes", "Dragones"),
            "Artropodos":{"Insectos":["Mariposas", "Moscas", "Cucarachas"], "Aracnidos":["Aranas", "Garrapatas", "Escorpiones"]}}
print(f"Este es un diccionario con datos de diferentes tipos:{animales}")

"""
Con los diccionarios tambien podemos emplear algunas de las funciones basicas de python. Ej:
"""
print(f"La variable 'usuarios' es del tipo {type(usuarios)}")
print(f"El diccionario tiene un tamano de: {len(usuarios)}")
print(f"Alejandra" in usuarios)
print(list(animales)) #solo nos regresara en forma de lista los valores de las keys

"""
Breve resumen:
Los diccionarios son estructuras mutables
Se puede acceder a los elementos de un diccionario mediante la clave
Son estructura que pueden ser anidadas
Las claves (keys) de un diccionario deben ser del tipo inmutable, mientras que los valores (values) pueden dar
datos mutables 
La sintaxis de las claves es importante ya que se podria reescribir el valor de una key
Desde la version python 3.7 los diccionarios son estructuras que mantienen el orden
"""