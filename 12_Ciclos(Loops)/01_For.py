"""
El ciclo for en python se emplea para iterar sobre una conjunto de elementos. Dichos elementos pueden 
ser cadenas de texto, listas, tuplas, diccionarios, entre otros.
El numero de iteraciones del ciclo for esta definido Ej:
"""

lista = [1,2,3,4,5]

for i in lista:
    print(i)
    
for i in range(len(lista)):
    print(i)
"""
Aunque los resultados de cada print son ligeramente diferentes, 
el numero de iteraciones esta limitado por la cantidad de elementos que conforman la lista
o el rango en que se ubican los valores de lista

La estructura general de un ciclo for es

for variable_iterable in secuencia:
    #bloque de codigo a ejecutar sobre cada elemento contenido en la secuencia
"""
palabra = "supercalifragilisticoespialidoso"

for i in palabra:
    print(i)
    
diccionario = {"Ana":"Genetica", "Hector":"Bioquimica", "Samuel":"Estadistica", "Mariana":"Zoologia"}
#generemos un ciclo for que no mueste el nombre del profesor y la materia que da en la universidad


for i, j in diccionario.items():
    print(f"El docente {i}, da la materia {j}")

"""
Con el ciclo for tambien podemos combinar funciones que ya hemos estudiando anteriormente
como los condicionales y los operadores logicos o comparativos. Ej
"""

numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

suma_cuadrados = 0

for numero in numeros:
    cuadrado = numero**2
    suma_cuadrados += cuadrado
print(f"La suma de los cuadrados es {suma_cuadrados}")

#otro ejemplo
pares_mayores = []
impares_menores = []
for numero in numeros:
    if numero % 2 == 0 and numero > 10:
        pares_mayores.append(numero)    
    elif numero % 2 != 0 and numero < 10:
        impares_menores.append(numero)
print(f"Estos son numeros pares mayores a 10 {pares_mayores}")
print(f"Estos son numeros impares menores a 10 {impares_menores}")



"""
🛑
Como hemos visto, for un ciclo que se sirve para iterar sobre los elementos de una variable, pero
Que es iterar y como sabes como una variable es iterable?
Iterar es repetir un numero de veces determinado un proceso
Un elemento iterable es o son elementos indexados, los elementos que lo componen pueden tener un indice

Con el ciclo for se pueden realizar bloques de codigo que nos permitan repetir una tarea un numero 
determinado de veces, es bastante util para reducir las lineas de codigo y se puede usar o combinar con
otras funciones. 
"""

