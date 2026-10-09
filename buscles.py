#for
lista=["manzana","pera","platano","limon","fresa"]
for fruta in lista:
    print("nombre de fruta:" , fruta) 

    for letra in fruta:
        print("letra " + letra)


prices=[100,250,75,500,150]
dicounted_prices=[]
dicounted_rate=0.2
for price in prices:
    
    price*=(1-dicounted_rate)
    dicounted_prices.append(price)

print(prices)
print(dicounted_prices)
#range
for number in range(1,11,2):
    print(f"Numero: {number+1}")
for number in range(10,0,-1):
    print(f"Numero: {number}")


#tabla de multiplicar
for i in range(0,11):
    print(f"Tabla de multiplicar de {i}")
    for e in range(1,11):
        print(f"{i} * {e} ={i*e}")
#for con enumerate
tasks=["Comparar leche","Llamar al medico","Hacer ejercicio"]
for index,tarea in enumerate(tasks,start=1):
    print(f"{index}. {tarea}")

#lista compregensions:
#nueva_lista=[expresion for elemento in iterable if condicion]
#calcula los cuadrados de los 5 primeros numeros
cuadrados=[]
for numero in range(1,6):
    cuadrados.append(numero**2)
print(cuadrados)

squares=[numero **2 for numero in range(1,6)]
print(squares)
