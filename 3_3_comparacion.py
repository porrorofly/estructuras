texto1="pepe"
texto2="Pepe"
texto5="pepa"
#lo verificamos alfabeticamente
if texto1 < texto2:
    print("texto1 es menor que texto2") 
if texto1 == texto2:
    print("texto1 es igual a texto2")
elif texto1 > texto2:
    print(f"{texto1} va antes que {texto2}")
else:
    print(f"{texto1} va despues que {texto2}")