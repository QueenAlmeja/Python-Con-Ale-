#1. Hacemos un print con un saludo de bienvenida que se mostrara al user que ingrese al programa de compras 
print("Bienvenido a ShoppingLab 🛒. Todo lo que necesitas en un solo lugar\n")
print("Aprovecha nuestras ofertas diaria y ahorra tu 💵 comprando inteligentemente\n")
print("Tendras disponibles despuestos del '20, 35, 50 %' de descuento en algunos productos que adquieras ✅\n")

#2. Pedimos al user que ingrese el nombre y el monto neto del producto  
name_producto = input("🗣️ Dinos el nombre de producto: ").title()
price_product = float(input("💳Dinos el monto neto del producto que has escogido: "))

#3. Calculamos el descuento que se aplicara al producto

if price_product <= 50: #el producto tendra un descuento de 20% 
    descuento = price_product * 0.20
    precio_final = price_product - descuento
    print(f"{name_producto} tienen un descuento de 20% 🛍️⬇️ 💙")
    print(f"El precio final a pagar sera: {precio_final}")
    print("Gracias por tu compra 👋🏼")
elif price_product >= 51 and price_product <= 110: #el producto tendra un descuento de 35%
    descuento = price_product * 0.35
    precio_final = price_product - descuento
    print(f"{name_producto} tienen un descuento de 35% 🛍️ 🧡")
    print(f"El precio final a pagar sera: {precio_final}")
    print("Gracias por tu compra 👋🏼")
elif price_product >= 111 and price_product <= 200: #el producto tendra un descuento de 50%
    descuento = price_product * 0.50
    precio_final = price_product - descuento
    print(f"{name_producto} tienen un descuento de 50% 🛍️ 🩷")
    print(f"El precio final a pagar sera: {precio_final}")
    print("Gracias por tu compra 👋🏼")
elif price_product >= 201: #sin descuento 
    print("Por el momento tu producto no tiene descuento 🥲") 
    print(f"El monto que deberas cancelar sera {price_product}")
else: #monto o valor invalido 
    print("No has ingresado ningun monto. Debes volver a intentarlo")
    
"""
Este programa calcula los valores con descuento de productos que uno persona podria estar comprando 
en un supermercado. Para este caso hemos empleado:

    1. Declaracion de variable
    2. Tranformacion de datos
    3. Operaciones matematicas 
    4. Condicionales if, elif, else
    5. Operadores comparativos 
    6. Metodos de cadenas 
"""
    






