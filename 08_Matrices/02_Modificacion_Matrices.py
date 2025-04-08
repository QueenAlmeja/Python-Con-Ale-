"""
A las matrices tambien podemos agregar o eleminiar elementos usando las funciones correspondientes
Las matrices siguen los métodos que se usan con las listas[]
"""

#Parte I : Modificando las matrices
#Busquemos la posicion de un elemento en una matriz usando index

names = [["Ana", "Alejandra", "Adriana"], 
         ["Elena", "Enriqueta", "Esmeralda"], 
         ["Isabel", "Ilenia", "Ingrit"]]

print(f"Esta es la matriz de nombres {names}")
print(len(names))

"""
Con la funcion len, sabemos que nuestra matriz de nombre esta compuesta de 3 elementos
Es decir que hay una lista en la posicion 0,1 y 2 respectivamente
"""

#Busquemos la posicion del nombre Ana
ana_positions = names[0].index("Ana")
print(f"\nLa posicion de 'Ana' en la matriz es: {ana_positions}\n")


#Confirmemos si un elemento forma parte de la matriz
print("Antonia" in names[0])
print("Alexander" in names[1])
print("Abigail" in names[2])

#Como ningun de los elementos anteriores estan en la matriz agreguemos esto a la matriz

#Usando append() y extend() podemos agregar una o varias listas a la matriz

names.append(["Antonia", "Alexander", "Abigail"]) #se agregara al final de la matriz declarada
print(f"\nLa matriz tiene una nueva fila: {names}\n")

names.extend([["Antonella", "Claudia", "Estefan"], ["Christopher", "Taylor", "Selena"]]) #se agregaran al final de la matriz declarada
print(f"La matriz tiene mas filas {names}\n")


#Pero si queremos agregar elementos a las lista ya existentes, esta seria la manera 
names[0].append("Diego")
names[1].append("Victoria")
names[2].append("Agustina")

print(f"\nLa matriz modificada es: {names}\n")


#Insertemos element usando la funcion insert()

names.insert(0, ["Felipe", "Carlos", "Joanlys"]) #la lista que ocupara la posicion de indice 0 ahora sera esta
print(f"La matriz tiene una nueva lista en la posicion 0 {names}")
#en este caso estamos agregando toda una nueva lista a la posicion 0 de la matriz antes declarada
#Tambien podriamos hacer esto
names[0].insert(1, "Canela")
print(f"En la primera lista de la matriz se a insertado un nombre en la posicion 1 {names}")

#Si queremos modificar el valor de un elemento en una lista podemos emplear indexing[]

names[0] = ["Adriano", "Enrique", "Mereyda"]
print(f"\nHemos modificado los nombre de la lista de la posicion 0 de la matriz {names}")
#Usando slicing para modificar valor

names[0:2] = [["Jose", "Andres", "Daniel"],["Pedro", "Pablo", "Alfredo"]]
print(f"Se han cambiado los nombres de las filas ubicados en la posicion 0 y 1 de la matriz original {names}")

#Usemos el slicing para extraer listas de listas

mini_matriz = names[0:2]
print(f"\nEsta es la submatriz de la matriz original {mini_matriz}\n")

#Tambien podemos contar cuantas veces aparece un elemento dentro de una matriz

print(f"\nEl nombre 'Enrique' aparece {names[1].count("Enrique")} veces")
print(f"El nombre 'Andres' aparece {names[0].count("Andres")} veces\n")

#Tambien podemos remover un elemento de la matriz usando remove()
print(f"Se ha removido el nombre Isabel de la lista en la posicion 3 de matriz {names[3].remove("Isabel")}")
print(f"La nueva lista es: {names}")

#Asi como con la funcion insert(), la funcion remove() puede modificar el numero de columnas
#Podemos eliminar todo los elementos de una posicion con al funcion pop 

names.pop(1)
print(f"Se ha removido la lista de la posicion 1 de la matriz {names}" )
#Tambien podemos eliminar los elementos de una lista que compone la matriz

names[0].pop(0)
print(f"Se ha removido el nombre Jose de la lista en la posicion 0 de la matriz {names}" )