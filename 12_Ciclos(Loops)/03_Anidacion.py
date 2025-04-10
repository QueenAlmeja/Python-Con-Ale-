"""
Asi como en las listas o diccionarios, en los ciclos for tambien podemos encontrar anidaciones
Un ciclo for dentro de un ciclo for. La estructura del ciclo interno, sigue la misma estructura 
que hemos explicado. En general, un ciclo for general, se podria ver de la siguiente manera:

for variable_iterable in secuencia:
    for variable_iterable in secuencia:
En estos casos es muy importante respetar la tabulacion.
Ejemplo:
"""
animal = ["Leon", "Serpiente", "Tiburo", "Guacamayo"]
grupo = ["Mamifero", "Reptil", "Pez", "Ave"]

for i in animal:
    for j in grupo:
        print(f"el animal {i} es del grupo de los {j}")
"""
Si ejecutas este codigo notaras algo raro, pero tranquilo, esto por ahora es solo un ejemplo. 
Pronto lo mejoramos.
"""
#un ejemplo muy comun para entender como se emplea un ciclo for anidado es imprimir una matriz. Ej:

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matriz: #en este caso i seran las filas de la matriz
    for j in i: #j representa cada elemento contenido en una fila (i)
        print(j, end=" ")
    print()

#A los ciclos anidados tambien se les puede aplicar el uso de condicionales. Ej

for i in matriz:
    for j in i:
        if j % 2 == 0:
            print(f"{j} este es un numero par")
        else:
            print(f"{j} es impar")   

#podriamos incluso crear tablas de multiplicar usando ciclos for anidados

for i in range(0,11):
    for j in range(0,11):
        print(f"{i} x {j} = {i * j}")
    print()


"""
👩🏽‍💻Fixing a problem:
Ok, el problema con la lista de animales y grupos es que cuando hacemos la iteracion sobre cada variable,
el bucle for asoacia cada animal con cada grupo. Para mejorar esto podemos ajustar la iteracion y corregir
el error usando la funcion zip(). Let's do it
"""
for i, j in zip(animal, grupo):
    print(f"El animal {i} es del grupo de los {j}")
    
"""
Que hace la funcion zip()?
La funcion zip() de python nos permite agrupar pares ordenados de elementos iterables.

🔴En este caso, el ciclo anidado se puede simplificar, pero existe una forma de reducir la lineas
de codigo de un ciclo for a una sola.


"""