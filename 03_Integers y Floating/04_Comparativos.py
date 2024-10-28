"""
En la programación se puede hacer comparación para constrastar o verificar los datos o valores 
que componen una variable. 

El output que se obtiene en la comparación de datos son valores booleanos que indican el estado 
True or False.

La comparaciones de variables o datos se efectuan empleando los siguientes operadores 

== ➡️ es igual a 
!= ➡️ es distinto a 
>  ➡️ es mayor a 
>= ➡️ es mayor e igual
<  ➡️ es menor a 
<= ➡️ es menor o igual

Vamos con ejemplos
"""
print("\nEjemplos empleandos valores numericos\n")
x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Ejemplo con operaciones matemáticas

print((5*4) >= (7*9))

"""
Los operadores comparativos tambien pueden emplearse para comparar cadenas de texto o variables 
que contienen string y aunque aún no hemos hablado sobre que son los string, tranquilo, ya llegaremos 
allí, por ahora, te dejo unos ejemplos básicos para que comprendas bien estos conceptos
"""

print("\nEjemplos empleandos cadenas de texto\n")
name = "Alejandra"
name2 = "Gabriela"

print(name == name2)
print(name != name)
print(name > name2)
print(name < name2)
print(name <= name2)
print(name >= name2)

"""
💡
Toma en cuenta que los strings almacenados en variables puede no tener el mismo número de caracteres
En este punto, es bueno recordar el uso de la funcion len() 
"""