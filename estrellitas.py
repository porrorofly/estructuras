import random
""" for i in range(1,5):
    
    for j in range(i,6):
        print("*", end="")
    print(" ")
 """
    #ejercicio de profe
for i in range(5,1,-1):
    
    for j in range(1,i):
        randoms=random.randint(1,9)
        if randoms%2==0:
            randoms="p"
        print(randoms, end=" ")
    print(" ")