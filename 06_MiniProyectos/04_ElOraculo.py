"""
Construiremos un programa donde le consultemos a el usuario 
1. Su mes de nacimiento (Dato tipo string)
2. Si dia de nacimiento (Dato tipo int)

En base a la respuestas que el usuario proporcionara al programa, se le dira

a. Su signo zoodiacal 
b. La estrella de su signo y un dato interesantes sobre dicha estrella 
"""

#1. Comencemos por saludor bonito 😁

print("""Bienvenido a tu Carta Astral 💫.
Aqui no solo te diremos tu signo zoodiacal, sino que tambien te mencionaremos cual es el nombre de la estrella de tu constelacion 
📌Todas las constelaciones tienen una estrella importante, asi que ven y descubre la tuya
      """)

#2. Preguntemos mes de nacimiento y dia
month = input("Para comenzar dinos tu mes de nacimiento: ").capitalize()
day = int(input("Ahora dinos tu dia de cumpleaños: "))

if month == "Enero" and day >= 20 and day <= 31 or month == "Febrero" and day >= 1 and day <= 18:
    print("Oh por dios eres un Acuariano! ♒ ")
    print("Sabes que la estrella mas brillante de este signo es Sadalsuud o Beta Aquarii ")
elif month == "Febrero" and day >= 19 and day <= 29 or month == "Marzo" and day >= 1 and day <= 20:
    print("Eres un ser de agua como todos los Psicis ♓")
    print("La constelacion de ♓ tiene una de las estrellas mas brillantes del cielo nocturno, la gran Fomalhaut")
elif month == "Marzo" and day >= 21 and day <= 31 or month == "Abril" and day >= 1 and day <= 19:
    print("Eres  un poderoso signo de fuego, un gran Aries ♈")
    print("Aries tiene una estrella gigante roja conocida como Hamal")
elif month == "Abril" and day >= 20 and day <= 30 or month == "Mayo" and day >= 1 and day <= 20:
    print("Un de los signos con la mejor personalidad del zoodiaco ha llegado un Tauro ♉") 
    print("Tu ⭐, Aldebarán persigue a las Pleyades")
elif month == "Mayo" and day >= 21 and day <= 31 or month == "Junio" and day >= 1 and day <= 20:
    print("Vaya vaya, Geminis ♊ es uno de los mas controversiales de este grupo de 12")
    print("Polux y Castro brillan para ti desde el firmamento cada noche")
elif month == "Junio" and day >= 21 and day <= 30 or month == "Julio" and day >= 1 and day <= 22:
    print("Dicen que los miembros de Cancer ♋ pueden llegar a ser los mas sabios de su grupo")
    print("Tarf te cuida 50 veces mas que nuestro sol☀️")
elif month == "Julio" and day >= 23 and day <= 31 or month == "Agosto" and day >= 1 and day <= 22:
    print("Abran paso a los mas poderosos, hermoso y grandes reyes. Los leo ♌")
    print("Los Reyxs Leones son protegidos por el rey Regulus")
elif month == "Agosto" and day >= 23 and day <= 31 or month == "Septiembre" and day >= 1 and day <= 22:
    print("El viento sopla fuerte y esperanzado para los Virgos ♍")
    print("Espiga te mostrara el camino que debes cursar")
elif month == "Septiembre" and day >= 23 and day <= 30 or month == "Octubre" and day >= 1 and day <= 22:
    print("Se dice que los libras ♎ son los verdaderos maestros aires")
    print("Los cielos de los maestros se iluminan con Zubeneschamali")
elif month == "Octubre" and day >= 23 and day <= 31 or month == "Noviembre" and day >= 1 and day <= 21:
    print("Ha llegado el signo fijo del agua, Bienvenido a los Escorpio ♏")
    print("La super gigante roja Antares potencia la energia y las emociones de los Escorpio")
elif month == "Noviembre" and day >= 22 and day <= 30 or month == "Diciembre" and day >= 1 and day <= 21:
    print("Siempre positivos y buena vibra, por supuesto un Sagitario ♐")
    print("Protetores bajo el arco de Kaus Australis")
elif month == "Diciembre" and day >= 22 and day <= 31 or month == "Enero" and day >= 1 and day <= 19:
    print("Apasibles y tiernos, siempre son bienvenidos los Capricornios ♑")
    print("Deneb Algedi te cuidara siempre")
else:
  print("Debes decirnos tu signo")
    
"""
Existe mucha gente que le encata hablar sobre los signos zoodiacales. Aqui hemos creado un programa
donde con tema casual que podriamos tener en una conversacion entre amigos hemos aplicado

1. Declaracion de variables
2. Uso de condicionales if, elif, else
3. Uso de varios operadores logicos AND y OR 
4. Uso de Operadores comparativos
5. Metodos de cadenas 
"""

#Como podriamos mejor esto?



