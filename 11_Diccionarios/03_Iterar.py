"""
Sobre un diccionario tambien se puede realizar iteraciones. Ej
"""
pais = {"Brasil":"America", "Holanda": "Europa", 
            "Thailandia": "Asia",
            "Congo": "Africa", "Nueva Zelanda":"Oceania"}

for i in pais.keys():
      print(i)
      
#otra forma de mostrar tanto los keys como los values seria


for i, j in pais.items():
    print(f"País: {i}, pertenece: {j}")

for i in pais.keys():
    print(f"País: {i}, País al que pertenece: {pais[i]}")