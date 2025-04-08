"""
Para manipular los diccionarios, existe varios metodos que podemos aplicar.
"""

pais = {"Brasil":"America", "Holanda": "Europa", 
            "Thailandia": "Asia",
            "Congo": "Africa", "Nueva Zelanda":"Oceania"}

#Parte I: Claves - Valores
#1.Queremos saber las claves contenidas en nuestro diccionario. Usamos el metodo keys()
print(f"Las claves de nuestro dicccionario son: {pais.keys()}")

#2. Queremos conocer los valores de cada clave consultada. Usamos el metodo values()
print(f"Los valores de las clave consultadas son {pais.values()}")

#3. Queremos saber los valores pares de las keys y los values. Usamos la funcion items()
print(f"Los pares clave-valor son: {pais.items()}")

#4. Consultar el valor de un elemento especifico dentro del diccionario. Tenemos dos formas
print(f"El valor de la clave Brasil es: {pais.get("Brasil")}")
print(f"El valor de la clave Congo es: {pais["Congo"]}")

#Parte II: Modificamos un diccionario. Agregar o eliminar elementos

#1. Agregar un nuevo elemento al diccionario con la funcion update({})
pais.update({"Haiti":"America"})
print(f"El diccionario ahora es: {pais}")
pais.update({"Italia":"Europa", "China":"Oceania"})
print(pais) #la funcion upadate nos permite agregar uno o varios elementos.
#Tambien podriamos emplear [] 
pais["Turquia"] = "EuroAsia"
print(pais)

#2. Modifiquemos el valor de clave empleando []
pais["China"] = "Asia"
print(pais)
"""
MiniReto: Que pasaria si intentas realizar la siguiente linea de codigo
pais["China", "Haiti"] = "Asia", "Europa"
print(pais)
"""

#3. Copiar un diccionario
nuevo_pais = pais.copy()
print(len(nuevo_pais))
print(len(pais))
#agregemos elemento a un de los diccionarios.
nuevo_pais.update({"Uruguay":"America", "Egipto":"Africa"})
print(nuevo_pais)

#4. Se pueden concatenar diccionario para generar uno solo. Ej
num = {"uno":1,"dos": 2,"tres":3, "cuatro":4 }
num2 = {"cinco": 5, "seis":6, "siete":7, "cuatro": 4}
total_num = num | num2
print(total_num) #si hay algun valor repetido en uno de los diccionarios, al concatenar, solo quedara uno


#5. Elimamos algun valor las funciones pop(), clear() and del 
pais.pop("Holanda")
print(pais)
pais.popitem()
print(pais)
#La funcion pop nos permitira elimina la clave-valor que indiquemos entre parentesis y popitem() remueve el ultimo par clave-valor 
pais.clear()
print(pais)
#clear eliminara todos los pares clave-valor, dejando un diccionario completamente vacio 
"""
del pais
print(pais)
Al intentar imprimir la varible pais, el programa no arrojara un error
ya que al haber eliminado el diccionario usando del, ahora pais no se encuentra definido
"""

