"""
🔴Las matrices son elementos de uso frecuente dentro de ciertos programas. 
En python las matrices son objetos bidimencionales que poseen un ancho (numero de filas)
y un largo (numero de columnas). 
Podemos imaginar las matrices como una tabla de ajedrez a♟️ o una hoja de calendario 📅
esta es una forma sencilla de imaginar la estructura general de una matriz
"""

#En python una manera sencilla de hacer matrices es empleando lista anidadas o listas de listas. Ej

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Esta es una matriz\n: {matrix}") #esta es la manera mas sencilla de imprimir una matriz

"""
Las matrices siguen la dinámica de las litas, es decir:
a. Son ordenadas
b. Se pueden modificar empleando los metodos que hemos aplicado antes
c. Algo importante es que, dentro de la matrices, cada lista que almacena un valor es un elemento. 
Si consultamos el elemento con indice 0, obtendremos la lista que se ubica en dicho valor de indice
Ej
"""
print(f"la primera lista de la matrices es: {matrix[0]}")
print(f"la segunda lista de la matrices es: {matrix[1]}")

#a. Funciones basicas en matrices
"""
Para consultar el tamaño de la matrices podemos usar la funcion len
Para consultar si un elemento forma parte de la matrices usamos la funcion in
"""

print(f"La matriz tiene {len(matrix)} elementos ")
print(f"La lista [4,5,6] forma parte de los elementos de la matriz? {[4,5,6] in matrix}")
print(f"El numero 9 forma parte de la 3 lista de la matriz {9 in matrix[2]}")

"""
🟢
Mini reto: Que resultado arrojaria el siguiente print
print(f"El numero 5 forma parte de la matriz? {5 in matrix}")

"""

#b Acceder a los elementos de una matriz usando indices : Metodo de Indexing en matrices

primera_matriz = [["Laura", "Gabriela", "Alejandra"], [63, 28,40], ["Aries", "Cancer", "Leo"], ["Abril", "Julio", "Agosto"]]
print(f"\nEsta es mi nueva matriz de elementos: {primera_matriz}")

#Vamos a modificar el valor numerico que esta en la posicion 2 de la segunda lista de nuestra matriz

primera_matriz[1][2] = 30 
#el primera valor en [] corresponde a la posicion de la fila y el segundo valor entre [] corresponde a la posicion en la columna 
#el valor que deseamos cambiar se ubica en la fila con la posicion [1] y en la columan [2] 
print(f"\nLa matriz modificada es: {primera_matriz}")

#Veamos otros ejemplos de esto

print("Cual es el nombre y signo zoodiacal de la persona que ocupa la oposicion 1 en la primera lista?")
print(f"El nombre es: {primera_matriz[0][1]} y su signo zoodiacal es: {primera_matriz[2][1]}\n")
print("Cual es el mes de cumpleaños de la persona que ocupa la posicion 2 en la primera lista")
print(f"{primera_matriz[0][2]} cumple en {primera_matriz[3][2]}\n")
print("Cual es la edad de la persona que ocupa la posicion 0 en la primera lista")
print(f"{primera_matriz[0][0]} tiene {primera_matriz[1][0]} años")
