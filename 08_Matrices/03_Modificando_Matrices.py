"""
A la matrices tambien se les puede extrar los valores maximo, minimo, organizar por orden alfabetico o numerico,
cambiar la lista a una cadena de texto o copiar, empleando la siguiente funciones.
"""
#Supongamos que tenemos la siguiente matriz de elementos:

matrix = [["Laura", "Gabriela", "Alejandra"], [63, 28, 40], [9,13,12], ["Aries", "Cancer", "Leo"], ["Abril", "Julio", "Agosto"]]
print(f"La matriz es: {matrix}")

#extraigamos el valor minimo y maximo
print(f"El valor maximo del elemento en la posicion 1 es: {max(matrix[1])}")
print(f"El valor minimo del elemento en la posicion 1 es: {min(matrix[1])}")

#organizar una sublista con la funcion sort()
print(f"\n La matriz original tiene el siguiente orden de elementos en la posicion 0, 1 y 4: {matrix[0]}, {matrix[1], matrix[4]}")
matrix[0].sort()
matrix[1].sort()
matrix[4].sort()
print(f"Modificando el orden de esta subcadenas con la funcion sort() tenemos: {matrix}")

"""
PD: Si pensaste hacer o hiciste esto:
print(matrix[0].sort())
print(matrix[3].sort())
🔴Es incorrecto y el output de python arrojara None ya que la funcion sort() no devuelve ningun valor,
modifica el elemento, pero no retorna un valor como si ocurre con la funcion min() o max(). Por ello debemos
hacer la modificacion y despues imprimir la matriz o la lista para apreciar la modificacion.
"""

#Ahora, hagamos que todos los elementos de una sublista de la matriz se torne en un solo elemento con la funcion join()

print(f"\nLa matriz original tiene el siguiente orden de elementos en la posicion 0: {matrix[0]}")
matrix[0] = "".join(matrix[0])
print(f"La subcadena modificada con la funcion join() ahora es: {matrix}")

"""
al emplear la funcion join(), los elementos que forman la sublista ubicada en la posicion 0 de la matriz
se han transformado en una cadena de texto
"""
#copiemos una matriz

matrix_copy = matrix.copy()
print(f"\nLa matriz copiada es: {matrix_copy}")

#que pasa si modificamos la matriz original. Ejemplo:

matrix.extend([["Mama", "Hija Menor", "Hija Mayor"], ["Primavera", "Verano", "Otono"]])
print(matrix)
print(matrix_copy)
"""
Como vemos, los elementos agregados se anexaran a la matriz original o la que hemos aplicado el metod extend()
mientras que la copy se mantendra intacta, sin sufrir ninguna modificacion.
"""