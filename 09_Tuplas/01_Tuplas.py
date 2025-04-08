"""
Las tuplas () son otro de los métodos empleados para agrupar conjuntos de datos.
a. Pueden incluir datos de diferentes tipos, pero a diferencia de las listas, no pueden modificarse una vez creadas.
b. Pueden tener elementos duplicados y son ordenadas
 
"""

tupla = (1,2,3,4,4,[23,45,[ 34,56]])
print(len(tupla)) #usamos len determinar el tamano de mi tupla

""""
🔴
Ya que las tuplas no se pueden modificar como las lista, este tipo de variable no muchas metodos
como los que hemos visto y aplicado a otras variable. Sin embargo, se puede:

1. Consultar si un elemento esta presente en la tupla mediante la funcion in
"""
print(4 in tupla) 
print(23  in tupla) 

"""
2. Si queremos transformar en una variable del tipo str o list en tupla, solo debemos emplear la funcion tuple()
"""


name = "Alejandra"
print(type(name),name)
lista = [45,65,76,89,23,45,23]
print(type(lista),lista)

#Cambiamos las variables:
tuple_name = tuple(name)
print(type(tuple_name),tuple_name)
tuple_lista = tuple(lista)
print(type(tuple_lista),tuple_lista)

#Tambien podemos desempaquetar los valores contenidos en una tupla. Por ejemplo:

tupla_desempaquetada = (1,2,3,4)
x,y,z,w = tupla_desempaquetada
print(x,y,z,w)
#si quisieramos modificar el contenido de una tupla, sin desempaquetar y guardar los elementos en variables individuales, se puede:
lista_desempaquetada = list(tupla_desempaquetada)
lista_desempaquetada[0] = 34 #cambiamos el valor en indix 0
lista_desempaquetada.append(323) #agregamos un valor a la matriz
print(lista_desempaquetada)
#🟢como volverias a convertir lista_desempaquetada en una tupla?

