
"""
Return
Para que y como debe emplearse?
"""

#Las funciones de return es devolver un valor y salir de la funcion. Veamos un ejemplo

def ejemplo(letra):
    mensaje = "La letra es:" + letra
    return mensaje
	#mensaje2 = "La otra letra es:" + letra este bloque de cod no se mostraria despues del return
print(ejemplo("A")) 

#retornar argumentos a un parametro

def saludando():
    return "Hola, que tal?"
print(saludando()) 
#🟢Que pasa si solo llamo a la funcion como saludando() y lo saco del print()

"""
De no emplearse la funcion return, no se podria ver el resultado almacenado en una variable
"""

#Podriamos llamar a mas de una variable empleando return

def suma(a,b,c=5):
    resultado = a +b+c
    promedio = resultado/3
    return resultado, promedio
print(suma(12,45))
