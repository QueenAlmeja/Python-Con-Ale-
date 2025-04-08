"""
A los conjuntos se le pueden aplicar una serie de funciones que nos permiten 
Unir elementos de varios conjunto para crear uno solo
Interserta dos conjuntos para extraer los elementos comunes
Entre otros, aqui veremos unos ejemplos
"""

#1 Union de varios conjuntos a.union(b)

a = {1,2,3,4}
b = {3,4,5,6}
print(f"El conjunto a tiene lo siguientes elementos {a}")
print(f"El conjunto a tiene lo siguientes elementos {b}")
print(f"La union del conjunto a y b es {a.union(b)}")

"""
Al emplear la funcion union() se concatenan los elementos de dos conjuntos, el set resultante 
generara un unico conjunto con elementos de cada set, excluyendo los elementos que se repiten o son
similares en el conjunto a y en el conjunto b
Tambien se pueden emplear la el simbolo | para unir conjuntos
"""
c = a | b 
print(c)

#2 Interseccion de conjuntos empleando la funcion a.intersection(b) o el simbolo &
print(f"La interseccion de los dos conjunto es: {a.intersection(b)}")
d = a & b
print(d)
"""
Al realizar un interseccion, el set resultante mostrara los elementos en comun que se encuentran 
en ambos conjuntos
"""

#3 Diferencia entre conjuntos a.difference(b) o el simbolo -
print(f"La diferencia entre los conjuntos a y b es: {a.difference(b)}")
e = a - b
print(e)
"""
La diferenciacion siempre regresara los elementos unicos del primer conjunto o aquellos 
elementos que no se repiten en el otro conjunto
"""

#4 Simetria de conjuntos empleando a.symmetric_difference(b) o ^
print(f"El conjunto resultante a aplicar la funcion de simetria es: {a.symmetric_difference(b)}")
f = a ^ b
print(f)
"""
Esta funcion retornara un conjunto donde se almacenaran los valores que se repiten una sola vez
en cada conjunto
"""

#5 Determinar un subconjunto con la funcion a.issubset(b) o el operador <=
print(f"hay un subconjunto contenido es a o b: {a.issubset(b)}")


"""
Para determinar si todos los elementos que conforman un conjunto se encuentran en el otro
podemos emplear la funcion .issubset(). El output arrojara un valor booleano
"""

#6 Determinar un superconjunto con la funcion a.issuperset(b) o el operador =>
print(f"Hay un superconjunto contenido en a o b: {a.issuperset(b)}")

"""
Al igual que la funcion  issubset, cuando queremos verificar si un conjunto es 
un superconjunto, obtendremos un valor booleamos en el output.
Un superconjunto debe contener todos los elementos del set con el que se esta comparando
"""

#7 Determinar si dos conjuntos son disjuntos con la funcion a.isdisjoint(b)
print(f"Los conjuntos a y b son disjuntos: {a.isdisjoint(b)}")
"""
Este metodos nos permite corroborar si todos los elementos que conforman dos conjuntos o mas 
son diferentes. Asi como las dos funciones anteriores, este metodo retorna un valor booleano en
el output 
"""

"""
Investigar las siguientes funciones:
a.intersection_update(b)
a.difference_update(b)
a.symmetric_difference_update(b)
"""
