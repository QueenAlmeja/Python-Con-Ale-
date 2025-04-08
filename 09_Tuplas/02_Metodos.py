"""
Las tuplas, al no poder modificarse no poseen metodos que nos permitan agregar, modificar o eliminar elementos
La forma de cambiar el contenido de una tupla es transformandola en una lista con la funcion list()

💡Sin embargo, hay un par de funciones que podemos emplear para conocer el contenido de una tupla
"""

tupla = (1,2,3,4,4,[23,45,[ 34,56]])
"""
1. Si queremos consultar la presencia de un elemento en un la tupla, podriamos emplear la funcion index()
para conocer el valor del indice en el que se ubica 
"""
print(tupla.index(4))
#Nos indicara el valor del indice donde aparece por primera vez el elemento consultado

"""
Tambien podemos emplear el siguiente metodo para acceder a los elementos de una tupla
"""
print(f"El elemento que esta el valor de indice 3 de tupla es {tupla[3]}")


"""
index puede aceptar un segundo valor de parametro que indicara al programa desde que punto debe 
comenzar a realizar la busqueda.
"""
print(tupla.index(4, 2)) #el primer valor es el elemento que queremos buscar, el segundo, la posicion desde donde iniciara la busquedad

"""
2. Para determinar el numero de veces que aparece un elemento en una tupla, empleando la funcion count()
"""
print(tupla.count(4))

"""
3 Tambien podemos eliminar una tupla, empleando la funcion del
Las tuplas no permiten la funcion clear()
"""
#del tupla
#print(tupla) #el codigo dira que la variable no esta definida

