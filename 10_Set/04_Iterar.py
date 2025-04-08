"""
Asi como la lista, sobre los set se puede realizar iteraciones. Veamos algunos ejemplos
"""

#1. Imprimimos a cada uno de los elements de un set
a = {1,2,3,4}

for i in a:
    print(i)
    

for i in a:
    if i % 2 == 0:
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar")

#creemos un conjunto donde se almacene el valor cuadrado de los elementos del conjunto a

cuadrados = [i**2 for i in a]
print(f"El nuevo conjunto de elementos es : {set(cuadrados)}")


b = {"Alejandra", "Manuel", "Felipe", "Juan"}

for i in b:
    if len(i) > 6:
        print(f"Estos nombres tiene mas de 6 palabras {i}")
    elif len(i) < 6:
        print(f"Estos nombres tienen menos de 6 palabras {i}")
    else:
        print(f"Estos nombres tienen 6 palabras {i}")
        

"""
Esta es la forma mas sencilla de realizar una iteracion empleando conjunto
Ten cuidado de la forma en que escribes el codigo porque recuerda que los simbolos {}
tambien se emplea para definir diccionarios y esto puede o podria generar algun error 
en el programa. 
"""