"""
Los operadores lógicos : AND, OR, NOT 

Los procesos comparativos son muy frecuentes dentro de la programación. Para realizar comparaciones
entre elementos, variables o tipos de datos empleamos los operadores lógicos que permiten hacer pruebas 
entre elementos, datos o variables y nos propocionan una respuesta en forma de booleans

Tenemos 3 operadores logicos

➡️ AND :Quien regresa un valor booeal True siempre y cuando TODAS las variables que se estén comprobando
sean VERDADERAS

➡️ OR : Quien regresa un valor booeal True siempre y cuando AL MENOS UNA de las variables que se estén comprobando
almacene el valor True y regresa False cuando todas las variables que se estén comprobando sean False

➡️ NOT : Invierte el valor descritó en la variable y devuelve un valor opuesto con el que se ha definidó la variable. 

Hagamos ejercicios
"""

#Declaremos variables con valores booleanos : Recuerda los enunciados que definen cada operador 

is_day = True
is_happy = False
is_sunny = False
is_cool = True

#Usando solo AND
comp1 = is_day and is_happy 

print(f"Es de dia? : {is_day}: ")
print(f"Es un dia feliz? : {is_happy}")
print(f"Es de dia y es un dia soleado: {comp1}\n")


comp2 = is_day and is_cool

print(f"Es de dia? : {is_day}: ")
print(f"Es un dia frio ? : {is_cool}")
print(f"Es de dia y es un dia frio?: {comp2}\n")


#Usando solo OR 

comp3 = is_day or is_sunny


print(f"Es de dia?: {is_day}")
print(f"Es un dia soleado?: {is_sunny}")
print(f"Podria ser un dia soleado?: {comp3}\n")

comp4 = is_happy or is_sunny

print(f"Es un dia feliz?: {is_happy}")
print(f"Es un dia soleado?: {is_sunny}")
print(f"Podria ser un dia soleado y feliz?: {comp4}\n")

comp5 = is_day or is_cool
print(f"Es de dia?: {is_day}")
print(f"Es un dia frio?: {is_cool}")
print(f"Podria ser un dia frio?: {comp5}\n")

#NOT 

comp6 = not is_day

print(f"Es de dia?: {comp6}\n")

#Podriamos emplear varios operadores al mismo tiempo? Intentemos a ver

comp7 = (not is_day and is_happy) or (is_day and is_cool) or (is_happy or is_sunny) and (is_day and not is_sunny)

print(comp7)

"""
🟢RETO

Antonio es un chico muy inteligente que estudia ciencias computacionales.
No estudia todos los días, pero si juega video juegos todas las mañanas.
Es alguien amable que le encanta salir con sus amigos a comer, pero no le gustan mucho las fiesta.

Tomando el siguiente enunciado, crea una variables sobre:
Es Antonio un chico?
Es Antonio inteligente?
Antonio estudia todos los dias?
Antonio juega todos los dias?
Es Antonio amable?
Antonio tiene amigos?
Antonio le gustan las fiestas?

Haz comparaciones entre las variables declaradas e invierte el valor de 3 de ellas 
"""