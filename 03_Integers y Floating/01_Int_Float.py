"""
Python es uno de los lenguajes de programación más empleados para el análisis de datos, 
por ello, uno de los tipos de datos más frecuentes que se almacena en las variables 
son los datos de tipo númerico 🔢. En Python existen 3 tipos de datos númericos

Los números enteros que se definen como integers ➡️ int()
Los números decimales que se conocen como flotantes ➡️ float()
Los numeros complejos que se conocen como complex  ➡️ complex()

En este curso básico nos concentraremos en los dos primeros

🔴 Los datos del tipo int podemos emplearlos para declarar una variable donde almacenemos una año, edad
o un valor que corresponda a un número entero. Ej:
"""

#Los int()

print("Estos son datos del tipo int\n")

edad = 30
print(edad)

birth_date = 1994
print(birth_date)

skincare_presupuesto = 100
print(skincare_presupuesto)

lives = -2
print(lives)

#Los float()

"""
Los datos del tipo float podemos emplearlos para declarar una variable donde almacenemos un precio, un peso o un número decimal.
En python, los números decimales se declaran empleando un punto, no una coma. Esto es muy importante ya que la mala 
sintaxis puede generar errores al momento de tratar de ejecutar el programa.
Ej:
"""

print("Estos son datos del tipo float\n")

dinero_en_cuenta = 23.4
print(dinero_en_cuenta)

GRAVEDAD = 9.8
print(GRAVEDAD)

PI = 3.14
print(PI)

#💡 Recuerda que es una buena practicar declarar elm nombre de constantes en mayúsculas

negative_num = -2.3
print(negative_num)

"""
En ambos casos (int y float) podemos emplear valores numericos positivos o negativos.
Recordemos que pueden existir operaciones en las que requiramos obtener algún
valor negativo como calcular una temperature ℃ o alguna magnitud.
"""

#🟢Reto: 
# Declara 4 variables que contengan valores númericos y empelando la función type() determina que tipo de datos está contenido dento de cada variable
