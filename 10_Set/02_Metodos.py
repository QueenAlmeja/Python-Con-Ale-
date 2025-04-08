"""
En los conjuntos se pueden agregar o eliminar elementos empleando algunas funciones conocidas
"""

mi_set = {1,2,3,4,5,6}
print(type(mi_set), mi_set)

#1 Agregar un elemento usando la funcion add()
mi_set.add(7)
print(f"El conjunto es: {mi_set}")
"""
Pregunta rapida: Que pasa si intentamos agregar el numero 2 al conjunto ya declarado❓
"""

#2 Agregar varios elementos al conjunto con la funcion update()
mi_set.update([8,9,11])
print(f"El conjunto es: {mi_set}")

#3 Eliminamos un elemento usando la funcion remove(), discar() y pop()
mi_set.remove(4)
print(f"El conjunto es: {mi_set}")
mi_set.discard(10)
print(f"El conjunto es: {mi_set}")
mi_set.pop()
print(f"El conjunto es: {mi_set}")

"""
Si intentamos eliminar un elemento de set con la funcion discard(), el elemento se borrara del conjunto,
sin embargo, de no existir tal dato dentro del conjunto, el codigo no generara ningun error en codigo.

El metodo pop eliminara un elemento aleatorio del conjunto. Si bien, puede emplearse, no es recomendable
ya que los conjuntos no mantienen un orden

Pregunta rapida: Que pasa si intentamos eliminar un elemento que no forma parte del conjunto
empleando la funcion remove()❓
"""

#4 Copiar un set
mi_set2 = mi_set.copy()
print(f"Este es el set original {mi_set}")
print(f"Esta es una copia del set {mi_set2}")
#agregamos o modificamos el set original
mi_set.update([23,12,45,34])
print(mi_set)
"""
Asi como en la lista, hacer una copia de un set nos permite tener un respaldo del original
"""

#5 Limpiamos el conjunto con la funcion clear()

mi_set.clear()
print(f"El conjunto es: {mi_set}")

"""
Eliminamos todo el conjunto con la funcion del

del mi_set
print(f"El conjunto es: {mi_set}") 
#Devolvera un un error de tipo NameError porque el conjunto no ha sido definido
"""