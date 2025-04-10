"""
El ciclo while nos permite ejecutar un bloque de codigo mientras la condicion sea verdadera
La estructura o sintaxis del ciclo while es:

while condicion:
    #bloque de codigo a ejecutar 

Cuando declaramos un ciclo while porque podemos generar un ciclo infinito. Ej:
while True:
    print("Bucle infinito")
🔴 En caso de que generes por error un ciclo while, presiona Ctrl + C
"""

x = 0

while x <= 5: #mientras x sea menor o igual a 5
    print(x)
    x += 1 #incremento en uno el valor de la variable para evitar un bucle infinito
    

'''
Tambien podemos agregar condiconales al ciclo while para ejecutar una funcion de forma
repetida hasta que la condicion sea verdadera
'''
num_fav = 12
num_guess = " "

while num_fav != num_guess:
    num_guess = int(input("Introduce un numero para adivinar: "))
print("Numero correcto, Has adivinado")

#🟡hagamoslo mas complejo usando if, elif
print("\nNuevo ejercicio")
num_guess = " "  #volvemos a invocar la variable para reiniciar el bucle while y
while num_fav != num_guess:
    num_guess = int(input("Introduce un numero para adivinar: "))
    
    if num_guess > num_fav:
        print("El numero es mayor al numero secreto")
    elif num_guess < num_fav:
        print("El numero es menor al numero secreto")
        
print("Numero correcto, Has adivinado")
"""
Aunque algunos en este punto se podran preguntar porque la variable num_guess es una string vacio.
Lo que estamos haciendo en este punto es hacer que la varible este vacia y la convertimos en un int
cuando la llamamos dentro del bucle para pedirle al user que ingrese un num
"""
#🟡usando else con while 

num = 10 #creamos una variable que contendra la condicion 
while num > 5: #declaramos el ciclo. mientra el num sea mayor a 5 este sera impreso por print 
    num -= 1 #se le ira restando -1 a cada ciclo 
    print(num)
else:
    print("El ciclo a terminado") #finalmente el ciclo terminara 
#🟢MiniReto: que pasaria si el num = 5 y el ciclo empezar en 5
 
num = 20
pares = []
impares = []
while num > 10:
    num -= 1
    if num % 2 == 0:
        pares.append(num)  
    elif num % 2 != 0:
        impares.append(num)
print(f"Son pares {pares}")
print(f"Son impares {impares}")

#🟡usando el break y el continue con while

print("\nEjemplo con break")
num = 20
while num > 10:
    num -= 1
    if num < 15:
        break
    print(num)

print("\nEjemplo con continue")
num = 20
while num > 10:
    num -= 1
    if num % 2 == 0:
        continue
    print(num)
"""
el ciclo break y continue tienen el mismo proposito dentro del ciclo while
el break, finaliza el ciclo bajo una condicion dada, mientras que continue
salta a la condicion que si cumple con lo establecido con el ciclo
"""

#Dentro de un ciclo while, tambien podemos usar dos variable. Uno de los ejemplos mas conocidos en la sucesion de fibonacci

a,b = 0,1 #recuerda que podemos declara varias funciones en una sola linea
while b < 25: 
    print(b)
    a, b = b, a+b
#🟡un ciclo while tambien puede tener ciclos anidados. Esto es especialmente util cuando queremos crear patrones
filas = 5
i = 1
while i <= filas: 
    j = 1
    while j <= i:
        print(j, end=" ")  # Imprime en la misma línea
        j += 1
    print()  # Salto de línea
    i += 1
    
"""
Esto tambien puede ser de utilidad cuando queremos limitar la repeticion del ciclo.
Como vemos el ciclo while, es similar al ciclo while, sin embargo existen diferencias claves
1. Para que el ciclo while se detenga la condicion debe cumplirse, el ciclo for tiene un numero limitado de iteraciones
2.for se ejecuta sobre un objeto iterable, while se ejecuta mienttras la condicion sea verdadera 
"""