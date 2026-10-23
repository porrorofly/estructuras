def sumar(uno ,dos):
    return (uno+dos)

sumar(7,8)
print(sumar(7,8))



def calcular(numeros):
    total=sum(numeros)
    promedio=total/len(numeros)
    maximo=max(numeros)
    return total,promedio,maximo

suma,prom,max_val=calcular([10,20,30,40,50,60])
print(f"{suma},{prom,max_val}")
