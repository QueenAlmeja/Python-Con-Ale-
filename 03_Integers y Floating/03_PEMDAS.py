"""
El método PEMDAS es una manera de recordar el orden en que debemos resolver una operación matemática 
cuando tenemos varios operadores aritméticos en la ecuación

Es muy común encontrar ecuaciones donde hay sumas, multiplicaciones y hasta divisiones, sin embargo, la 
manera en que vamos resolviendo estas operadores es determinante al momento de obtener el valor final

Ejemplo: Supongamos que tenemos la siguiente ecuacion

x = (56 + 34 * (34 * 2) - 45 * 2 + 2**67)

Cual seria el orden correcto para resolver dicha ecuación y conocer el valor de x?

Empleando el método PEMDAS podremos saber el orden en que debemos ir resolviendo 
las operaciones para obtener el resultado.

La secuencia de los pasos es la siguiente:

a. P = Resolver los valores que estan entre parentesis ()
b. E = Resolver los valores o numeros exponenciales **
c. M = Resolver la multiplicacion *
d. D = Resolver la division /
e. A = Resolver la adicion o suma +
f. S = Resolver la sustracion o resta -
"""
#Hgamos el ejercicio en empleando Python 🐍

x = (56 + 34 * (34 * 2) - 45 * 2 + 2**67)
print(x)

#Recuerda que tambien podriamos hacerlos de la siguiente manera:

print(56 + 34 * (34 * 2) - 45 * 2 + 2**67)

#Empleando variables 

a = 56 
b = 34
c = 2
d = 45
e = 67

y = a + b * (b * c) - d * c + c**e
print(y)

"""Te dejo algunos ejercicios para que resuelvas usando el este método, pero primero! 
Intenta hacerlo a mano y compara tus resultados

Ejercicio 1: Resolver (78 + 32 * (12 * 3) - 48 * 3 + 2**89)
Ejercicio 2 : Resolver (456 + 23456) * (8 ** 45) + 7564 / 897 - 234 

🟢Reto 
¿Como sacarias la raíz cuadrada de un numero sin emplear alguna función especial de python?
"""

