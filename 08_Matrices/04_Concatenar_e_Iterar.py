"""
Asi como la listas o las cadenas de texto, podemos concatenar matrices para generar una matriz general
a partir de otra matrices
"""

matriz1 = [[0,1,2], [3,4,5]]
matriz2 = [[6,7,8],[9,0,1]]
matriz3 = matriz1 + matriz2
print(matriz3)  


#Iterar en una matriz: uso del ciclo for

"""
Si quisieramos imprir los elementos que se encuentran dentro de cada lista que conforman la matriz, tendriamos que:
"""
for fila in matriz3: #el primer ciclo for recorre cada una de las filas que conforman la matrices general
    for elemento in fila: #el segundo ciclo for recorre cada uno de los elementos que estan dentro de las filas
        print(elemento) #aqui se imprime cada elemento

#supongamos que queremos agregar una condicion al ciclo, ejemplo

for fila in matriz3:
    for elemento in fila:
        if elemento % 2 == 0: #si el elemento es par
            print(f"{elemento} es par")
        else:
            print(f"{elemento} es impar") #el elemento es impar

"""
Supongamos que queremos que el resultado nos muestre todos los numeros pares en una lista, mientras
que los impares en otra lista. Como deberiamos escribir el codigo?
"""
#creamos dos listas vacias antes de declarar el ciclo ya que las usaremos dentro del ciclo
pares = []
impares = []
for fila in matriz3:
    for elemento in fila:
        if elemento % 2 == 0: #si el elemento es par
            pares.append(elemento)
        else: #de no cumplirse la condicion anterior, el numero sera impar
            impares.append(elemento)
            
print(f"Los numeros {pares} son pares")
print(f"Los numeros {impares} son impares")

"""
Pregunta
Por que he puesto los print de cada condicional fuera del ciclo?
"""
"""
Nota final
Con las matrices tambien podemos hacer operaciones, pero este tema es un poco mas complejo 
y lo dejaremos para cursos mas avanzados.
"""