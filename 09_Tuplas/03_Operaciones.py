#Operaciones en las tuplas
"""
a. Podemos concatenar los elementos presentes en dos tuplas empleando el simbolo +
Ejm
"""
a = (12, 24, 10, 9, 13)
b = (34, 78, 98, 4)
c = a + b 
print(c) #nueva tupla

"""
b. Empleando el simbolo de multiplicacion *, podemos repetir n veces la cantidad de elementos
presentes en una tupla
Ejm:
"""
d = 3*c
print(d) #todos los elementos que comprenden la tupla c se repetiran 3 veces
print(f"El numero 13 aparece {d.count(13)} veces en la tupla d")
