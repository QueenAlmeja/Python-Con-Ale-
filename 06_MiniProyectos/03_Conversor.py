#1. Saludamos al user que ingresa al programa
print("Vamos a hacer un convertor de monedas.")

#2. Le muestras el menu de opciones al user
print("¿Que tipo de conversion quieres hacer? \n")
menu1 = ("""
1️⃣  De tu moneda local a dolares
2️⃣  De dolares a tu moneda local
3️⃣  De tu moneda local a euros
4️⃣  De euros a tu moneda local
         """)
print(menu1)

#3. Le preguntamos al user que desea ejecutar
user_options = int(input("Escribe el numero de la opciones del tipo de conversion que deseas usar: "))

#4. Logica del programa

if user_options == 1: #Logica de tu moneda local a dolares
    monto_cambio  = float(input("Escribe el monto de tu moneda local que deseas transformar: "))
    local_coin = float(input("Escribe el monto en tu moneda local a lo que equivale un dolar: "))
    conversion = monto_cambio / local_coin
    conversion = round(conversion, 2) #este variable permite tener una pareciacion de 2 decimales en la cantidad obtenida
    print(f"El monto en dolares es: {conversion}")
elif user_options == 2: #Logica de dolares a tu moneda local
    dolar = float(input("Escribe la cantidad en dolares que tienes: "))
    local_coin = float(input("Escribe el monto en tu moneda local a lo que equivale un dolar: "))
    conversion2 = dolar * local_coin
    conversion2 = round(conversion2, 2)
    print(f"La cantidad de dinero que tienes es: {conversion2}")
elif user_options == 3: #Logica de tu moneda local a euros
    monto_cambio = float(input("Escribe el monto en tu moneda local que deseas transformar: "))
    local_coin2 = float(input("Escribe el monto en tu moneda local a lo que equivale un euro: "))
    conversion3 = monto_cambio / local_coin2
    conversion3 = round(conversion3, 2)
    print(f"El monto en euros es: {conversion3}")
elif user_options == 4: #Logica de euros a tu moneda local
    euro = float(input("Escribe la cantidad en euros que tienes: "))
    local_coin2 = float(input("Escribe el monto en tu moneda local a lo que equivale un euro: "))
    conversion4 = euro * local_coin2
    conversion4 = round(conversion4, 2)
    print(f"La cantidad de dinero que tienes es: {conversion4}")
else:
    print("La opcion ingresada no es valida. Intentelo de nuevo.")
    
"""
Este programa es de utilidad para hacer conversion de cantidades y tranformar los valores de una moneda local
a dolares o user. En este caso ponemos en practica

    1. Declaracion de variables
    2. Uso de funciones basicas
    3. Condicionales if, elif, else
    4. Operadores comparativos 
    5. Operaciones matematicas
"""
    
#🟢Reto
#Como podrias mejorar o reducir las lineas de codigo de la logica que esta dentro de los condicionales?