"""
En python existen varias manera de organizar un conjunto de datos o informacion que puede variar y puede
ser empleado de diferentes maneras.

Para organizar un variado grupo de información podemos emplear las listas, tuplas, diccionarios o conjuntos. 
Estos se consideran variables complejos y suelen emplearse para manipular y trabajar mucha información. 
Aunque tienen aspectos similares, existe diferencias que pueden ser determinantes al momento de elegir cual de
estas variables se debería emplear. 

Empecemos por:

🔴 Las listas []

Son secuencias o estructuras de datos que permiten almacenar una coleccion de elementos de cualquier tipo
(str, float, int, bool, listas, dict, tupla). Las listas pueden ir modificandose según la necesidad o requerimientos 
que el programa deba ejecutar

Los elementos almacenados dentro de una listas van entre [] y los argumentos o datos se separan empleando ,

Ej:
"""

person1 = ["Alejandra", 30, True, ("libros", "peliculas", "animales"),{"Pais": "Venezuela"}]
print(f"Esta es la informacion de una persona {person1}")

"""
Usando alguna de la funciones básicas que ya hemos y aplicando en otros elementos de python podemos:

"""
#1. Conocer la cantidad de elementos almacenados en una lista []
print(f"La cantidad de elementos en la lista es {len(person1)}") #funcion len()

#2. Consultar si un elemento forma parte de la lista []

print("Alejandra" in person1) #funcion in

#3. Consultar el tipo de variable en donde se han almacenado todos estos elementos

print(type(person1)) #funcion type()

"""
🔴Una de las cosas más importante de la listas es que MANTIENE UN ORDEN 

¿Porqué el orden sería importante en los casos que usamos la listas [] 
para almacenar la información de algo o alguien?

💡Porque podemos usar los metodos de indexig para acceder a los elementos guardados en una lista

Ejem
"""
print(f"Los hobbies de {person1[0]} son {person1[3]}")
#en este ejemplo estamos accediendo solo a los valores de indice donde hemos escrito el nombre de la persona y la lista de hobbies

#Tambien podemos usar los valores negativos para acceder a los elementos de una lista []

print(f"El ultimo elemento de la lista declarada es: {person1[-1]}")
print(f"La persona está en pareja: {person1[-3]}")

#Si un valor de indice esta fuera de rango de los elementos, python arrojara un error
#print(f"El valor de indice 10 no existe en la lista: {person1[10]}")

#Tambien podemos usar el metodo slicing para extraer un subconjunto de elementos determinados de una lista global []

valores = person1[1:3]
print(f"Estos datos {valores} están entre la posicion 1 y 3 de los elementos de la lista")

