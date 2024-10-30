print("Bienvenidos a RaptorHouse 🦎🎵")
print("El mejor lugar para pasarla bien y rumbear con tus panas 💃🏼\n")

print("Hoy tenemos una promo especial. Todos los que tenga edad pares podran pasar a la ZONA VIP")
print("Las ZONA VIP tiene barra libra en bebidas y pizza, así que vamos a ver si puedes pasar 🚓 ")

user_name = input("Cual es tu nombre: ").capitalize()
age_user = float(input(f"Hola {user_name}, ¿Cual es tu edad?: "))

if age_user % 2 == 0 and age_user >= 18:
    print(f"Hey {user_name}, tu edad es un numero par! Puedes ingresar a la ZONA VIP y disfrutar de la 🍔🍻")
elif age_user % 2 != 0 and age_user >= 18:
    print(f"Vaya {user_name}, tu edad es un numero impar! Hoy no podras ingresar a la ZONA VIP 🥴")
elif age_user % 2 == 0 and age_user <= 18:
    print(f"Bueno {user_name}, tu edad es un numero par!, pero eres menor. Asi que no podras ingresar a RaptorHouse 🦎🎵")
    print("Esperate a ser mayor para venir a vacilar aqui")
elif age_user % 2 != 0 and age_user <= 18:
    print(f"Vaya vaya {user_name}, No eres mayor y tu edad no es par 🤡")
    print("Tendras que esperar a ser mayor para rumbear en la RaptorHouse")
else:
    print("Los datos que has ingresado no nos permiten determinar si puedes ingresar o no al local ⛔ ")
    
    
"""
Seguro mucha gente ha ido de fiesta y le han pedido su identificacion para saber si puedo o no ingresar 
en el local y disfrutar de una buena rumba. Bueno aqui hemos plasmado en codigo una situacion real, ademas
la logica del programa nos permite comprobar si el user es mayor y su edad es un numero par para disfrutar
de una promo especial. En esta oportunidad hemos empleado 
    1. declaracion de variables
    2. Uso de funciones elementales
    3. Uso de condicionales if, elif,else
    4. Operadores de comparacion
    5. Uso de operadores logicos AND
    6. Operaciones matematicas 
"""