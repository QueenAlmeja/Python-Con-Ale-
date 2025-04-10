"""
El metodo list comprehesion es un metodo o estilo de sintaxis en python que nos permite crear lista.
La ventaja de este metodo es que resumen en una sola linea de codigo lo que a veces hacemos en varias
Junto con este codigo solemos usar mucho el ciclo for. Ej
"""
cuadrados = [i**2 for i in range(10)]
print(f"la lista de numero cuadrados es: {cuadrados}")
#🔴estructura basica de una list comprehesion 
#cuadrados: es lo que se agregara a la nueva lista, en este caso hemos empleado la palabra cuadrados
# for i in range: ciclo que recorrera el objeto iterable 
#resumen: lista = [expresion for element in iterable]
"""
Dentro de la estructura basica de un list comprehesion tambien podemos agregar condicionales. 
Hagamos el ejemplo de los numero pares e impares
"""
num = [1,2,3,4,5,6,7,8,9,10]
pares = [i for i in num if i % 2 == 0 and i > 4]
print(f"Esta es la lista de numeros pares mayores a 4 {pares}")
#🟢Minireto: realiza el ejercicio sacando los cuadradados de los numero impares mayores a 5

nombres = ["melani", "rudy", "nemo", "gaby", "samanta"]
mayusculas = [i.capitalize() for i in nombres]
print(mayusculas)
"""
El metodo comprehesion list se puede aplicar unicamente a las listas?
No, este metodo se puede aplicar a otros tipos de variables como los diccionarios
"""
#Aplicando a str
frase = "supercalifragilisticoespialidoso"
vocales = [i for i in frase if i == "a" or i == "e" or i == "i" or i == "o" or i == "u"]
print(vocales)

#Aplicando a set 
set = {"Manaties", "Monos", "Mariposa", "Tarantula", "Zebra", "Leon"}
solo_m = {i for i in set if i.startswith("M")}
print(solo_m)

#Aplicando a diccionario
numero = [2,3,4,5,6]
cuadrado = [i**2 for i in numero]
print(cuadrado)

num_dic = {i:j for i,j in zip(numero, cuadrado)}
print(num_dic)