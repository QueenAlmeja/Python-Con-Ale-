"""
Vamos a crear un programa que nos muestre un menu de opciones con el nombre de bebidas 
que nos permita tomar un break de nuestri dia.
"""

#1.Comencemos dando un mensaje de Bienvenida 
user_name = input("Bienvenido a CoffeBreak, para atenderte, dinos tu nombre: ").capitalize()
print(f"Hola {user_name}, seguro quieres tomarte algo rico para descansar un poco")
print("\nAquí te dejamos nuestro menu para que elijas que tomarte 🫖")

"""
En esta primera parte declaramos una variable y empleamos la funcion input para recoger un dato
que sera ingresado por desde teclado por un usuario
Tambien empleamos el metodo capitalize() para asegurarnos que la primera letra del nombre de la persona
siempre este en mayusculas. Ademas se uso el formato f-string para crear un mensaje personalizado con 
el nombre de la usuario que es almacenado en la variable {user_name}
"""

#2.Creamos un menu de opciones declarando una variable y empleando la triples comillas
menu = """
 a. Cafe Negro
 b. Cafe Con Leche
 c. Expresso
 d. Latte
 e. Cappuccino
 f. Mocaccino
 g. Affogato
 h. Cafe Bombon
 i. Te Negro
 j. Te Verde
 k. Te De Frutos Rojos
 l. Salir
"""

#mostamos el menu al user para que escoga la bebida 
print(menu)

"""
3. Volvemos a declarar una variable y empleamos la funcion input para recoger el nombre de la bebida
escogida por el usuario. Ademas empleamos el metodo title() para asegurarnos que cada palabra que escriba 
el user sea en mayuscula, asi como esta indicado el la lista del menu """
user_option = input("Escribe el nombre de tu opcion para preparar tu bebida: ").title()

print("Estamos preparando tu bebida 🤎🤎🤎🤍🍻\n")


"""
4. Empleamos los condicionales para crear la logica y declarar el mensaje que se le mostrara al user de acuerdo
al nombre de la bebida que se almacene en la variable user_option
"""
if user_option == "Cafe Negro": #nos aseguramos de que el nombre de las opciones escritas dentro de esta logica coincidan con las mostradas en el menu 
    print("A sido un día pesado así que, aquí te prepararemos la opción que no falla para que te relajes y cargues energía 🔋")
elif user_option == "Cafe Con Leche":
    print("Un con leche te ayudara despejar la mente 🧠 y tomarte un respiro de tus labores")
elif user_option == "Expresso":
    print("Necesitas un poco de energia para culminar el día, así que el Expreso es la mejor opción ☕")
elif user_option == "Latte":
    print("Los Lattes se beben con sorbitos de amor y tranquilidad. Aqui tu Latte love para un descanso placentero 🖤🤍")
elif user_option == "Cappuccino":
    print("Este café te ayudará a pensar en ti por un ratito. Abraza 🫂 cada buen momento de este día con tu Cappuccino")
elif user_option == "Mocaccino":
    print("El Mocca siempre nos recuerda que es el café y el chocolate son de las mejores combinaciones para acabar nuestras tardes 🌇")
elif user_option == "Affogato":
    print("Este cafe nos recuerda un poco el amor, algo entre calido y frio para terminar nuestro día con amor y determinación 🧡")
elif user_option == "Cafe Bombon":
    print("Tu cafe de dulzura y energia favorito para despejar el pensamiento por un ratito 🍃")
elif user_option == "Te Negro":
    print("Este te suele ser el favorito de los pensadores. Tomalo con calma y disfruta este momento")
elif user_option == "Te Verde":
    print("Paz y calma para este momento combina con este te. Siente el abrazo del descanso y skipea tus preocupaciones ☺️")
elif user_option == "Te De Frutos Rojos":
    print("Los olores y sabores de este té, te haran sentir como un miembro real 👑. Descansa y disfrura ")
elif user_option == "Salir":
    print("Estas saliendo del programa")
    print("Tal vez nimguna de las opciones te provoca por ahora. Esperamos regreses pronto 👋🏼")
else:
    print("No has intrudicido ninguna opcion valida. Vuelvo a intentarlo")
    
    
"""
Este programa es sencillo y se basa en una situacion real que puede vivir cualquier persona
Con esto hemos puesto en practica:
   1. Declaracion de variables
   2. Uso de funciones basicas
   3. Metodos de sting
   4. Operadores comparativos
   5. Uso de condicionales
"""