"""
En el siguiente apartado, haremos algunos ejercicios aplicando lo que aprendido sobre el uso 
de la funciones en escanrios de un dia a dia o experiencia que posiblemente hemos tenido.
Esto ejercicios fueron disenados empleando chatGPT, asi que puedes consultarle algo si necesitas
"""

#1.Crea un programa que recoga dos valores desde teclado y los sume 

def sumatoria(): #los parametros seran ingresados por un usario externo
    a = float(input("Ingresa un valor numerico: "))
    b = float(input("Ingresa otro valor numerico: "))
    resultado = a + b
    return resultado
print("La sumatoria total de los numeros es:", sumatoria())
#Facil, este ya lo habiammos hechos. Vamos con otro

#2. Calculemos el descuento del 10% de un producto cuando se consulta el precio

def descuento():
    precio_inicial = float(input("Ingresa el costo del producto para calcular el descuento: "))
    calculo_descuento = precio_inicial * 0.1 #hay varias formas de calcular esto, yo use la que mas me gusta
    precio_condescuento = precio_inicial - calculo_descuento
    return precio_condescuento #retornaremos solo el valor de producto una vez se haya calculado el descuento
print(f"El valor del producto aplicando el descuento es de: {descuento()}")
#🟢Como deberiamos modificar el codigo, si quisieramos que el user ingresará el % de descuento
#💡Podrias aplicar los condicionales if, else para resolver este pequeno reto

#3. Hagamos un converto de temperatura de Celsius a Fahrenheit

def temperatura():
    #F = °C × 1.8 + 32 toma en cuenta esta ecuacion
    temp_celsius = float(input("Ingresa el valor de la temperatura de tu ciudad: "))
    cambio_temp = temp_celsius * 1.8 + 32
    return cambio_temp
print("La temperatura en grados Fahrenheit es: ", temperatura())

#4.Calcular la edad en años perro -- multiplica x 7

def edad_perro(tu_edad):
    return tu_edad * 7

edad_persona = float(input("Dinos tu edad para calcular cuantos años 🐶 tienes: "))
calculo = edad_perro(edad_persona)
print(f"Tus años perros son:{calculo}")
#esta es otra forma de escribir el codigo una vez declara la la funcion empleando def

#5 Calculo de propina. Creamos un programa que determinara el porcentaje de propina que se debe dejar, segun lo consumido
"""
En este caso pensemo en que un consumo superior a los 50$ deberia generar una propina de 5%
Propina por consumo - Ideas de la logica que seguira el programa
< 50 --- 2.5
>= 50 and <= 100 -- 5
>100 and <=250 -- 7.5
>250 and <= 500 -- 10
So, let's do it 
"""

def propina():
    monto_de_consumo = float(input("Ingrese el total a pagar calcular el precio a pagar, incluyendo propina:"))
    if monto_de_consumo < 50:
        descuesto_a = monto_de_consumo * 0.025
        propina_a = monto_de_consumo + descuesto_a
        return propina_a
    elif monto_de_consumo >= 50 and monto_de_consumo <= 100:
        descuesto_b = monto_de_consumo * 0.05
        propina_b = monto_de_consumo + descuesto_b
        return propina_b
    elif monto_de_consumo > 100 and monto_de_consumo <= 250:
        descuesto_c = monto_de_consumo * 0.075
        propina_c = monto_de_consumo + descuesto_c
        return propina_c
    elif monto_de_consumo > 250 and monto_de_consumo <= 500:
        descuesto_d = monto_de_consumo * 0.10
        propina_d = monto_de_consumo + descuesto_d
        return propina_d
print(f"El precio que debes cancelar por el consumo es de: {propina()} esto incluye la propina")

"""
Existe una forma de mejor o reducir las lineas de codigo del ejemplo anterior.
A continuacion, te dejamos una alternativa:

def calcular_propina():
    monto = float(input("Ingresa el monto a cancelar: "))
    
    #aqui hacemos la logica empleando condicionales
    if monto < 50:
        porcentaje = 2.5
    elif monto <= 100:
        porcentaje = 5
    elif monto <= 250:
        porcentaje = 7.5
    elif monto <=500:
        porcentaje = 10
    else:
        porcentaje = 12
    propina = (monto * porcentaje) / 100
    return monto + propina
    
print(f"El monto que total a pagar es de: {calcular_propina()}")
"""       
