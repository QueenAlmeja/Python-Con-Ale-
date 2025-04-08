"""
Asi como en la lista, en las tuplas tambien podemos realizar iteraciones
"""

tupla = (1,2,3,4,5,6,7,8,9,10)

for i in tupla:
    print(i)

names = ("Antonio", "Alvaro", "Zuko", "Gaby", "Patas", "Loro")

name5 = []
name4 = []
for name in names:
    if len(name) > 5:
        name5.append(name)
    elif len(name) < 5:
        name4.append(name)  
    else:
        print(f"El nombre {name} tiene exactamente 5 caracteres")

print(f"{name5} son nombres con mas de 5 letras")
print(f"{name4} son nombres con menos de 5 letras")