"""
Slicing es un método que empleamos para extraer subconjuntos de caractéres de una variable
Así como en la indezación, este método emplea los valores de los indices para ingresar a un número determinado de caractéres 
"""

#Supongamos que tenemos la siguiente variable

song = "Now that we don't talk"
#veamos cuantos caracteres conformar el string de la variable song

print(len(song)) 

#Queremos extraer todos los caracteres. Tenemos varias formas

print(song[0:22]) #este slicing va desde la primera posicion, hasta la ultima
print(song[:]) #esta es otra forma de escribir la primera posicion y la ultima posicion de una cadena de texto
print(song[:22]) #esta es otra forma de indicar las posiciones de las que queremos extrar nuestro slicing

"""
Es importante recordar que en el método de slicing, si no se especifíca la posición final, Python asume 
que la porción de caractéres que se quiere extrar va desde la posicion inicia indica, hasta el final. 
Por otro lado, cuando se indica la posicion final a la que se desea llegar, Python excluye el caracter 
que corresponde a la posicion final indicada en el slicing. Vamos con ejemplos:
"""
#Primer caso:

frase = "Programar es divertido y nos ayuda a ejercitar la mente"
print(frase[5:])

#Segundo caso:
print(frase[10:15]) #la v que se ubica en la posicion 15 de la cadena de texto, no se incluye en el output

#Hagamos un ejemplo con valores negativos
#[-1] siempre sera el valor que corresponde al último caracter de la cadena de texto
#Las posiciones positivas y negativas son equivalentes y son intercambiables

print(frase[-1]) #esta es la última letra de la cadena de texto
print(frase[-2]) #asi podemos continuar a lo largo de los caracteres de la cadena de texto

print("El siguiente print nos muestra la subcadena de caracteres que se ubican desde el valor de indice -5 hasta el final\n")
print(frase[-5:]) #este slicing nos muestra los caracteres que se ubican desde la posicion -5 hasta el final 

print("El siguiente print nos muestra la subcadena de caractéres que se ubican desde el valor de indice 0 hasta -5")
print(frase[:-5]) #este slicing nos muestra los caracteres que se ubican desde la posicion hasta hasta la posicion -5

#Dando saltos entre la cadena usando el metodo de slicing [::]
"""
El metodo slicing nos permite extraer caractéres y crear subcadenas de los stings. Algo importante de resaltar
es que el uso de indice nos permite extraer caracteres dando saltos, usando tres parametros entre el indice. 
[posicion_inicial:posicion_final:salto]

Veamos un ejemplo
"""
print(frase[:])
print(frase[::3]) 

#Si el salto es negativo, Python nos permite ir de derecha a izquierda

print(frase[::-1]) #esto nos muestra la cadena de texto en reversa
print(frase[::-2]) #esto nos muestra la cadena de texto con saltos de 2 en 2 caractéres en reversa

#Es importante que tengamos coherencias cuando usemos este método, si nuestra cadena de texto se compone de 5 caracteres, no sería lógico que indice del salto de de 5

"""
📌Breve resumen
1. El primer número es el indice inicial, el segundo número es el indice final, y el tercero es el salto.
2. Si no se especifíca el indice inicial, Python asume que es 0.
3. Si no se especifíca el indice final, Python asume que es la longitud de la cadena de texto.
4. Si no se especifíca el salto, Python asume que es 1.
5. Si el salto es negativo, Python nos permite ir de derecha a izquierda.
"""

