"""
Iterar un objeto en Python es recorrer uno a uno los elementos que componen un objeto.
Para iterar un objeto en Python necesitamos usar el bucle for
Aunque no hemos visto el bucle for, vamos a ver los ejemplos para comprender el concepto de iterar
"""

#Creemos una lista de numeros 

numer_list = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]


#Iteramos sobre la lista que hemos creado
print("Primer ejemplo de iteracion\n")
for i in numer_list: #por cada elemento (i) en la lista declarada
    if i % 2 == 0: #si la division del elemento que esta recorriendo es 0
        print(f"El número {i} es par") #imprima un mensaje con el numero par
    elif i % 2 != 0: # si la division del elemento que esta recorriendo no es 0
        print(f"El numero {i} es impar")


#Otro ejemplo
print("Segundo ejemplo de iteracion\n")
for i in range (1,11): # declaro un rango de valores en el que se va iterar 
    numer_list.append(i * 2) #a la lista creada voy a agregar los valores de los elementos multiplicados por 2
print(numer_list) #imprimo la lista

#hagamos la lista con cadenas de texto

print("Ejemplo usando una lista con strings\n")
names = ["Daniel", "Jose", "Felipe", "Ana", "Paula", "Maria"]

for i in names:
    print(f"El nombre es {i}") #imprimo todos los valores contenidos en la lista names


for i in names:
    if "a" in i: #creamos un condicionales para evaluar los elementos que tiene la letra a minusculas
        print(f"El nombre {i} contiene la letra 'a'") #imprimimos los nombre que tiene la a minusculas
    #podemos ponerlo un poquito mas complicado para divertinos
    elif "a" in i and "e" in i:
        print(f"Estos nombres {i} contiene la letra 'a' y 'e'\n")

"""
List comprehension
El método list comprehension nos permite escribir en una linea de código lo que se ha declarado
en varias lineas. Esto nos permite ahorrar o mejorar la estrucuta de nuestro código
"""

print("Ejemplos usando list comprehension\n")
print("Ejemplo con numeros:")
numer_list = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
print(f"Mi lista original {numer_list}")
new_list = [i for i in numer_list if i % 2 == 0]
print(f"Esta es a lista de los numeros pares de la lista original {new_list}\n")
new_list2 = [i for i in numer_list if i % 2 != 0]
print(f"Esta es a lista de los numeros impares de la lista original {new_list2}\n")

print("Ejemplo con strings")
names = ["Daniel", "Jose", "Felipe", "Ana", "Paula", "Maria"]
print(f"Esta es mi lista de nombres original {new_list}\n")
new_list_names = [i for i in names if "a" in i and "e" in i]
print(f"Esta es la nueva lista: {new_list_names}")

"""
Creando una lista [] vacia
"""

print("Ejemplos con listas vacias\n")
empty_list = []
print(f"Esta es una lista vacia {empty_list}")

for i in range(1, 11):
    if i % 2 == 0 and i > 4 :
        empty_list.extend([i])
    print(f"Esta es la nueva lista {empty_list}")
    
#otra forma seria

empty_list = [i for i in range(1,15) if i % 3 == 0 and i > 2]
print(f"Esta es la nueva lista {empty_list} y el valor maximo de la lista es {max(empty_list)}")

