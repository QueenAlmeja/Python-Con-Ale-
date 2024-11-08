"""
Sigamos analizando que herramientas o metodos tenemos para modificar una lista

Supongamos que tenemos una lista de elementos y queremos modificar el valor de un
elemento que se encuentra en una posición específica. 

¿Cómo haríamos para saber cual es el valor de indices de un elemento?

🔴El método index() nos devuelve la posicion del elemento
"""

#Declaremos una lista de nombres

names = ["Daniel", "Jose", "Felipe", "Ana", "Paula", "Maria"]

#Buscamos el indice de un nombre usando la funcion .index()

#Podemos declarar una variable para buscar el valor de indices
print("Estamos buscando el valor de indices del nombre Ana con la funcion .index()\n")
indice_num = names.index("Ana")

print(f"Ana tiene el valor de indice: {indice_num}" )

#O hacerlo directamente dentro de la funcion print()
print(f"El nombre de Ana esta en la posicion {names.index("Ana")}\n")

#La funcion index() nos mostrará el valor de indice donde aparece por primera vez el elemento consultado


"""
Para CAMBIAR el valor de un elemento en una posicion especifica se puede emplear

.insert()

Ejm:

Cambie el valor del elemento que está en la posicion 3 por el nombre Gabriela
"""
print("Vamos a cambiar el valor de un elemento en una posicion especifico usando .insert()\n")
names.insert(3, "Gabriela")
print(f"El valor de que está en la posicion 3 de la lista es {names[3]}\n")

#otras formas serian 

print("Cambiamos el valor de un elemtnos usando metodos de indexing[]")
names[3] = "Antonia"
print(f"El valor de que está en la posición 3 de la lista es {names[3]}\n")

"""
🔴Es importante mencionar que la insertar un elemento, estamos agregando un dato en una posicion,
sin emabargo, la información que estaba anteriormente allí no será eliminada, solo cambiará el valor de
su indece 
"""

#Tambien se puede hacer modificacion de varios elementos usando el metodo slicing

print("Tambien podemos cambiar varios elementos usando los valores de indice y el metodo slicing\n")
names[3:5] = ["Pedro", "Maria"]
print(f"Hemos cambiado el valor de los elementos en la posicion 3 y 4 {names}\n")

"""
La lista [] permite que existan elementos repitos. 

Veamos cuantas veces aparece el nombre Maria en la lista names [] empleando 
el metodo .count()
"""
print("En las listas[] pueden haber elementos repetidos y para contarlos usamos la funcion .count()")
print(f"El nombre Maria aparece: {names.count("Maria")} en la lista de nombres\n")

#Debido a que tenemos un elemento repetido vamos a eliminar usando el metodo .remove()

print("Si un elemento esta repetido, lo podemos eliminar usando la funcion .remove()")
names.remove("Maria")
print(f"Estos son los nombre que estan en la lista: {names}\n")


#otra forma podria ser 
"""
print("Tambien podemos emplear la funcion remove en conjunto con los valores de indice donde esta el elemento")
names.remove(names[-1]) #en este caso debemos conocer el valor de indice del elemento que queremos quitar
print(f"Estos son los nombre que estan en la lista: {names}\n")
"""

#Si queremos eliminar el último elemento de nuestra lista usamos la función pop()
print("Si el elemento que deseamos eliminar está en la última posición de nuestra lista, usamos la funcion .pop()")
names.pop()
print(f"La nueva lista de nombres es: {names}\n")

#Sin embargo, la funcion pop() tambien permite eliminar los elementos de una lista si se le da el valor de indice
names.pop(0)
print(f"La nueva lista de nombres es: {names}\n")

"""
Los elemetos de una lista pueden invertir el orden original que se les ha dado u organizarse
por orden alfabetico o valor numerico. Ej.
"""
#En el primer caso usamos la funcion .reverse()

print("Para invertir la posicion de los elementos de una lista, usamos la funcion .reverse()")
names.reverse()
print(f"La lista de nombres en orden inverso es: {names}\n")

#en el segundo caso usamos la funcion .sort()
print("Para organizar los elementos de una lista en orden alfabetico o valor numerico, usamos la funcion .sort()")
names.sort()
print(f"La lista de nombres ordenada alfabeticamente es: {names}\n")

print("Hagamos un ejemplo con valores númericos\n")
number = [1,45,67,23,90,23]
print(f"Esta es nuestra lista numerica: {number}")
number.sort()
print(f"La lista organizada con la funcion .sort() es: {number}") 

"""
🔴Algo muy importantes es que la funcion .sort debe emplear en lista que tengan elementos del mismo tipo
Si la lista tiene diferentes tipos de datos, python arrojara un error

En las lista numericas podemos encontrar el valor maximo y minimo Ej:

"""

print(f"El valor maximo de la lista numerica es: {max(number)}")
print(f"El valor minimo de la lista es: {min(number)}")

"""
En resumen:

Cambiar el valor de uno elemento en una posicion usando insert()
Cambiar el valor de varios elementos empleando los indices y slicing
Saber si hay elementos repetidos count()
Quitar elementos como remove(), pop() o valores de indices
Invertir los valores de una lista con reverse()
Organizar los valores de una lista con sort()\
Conocer el valor de maximo y minimo de una lista
"""

