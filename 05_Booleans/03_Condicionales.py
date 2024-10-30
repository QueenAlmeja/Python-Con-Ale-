"""
Un aspecto fundamental en el que se pueden relacionar el uso de variables que guardan datos booleanos
y operadores lógicos es la toma de decisión que puede ejecutar un bloque de código. 

Gran parte de la lógica que efectuan los códigos requiere de la toma de decisión y para tomar decisiones
en Python debemos emplear los codicionales if, elif o else

El uso de los condicionales determina si un bloque de código se ejecutará o no. 
Este aspecto dentro de la programacion se puede comparar con las rutinas diarias que solemos realizar. 

El uso de los condicionales viene acopañado de conceptos que ya hemos estudiado antes, así que 
aquí pondremos en paráctica algunas cosas que hemos visto con anterioridad. 

Vamos con ejemplos basicos
"""

x = 5 

if x <= 6:
    print(f"El valor de la variable x es menor o igual a 6\n")
elif x >= 6:
    print(f"El valor de la variable x es mayor o igual\n") 
else:
    print(f"La variable x no tiene asignado un valor")

"""
Cuando ejecutamos el bloque de código que hemos construido, el print() que nos mostrará el output
será el que est+a declarado despues de el condicional if ya que la lógica declarada para este
condicional es el que cumple con lo que está sucediendo, es decir, que el valor contenido en la variable
x es menor o igual a cualquir numero inferior a 6

Veamos mas ejemplo
"""

is_boy = False
is_student = True 

if is_boy and is_student:
    print("La persona no es un chico, pero es estudiante")
elif is_boy or is_student:
    print("La persona tal vez no es un chico, pero es un estudiante")
else:
    print("El programa no puede describir al persona")

"""
En este caso, la linea de código que se ejecuta es la descrita para el condicional elif porque
recuerda que cuando comparamos variables operadores lógicos, lo que se comparar empleando el operador
OR sera True si al menos algunos de los elementos comparados es True, lo que coincide con lo descrito
por el segundo condicional. En este caso, la persona no es un chico, pero si es un estudiante, 
por lo que el output del print() del condicional elif es el que cumple con lo que esta sucediendo

📌Algo muy importante en el uso de los condiconales es el uso de la IDENTACIÓN que es el espacio que se deja
para declarar lo que sucedera si se cumple la condicion descrita en el condicional. Si este espacio no se 
declara, Python interpretará el código como un error y no se ejecutará el bloque de código que sigue.

El uso de los condiconales está muy relacionado con la interación que puede suceder entre un usuario y el programa
Para que recoger un valor desde teclado, se emplea la funcion basica input. Una vez que el usuario a ingresado un
valor, el código puede emplear esta información para tomar una decisión y ejecutar un programa. 
Veamoslo en codigo 👩‍💻
"""

#Vamos a preguntarle a un usuario su edad para dejarlo entrar a un club

user_edad = int(input("Dinos tu edad para ver si puedes ingresar al club ThePythonGuys: "))

if user_edad >= 18:
    print(f"El usuario tiene {user_edad}, puede pasar a al club y disfrutar de la rumba 🥳")
else:
    print("🔴 Lo sentimos chicuelo, eres menor de edad asi que no puedes pasar al club")
    
"""
🟢 Reto

Vamos a crear un programa empleando una rutina diaria.

Supon que son las 2PM y vas a tomarte un break de tu trabajo u horas de estudio y deseas tomarte algo para
relajarte. Crea una variable empleando input para  preguntar ¿Qué deseas tomar hoy: ?. 

Posteriormente emplea operadores comparativos y condicionales para crear una bloque de condigo que se ejecutara
empleando la informacion recogida por la funcion input. 

Te dejo una idea 💡

drink = inpt("Que quieres tomar hoy?: ")

if drink == "x":
    print(f"Genial! Quieres tomar un {x}")
elif drink == "y":
    print(f"Hoy es un buen dia para tomar un {y}")
else:
    print("No nos has dicho que tomar")


"""