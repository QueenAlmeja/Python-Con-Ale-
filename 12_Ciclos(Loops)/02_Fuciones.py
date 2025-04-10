"""
En el ciclo for, podemos emplear varias funciones como:
enumerate()
range()
break, continue y else
Hagamos ejemplos:
"""

#🟡enumerate()
nombres = {"Patricia", "Sofia", "Antonio", "Camila", "Jose", "Joanlys", "Billie"}

for indice, nombre in enumerate(nombres):
    print(f"El indice del nombre: {nombre} es {indice}")

"""
enumerate es una funcion que nos permite obtener el valor de indice al que corresponden los 
elementos de un iterable. La funcion puede ajustar el valor de indice donde comienza la iteracion
empleando la funcion start=
Ej
"""
nombres = {"Patricia", "Sofia", "Antonio", "Camila"}

for indice, nombre in enumerate(nombres, start=3):
    print(f"El indice del nombre: {nombre} es {indice}")
"""
La funcion enumerate es especialmente util cuando tenemos amplias colecciones de elementos 
y queremos determinar el valor de indice de algunos de ellos. 


🟡La funcion range() nos permite iterar en un rango de valores.Por defecto la iteracion comienza
en 0, pero se puede ajustar la funcion para indicar el inicio, el fin y lo saltos que debe realizar
el ciclo al momento de generar la iteracion
Ej:
"""
for i in range(20):
    print(i)
#ajustar la funcion indicando inicio y fin
for i in range (1,11):
    print(i)
#ajustamos la funcion y agregamos un salto
for i in range(0,21,3): #saltos de 3 en 3
    print(i)
"""
🟡 Al declarar un ciclo for, podemos ajustar la iteracion que este realizara con las sentencias
break, else o continue. Por lo general, estas funciones suelen emplearse con los condiconales 
Ej
"""
#break
for i in range(10):
    if i == 6: 
        break #el ciclo se detendra al llegar a 6
    print(i)
#continue
for i in range(10):
    if i == 5:
        continue #el ciclo imprimira todos los elemento contenido en el rango de valores, pero, saltara el valor de 5
    print(i)
#else se ejecuta una vez que el ciclo se ha completado y no es interrumpido por otra funcion. Ej

for i in range(5):
    print(i)
else:
    print("Este codigo no se ha interrumpido con ningun condicional o sentencia")
    
#ejemplo 2

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Este codigo tiene una interrupcion y esta linea de codigo no se ejecutara en el output")