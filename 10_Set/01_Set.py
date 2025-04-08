"""
Un set o conjunto en python, es un tipo de dato similar a la listas o tuplas 
donde se almacena un conjunto de elementos. Algo importante a destacar de los conjuntos es:
1. No se permite elementos duplicados
2. Se pueden modificar 
3. No mantienen un orden 
4. No se pueden emplear los métodos slicing ni indexing para extrar elementos del conjunto

"""

#Declaremos un set 

es_set = {1,2,3,"Alejandra", (1,2,3), 9.8,2}
print(es_set)

"""
Los conjuntos, solo pueden almacenar elementos inmutables. 
Que sucederia si al set declarado agregamos un dato tipo lista❓
"""

"""
Asi como en casos anteriores, podemos transformar un datos y convertirlos en otro tipo
Si quisieramos tranformar una lista o un tupla en un conjunto, solo tendriamos que emplear la funcion 
set
Ej:
"""
lista = ["Alejandra", 12, "Yessica", "11", "Laura", 9]
set_lista = set(lista)
print(f"El conjunto posee los siguientes valores: {set_lista}")

favorite_bookname = "LaCasaDeLosEspiritus"
set_book = set(favorite_bookname)
print(f"El conjunto posee las siguientes letras: {set_book}")

#podemos confirmar si hemos hecho el cambio de forma correcta empleando la funcion type

print(type(set_lista))
print(type(set_book),"\n")

"""
Cuando declaramos conjuntos, tambien podemos emplear las funciones:
len para conocer el tamano del conjunto
in para corroborar si un elemento forma parte del conjunto
Los metodos slicing e indexing para crear subconjuntos o extraer valores especificos ⚠️
"""

#Usando len e in 
print(f"El primer conjunto declarado contiene {len(es_set)} elementos")
print(f"El nombre Alejandra esta dentro del conjunto? {"Alejandra" in es_set}")
print(f"El numero 8 esta dentro del conjunto? {8 in es_set}")

"""
⚠️ Para poder usar los metodos slicing e indexing para extraer algun elemento de uno cojunto,
se debe transformar el conjunto a una lista o una tupla. 
La principal razón por la que no se pueden emplear los métodos indexing y slicing de forma directa
sobre un conjunto es porque los set no mantienen un orden.
"""