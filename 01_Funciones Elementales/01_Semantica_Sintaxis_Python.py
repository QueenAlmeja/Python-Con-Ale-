"""
En la programacion, la manera en que escribimos nuestro código es importante. Debemos ser precisos ya que los errores dentro del código
pueden generar fallas en la ejecución del código. 

Es Python puede que te encuentres con los concepto de semántica y sintaxis

La semántica en Python hace referencia al sentido que el programa le va a dar a las líneas de código que has escrito, 
mientras que la sintaxis es la manera en que escribimos el código siguiendo las normas establecidas y buenas prácticas. 

Vamos con un ejemplo sencillo para entender mejor esto.
"""

#El sentido en que Python leerá el código es de arriba hacia abajo ⬇️ y de izquierda a derecha ➡️

nombre = "Alejandr"
edad = 30
pais = "Venezuela"

#imprimamos las variables declaradas

print(nombre, edad, pais)

#Claro que podriamos organizar las variables dependiendo de lo que deseamos ejecutar o expresar con el codigo. Ejm:

print(f"{nombre}, vive en {pais} y actualmente tiene {edad} ")

#el orden es muy importante, especialmente cuando declaramos variables en una sola linea. Ejm:

carrera, color, mascota = "Biologia", "Vinotinto", "Canela"

print(carrera)

"""
Si por descuido escribieramos la palabra 'Vinotinto' en la primera posición después del igual, al imprimir el valor de la variable carrera, 
python nos indicaría que la variable carrera guarda el valor Vinotinto, así que debemos tener cuidado, ser organizados y precisos al escribir código
"""

#Otro ejemplo:

flor = "Margarita"
flor = "Rosa"
print(flor) #el output imprimira el string 'Rosa' 

"""
Esto sucede porque la variable flor está declarada dos veces y como Python lee el programa de arriba hacia abajo, 
el valor de la variable final que intrepretará y leerá el programa será el último que se haya declarado. 

🔴Es importante tener en cuenta esto, para evitar confusiones.

"""

#Otro ejemplo:

prin('Hola mundo, bienvenido a python')

"""
Si no somos precisos en la forma en que escribimos, variables, funciones o datos, el codigo nos arrojara un error, como en el caso del ejemplo anterior,
donde la funcion print() esta mal escrita y por ende el codigo no se puede ejecutar correctamente. 

Por suerte los editores de código ayudan a identificar en que parte del código hay un posible error resaltando 
la línea de código con algún color o al momento de ejecutar el programa, si hay un error dentro del código la consola 
te indicará en número de la línea donde se encuentra dicho error. 

Hemos empleado el uso de variables y la función print para escribir este pequeña introdución, pero:

Que es una variable?
Como se declara?
Qué es una función?
Cómo y cuando se usan?
Y todo las demás preguntas que te puedas estar haciendo lo estaremos aprendiendo paso a paso en este curso básico de programación con Python
"""