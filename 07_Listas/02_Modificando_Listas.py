"""
Como ya se ha definido, las listas son variables que almacenan datos de forma ordenada
Sobre estas se pueden usar una serie de funciones que nos permiten:
a. Conocer el valor de un elemento usando indices 
b. Extrar un subconjunto de elementos usando el método de slicing 
c. Modificar el valor de un elemento. 

Esta ultima consideracion es IMPORTANTE ya que nos recuerda que la listas son variables MUTABLES, es decir
que se pueden ir modificando o alterando.
"""
#Una forma sencilla de modificar los elementos declarados en una lista [] es usando los valores de indice. Ejm

person1 = ["Alejandra", 30, True, ("libros", "peliculas", "animales"),{"Pais": "Venezuela"}]
print(f"Esta es la lista original: {person1}\n")
print(f"La edad de {person1[0]} es {person1[1]}\n")

#hacemos una modificacion
person1[1] = 25 #se modficara el valor que esta en la posicion 1 de la lista []
print(f"La edad de {person1[0]} ahora es {person1[1]} años")
print("La lista original se ha modificado")

""""
Ya que las listas son objetos mutables debos tener en cuenta que podemos, agregar, eliminar o modificar los 
elementos que conforman una lista.

Para recordar esto podemos usar el acrónimo CRUD (create, read, update, delete)

C = Crear (Agregar un nuevo elemento)
R = Leer (Obtener un elemento de la lista)
U = Actualizar (Modificar un elemento existente)
D = Eliminar (Remover un elemento de la lista)

Empezemos creando una serie de elementos de diferentes tipos de datos
"""
#Creamos la lista
print("\nVamos a crear una lista con informacion de una cantante\n")
nueva_lista = ["Ariana", False, "Pink", 32, ["singer", "actress", "writter"], ("Travel", "Make cookies", "Watch movies", 6)]

#Leemos la lista
print(nueva_lista)

#vamos a ver cuantos elementos tiene nuestra lista inicial
print(f"Nuestra lista inicial tiene {len(nueva_lista)} elementos")

#Agreguemos un elementos a la lista 

"""
Para agregar elementos a una lista tenemos dos funciones principales
.append() que agrega un solo elemento a la lista original

.extend() que agrega una lista de elementos a la lista original

Ejm
"""
nueva_lista.append("SuperNatural")
print(f"La lista ahora tiene {len(nueva_lista)} elementos")

nueva_lista.extend(["Joven", True, "Eternol Sunshine"])

print(f"La lista ahora tiene {len(nueva_lista)} elementos")

#Eliminamos los elementos de nuestra lista

"""
Para elminar elementos de una lista podemos emplear la funcion
clear() que elimina todos los elementos de la lista o la funcion del
que elimina toda la lista y al hacer print, python arrojará el mensaje is not defined
"""

nueva_lista.clear()
print(f"Nuestra lista esta vacia {nueva_lista}")

del nueva_lista
print(nueva_lista)

"""
En el primer caso se eliminan LOS ELEMENTOS DE LA LISTA
En el segundo se elimina LA LISTA 
"""

