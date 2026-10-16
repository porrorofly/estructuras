""" # 1. Bucle for: Sintaxis basica (iterar listas)
# Enunciado: Dada una lista de precios de un carrito de la compra [15.50. 20.0. 35.75, 10.0],
# calcula el total iterando sobre la lista (sin usar la función sum0).
compras =[15.50, 20.0, 35.75, 10.0]
total=0
for compra in compras:
    total+=compra
print(f"Total de la compra {total}")
# 2. Bucle for: Sintaxis basica (iterar strings)
# Enunciado: Pide una palabra al usuario y cuenta cuantas vocales (a, e, i, o, u) contiene iterando
# letra por letra.
# palabra =input("Introduce la palabra ")
# contador=0
# for letras in palabra:
#     if letras in ["a","e","i","o","u"]:
#         contador+=1
# print(f"La palabra contiene {contador} vocales")

# 3. Bucle for con range()
# Enunciado: Genera la tabla de multiplicar del 8, desde el 1 hasta el 10 usando la función
# range().
print("Tabla de multiplicar de 8")
for numero in range(0,10):
    print(f"8 * {numero+1} = {8*(numero+1)}")
# 4. Bucle for con range() y paso personalizado
# Enunciado: Crea una cuenta regresiva que imprima solamente los numeros pares desde el 20
# hasta el O.
for i in range (20,-2,-2):
    print(i)
# 5. Bucle for con enumerate0
# Enunciado: Tienes una lista de tareas pendientes: ["Comprar leche", "Llamar al médico",
# "Estudiar Python"]. Imprimelas numeradas empezando desde el 1 para mostrarlas como una
# lista ofdenada.
tareas=["Comprar leche", "Llamar al médico","Estudiar Python"]
for numero , tarea in enumerate(tareas,start=1):
    print(f"{numero} .{tarea}")
# 6. Bucles for anidados
# Enunciado: Una tienda de ropa ofrece camisetas en dos tallas (M, L) y tres colores (Rojo, Azul,
# Negro). Genera y muestra todas las combinaciones posibles.
tallas=["M","L"]
colores=["Rojo","Azul","Negro"]
for i in tallas:
    for e in colores:
        print(f"Su opción es: Talla: {i} , Color: {e} ")
# 7. List comprehensions (for en una linea)
# Enunciado: A partir de la lista numeros = [1, 2, 3, 4, 5, 6], genera una nueva lista que contenga el
# cubo de cada número en una sola linea de código.
numeros = [elemento**3 for elemento in [1, 2, 3, 4, 5, 6]]
print(numeros)

# 8. List comprehensions con condicionales
# Enunciado: Dada la lista palabras = ["sol", "murcielago", "mar", "elefante", "luz"], usa una list
# comprehension para filtrar y guardar en una nueva lista solo las palabras que tengan mas de 3
# letras.
palabras = ["sol", "murcielago", "mar", "elefante", "luz"]
largos=[palabra for palabra in palabras if len(palabra)>3]
print(largos)
# 9. Bucle while: Sintaxis básica
# Enunciado: Pide al usuario que ingrese una contraseña. El programa debe seguir denegando el
# acceso y preguntando de nuevo hasta que el usuario escriba exactamente "python123".
contraseña=input("Introduce la contraseña ")
while(contraseña!="python123"):
    contraseña=input("Introduce la contraseña ")
print("contraseña correcta") """
# 10. Contador y acumulador en while
# Enunciado: Escribe un programa que pida números al usuario sin parar y los vaya sumando. El
# bucle debe terminar cuando la suma total (acumulador) supere el valor de 50. Muestra cuántos
# números se ingresaron (contador).
""" 
contador=0
suma=0
while suma<=50:
    numero=int(input("introduce un numero: "))
    suma=suma+numero
    contador+=1
print(f"Has introducido {contador} veces")
# 11. Bucle while con condiciones complejas
# Enunciado: Simula el login de un cajero. El usuario debe ingresar su PIN ("1234"). El bucle
# termina cuando acierta el PIN o cuando se superan los 3 intentos máximos permitidos.
PIN = "1234"
index = 0

while index < 3:
    request = input("Introduce su código: ")
    if request == PIN:
        print("¡Acceso concedido!")
        break
    else:
        index += 1  

 """
# 12. Bucle while infinito (con break)
# Enunciado: Crea un bucle infinito que funcione como una calculadora de sumas continuas. El
# programa pide un número. Si el usuario escribe "salir", el bucle se interrumpe con break y
# muestra el total.
#numero=input("Introduce el numero o salir para salir")
suma=0
num=0
while num!="salir":
    num=input("Introduce el numero o salir para salir ")
    if num=="salir":
        break
    else:
        suma+=int(num)
    
    
    
print(f"Total:{suma}")
    
# 13. Uso de continue en bucles
# Enunciado: Itera los números del 1 al 10 e imprímelos. Sin embargo, si el número es divisible
# por 3 (ej. 3, 6, 9), utiliza continue para saltarlo y no imprimirlo.
for i in range(11):
    if i%3==0:
        continue
    else:
        print(f"{i}")
# 14. Uso de else en bucles
# Enunciado: Busca el número 99 en la lista [10, 20, 30, 40]. Si lo encuentras, imprime
# "¡Encontrado!" y sal del bucle. Si terminas de recorrer la lista y no está, usa el bloque else del
# bucle para imprimir "Número no encontrado".
lista=[10, 20, 30, 40]
for i in range(len(lista)):
    if lista[i]==99:
        print("¡Encontrado!")
        break
    else:
        print("Número no encontrado")
    
    
# 15. Bucles for con diccionarios
# Enunciado: Tienes el inventario de una tienda de frutas en un diccionario: {"manzanas": 50,
# "peras": 30, "naranjas": 20}. Itera sobre el diccionario e imprime tanto la clave como el valor en
# una frase descriptiva.
inventario={"manzanas": 50,"peras": 30, "naranjas": 20}
for e,i in inventario.items():
    print(f"Fruta: {e} Stock:{i}")
for e in inventario.keys():
    print(e)
for e in inventario.values():
    print(e)