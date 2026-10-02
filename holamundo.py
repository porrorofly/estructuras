import random
"""print("Hola Mundo ")
x=2
l=[]
while x>=2:
    x=x+1
    if x%2==0 and x%5==0 and x%3==0 and  x%6==0 and x%4==0 and not x%32==0 and not x%55==0:
        print(x)
        l.append(x)
    
    if x==1000:
        break
print(str(l))
lista1 =[1,2,3]
lista2=[3,2,1]
lista3=lista1

print(lista1==lista2)
print(lista1 is lista2)
print(lista1 is lista3)
saludo ="Hola mundo"
print("Verdad o falso ")
print("Hola" in saludo)
print("pepe" in saludo)

#ipor teclado
nombre=input("Pon tu nombre")
entero=int(input("Pon tu edad"))



"""

#problema "Lea por la pantalla dos n. enteros y si los doa numneros son mayores que 0"




"""
entero1=0
entero2=0 
while True:
    entero1=int(input("Introduce el numero mauor que 0: "))
    entero2=int(input("Introduce el numero mauor que 0: "))
    if (entero1<=0 or entero2<=0):
        True
    else: 
        print("Todo correcto")
        break



a=8
if a >5:
    print("Mayor que 5")
elif a>7:
    print("Mayor que 7")

"""


#nota aprobado <5suspenso ,entre ==5 y <7 aprobado,desde ==7 hasta <8.5 notable y 8.5 y 10 sobresaliente
nota=float(input("Introduce la nota "))
if nota<5:
    print("Está suspendido")
elif nota>=5 and nota<7:
    print("Está aprobado")
elif nota>=7 and nota<8.5:
    print("Su nota es Notable")
elif nota>=8.5 and nota<=10:
    print("Felicidades,es un sobresaliente")    
