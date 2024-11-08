"""
Los valores  contenidos en una listas tambien se pueden sumar o concatenar. Depende de lo que estes realizando en nuestro programa. 
"""

num1 = [23,34,45,56,67,78,89,100]
num2 = [10,21,32,43,54,65,76,87,98]

#Concatenamos los valores de la lista declaradas empleando el operador +

suma = (num1 + num2)
print(type(suma), suma) #en este caso, se generara una sola listas con los valores de la lista num1 y num2

#Vamos a sumar los valores entre si, pero primero comprobemos que la listas tengan la misma cantidad de elementos

print(len(num1))
print(len(num2))
print(f"La lista de elementos num1 es igual a la lista de elementos num2?: {num1 == num2}")


#Aunque las listas no tenga la misma cantidad de elementos, podemos manipular la lista de elementos para sumar los valores de la lista


suma_listas = [num1[i] + num2[i] for i in range(len(num1))]
print(f"La suma de los elementos de num1 y num2 es: {suma_listas}")

"""
En este ejercicio la suma de los elementos corresponde al valor de indice donde se ubica cada numero, es decir, 
los valores ubicados en los valores de indice 0 de cada lista, se sumarán entre sí, de igual forma que pasará con
el resto de los valores númericos.
"""

#Hagamos ejemplos con cadenas de texto

names1 = ["Alejandra", "Laura", "Gabriela"]
names2 = ["Miley", "Vanesa", "Danelys"]

all_names = (names1 + names2)
print(all_names)

#En este caso, no se puede hacer una suma algebraica entre los valores agrupados en ambas listas


#Se puede hacer suma de listas cuando estas contienen datos de diferentes tipos?

mixted = (num1 + names1)
print(f"Esta es una lista con valores mixtos {mixted}")

"""
Se puede concatenar los valores de las listas y generar una sola lista, pero no se puede hacer una suma algebraica 
de listas que con contienen datos de diferentes tipos. Ejm:

mixted2 = [num1[i] + names1[i] for i in range(1,5)]
print(mixted2)
Python indicara que hay un error y los valores no se podrian sumar 
"""

#Se podría convertir una candena de texto en una lista?

frase = "Biblioteca con libros de fantasia"
print(type(frase), f"Esta es mi frase {frase}")
#Usamos la funcion list()
frase_list = list(frase)
print(type(frase_list), f"Hemos convertido la frase en una lista {frase_list}")

"""
Sí, un dato que está almaceano en forma de string, puede tranformaese en una lista usando la funcion list()
"""