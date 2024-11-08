"""
Los elementos de una lista se pueden copiar. La forma mas sencilla es usando la funcion .copy()

Ej:
"""

names = ["Daniel", "Jose", "Felipe", "Ana", "Paula", "Maria"]

names2 = names.copy()

print(names)
print(names2)

#otra forma seria 

names3 = names
print(names)
print(names3)

"""
Copiar los elementos de una lista nos permite tener un respaldo de la informacion inicial que tenemos al declarar
una lista y hacer modificaciones sobre la copia.

Sin embargo debemos tener cuidado al momento de manipular la lista original y la copia.

"""

print("Voy a agregar un nombre a la lista copiar names2 y names3\n")

#Ejm1
names2.append("Samuel")
print(f"La lista names2 ahora es: {names2}")
print(f"La lista original era: {names}\n")

#Ejm2
names3.append("Daniela")

print(f"La lista name3 ahora es: {names3}")
print(f"La lista original era: {names}")

"""
En el caso del ejemplo 2, la copia que se ha hecho es directamente la lista original y todo lo que 
se modifique en la lista copiada, se verá reflejado en la lista original. 

Una forma de comprobar si la lista son iguales o no es usar los comparadores lógicos o ver si hay más elementos
con la funcion len()
"""
comparando = names == names2 
comparando2 = names == names3

print(f"La primera lista es igual a la segunda {comparando}")
print(f"La primera lista es igual a la tercera {comparando2}")

"""
Otra forma de copiar una lista es usando el metodo de slicing
"""

names4 = names[:]

names4.extend(["Eduardo", "Carolina", "Yessica"])
print(f"La lista names4 tiene los siguientes nombres: {names4}")
print(f"Esta es la lista original {names}")

#usando la funcion len() coprobamos el nuevo numero de elementos que tenemos en la lista
print(len(names))
print(len(names2))
print(len(names3))
print(len(names4))