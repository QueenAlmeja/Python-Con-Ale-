"""
Los operadores aritméicos y de comparación pueden emplearse para asignar valores a variables.
Vamos con ejemplos para que se entienda mejor:

"""
x = 10
x -= 2
print(x)  

"""
💡
Esto es un buen ejemplo para recordar la sintaxis de Python y la manera en que el código se va leyendo
el valor de la variable x en principio es 10, pero al hacer la asignacion de x  -= 2, al valor original
se le restan 2 y el nuevo valor de x y el que python nos mostrará sera 8. Igual pasa con lo casos que vienen
"""

y = 15
y += 4
print(y) 

w = 34
w *= 2
print(w) 

a = 24
a /= 2
print(a)

b = 45
b //= 5
print(b) 

c = 76
c %= 3
print(c) 

d = 4
d **= 7
print(d) 


e = 78
e <<= 4
print(e) 

f = 25
f >>= 4
print(f) 

g = 99
g &= 3
print(g) 
"""
Estos operadores permiten realizar operaciones matemáticas y asignar
los resultados en una sola línea, simplificando el código.

Para fijar mejor estos conocimeintos te recomiendo que hagas una tabla con el significado y uso de
cada uno de estos operadores. Te ayudara a recordarlos y podras repasarlos
"""