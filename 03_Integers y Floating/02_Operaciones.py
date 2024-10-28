"""
🧮
Una de las cosas mas comunes en las que se emplean variables o datos con valores númericos son las operaciones aritméticas 
 
Sí,  en la programación solemos emplear las matemáticas, pero tranquilo que empezaremos por las operaciones básicas para explicarles
el uso de los operadores mas empleados en Python 

🌟Operadores Básicos 

suma +
resta -
multiplicacion *
division /

Veamos esto con ejemplos
"""

num1 = 2
print(num1)
num2 = 7
print(num2)
#suma
print("\nEsto es el resultado de la suma de los valores contenidos en las variables num1 y num2\n")
suma = num1 + num2
print(suma)

#otra forma de escribir el resultado seria:
print(num1 + num2) #no es necesario crear una variable que almacene el resultado de la operacion, pero puede ser de utilidad

#resta
print("\nEsto es el resultado de la resta de los valores contenidos en las variables num1 y num2\n")
resta = num1 - num2
print(resta)
print(num1 - num2)

#multiplicacion
print("\nEsto es el resultado de la multiplicacion de los valores contenidos en las variables num1 y num2\n")
multiplicacion = num1 * num2
print(multiplicacion)
print(num1 * num2)

#division
print("\nEsto es el resultado de la division de los valores contenidos en las variables num1 y num2\n")
division = num1 / num2
print(division)
print(num1 / num2)

print("\nOtros operadores \n")
"""
Como te has dado cuenta, puedes crear variables para guardar la operacion que ejecutas entre variables que contienen datos numericos o 
puedes escribir la operacion que deseas ejectar entre las variables declaradas entre los parentesis de la funcion print()

Ademas de los operadores basicos, tenemos:

Operaciones con exponente donde se emplea **
Operaciones de modulo %
Operaciones de division con valor entero o floor division //

Vamos con ejemplos
"""
print("\nEsto es el resultado de valor contenido en la variable num2 elevado a la 3\n")
exponencial = num2 ** 3
print(exponencial)

print("\nResultado de modulo entre los valores de variables num2 y num1 \n")
modulo = num2 % num1
print(modulo)

print("\nResultado de division con valor entero entre los valores de variables num2 y num1 \n")
floor_division = num2 // num1
print(floor_division)

"""
Como interpretar el % y el //

Para esta parte te recomiendo que hagas las operaciones en papel y así podras profundizar en estos dos conceptos y el uso de estos operadores 

El resulatdo obtenido con el operador del modulo % representa el valor numerico que queda al dividir 7 entre 2, mientras que el valor obtenido de la 
division con valor entero es el cociente de una división.

La operaciones que se efectuen con estos operadores siempre arrojaran un numero entero, aqui no se obtendra una presicion decimal del resultado 

Por ejemplo, el operador % nos permitira realizar un programa que nos indique si un número es par o impar

"""

#🟢 Reto : Escribe variables para almacenar los siguientes numeros:

"""

234
5468 
786
924
98.45
7261.9
463
195
34.6
32

Y realiza operaciones basicas con estos numeros utilizando los operadores que vimos anteriormente

PARTE 2

Cuál es el valor del modulo y el cociente de dividir 924 entre 5?
Cuál es el valor del modulo y el cociente de dividir 786 entre 32?
Cuál es el valor de 56 elevado a la 5?
Cuál es el valor 5468 elevado a la 2?

PARTE 3

Calcular el area y la circunferencia de un circulo empleando las ecuaciones del area ( area = pi x r x r) y circunferencia (c = 2 x pi x r)

PARTE 4

a. Cual seria el precioso de un televisor que tiene un costo inicial de 345 dolares, pero has obtenido una gift card que te permite aplicar un descuesto del 35%
b. Tienes 436 naranjas cosechas en tu patio, pero debido a una plaga de hongos has perdido el 43% de tus naranjas. Cuantas naranjas te quedan?
"""