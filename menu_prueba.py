from unittest import case


eleccion=int(input("Buenos días, bienvenido a nuestro restaurante.¿Qué desea ordenar?\t" \
"\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n4. Bebida\n5. Postre\n6.Acabar el pedido. \n7. Salir\n"))
pedido=[]
while eleccion != 6:
    match eleccion:
        case 1:
            print("Ha seleccionado Hamburguesa.")
            pedido.append("Hamburguesa")  
            eleccion=int(input("Buenos días, bienvenido a nuestro restaurante.¿Qué desea ordenar?\t" \
"\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n4. Bebida\n5. Postre\n6.Acabar el pedido. \n7. Salir\n"))
            
        case 2:
            print("Ha seleccionado Pizza.")
            pedido.append("Pizza")
            eleccion=int(input("Buenos días, bienvenido a nuestro restaurante.¿Qué desea ordenar?\t" \
"\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n4. Bebida\n5. Postre\n6.Acabar el pedido. \n7. Salir\n"))
            
        case 3:
            print("Ha seleccionado Ensalada.")
            pedido.append("Ensalada")
            eleccion=int(input("Buenos días, bienvenido a nuestro restaurante.¿Qué desea ordenar?\t" \
"\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n4. Bebida\n5. Postre\n6.Acabar el pedido. \n7. Salir\n"))
        case 4:
            print("Ha seleccionado Bebida.")
            pedido.append("Bebida")     
            eleccion=int(input("Buenos días, bienvenido a nuestro restaurante.¿Qué desea ordenar?\t" \
"\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n4. Bebida\n5. Postre\n6.Acabar el pedido. \n7. Salir\n"))
        case 5:
            print("Ha seleccionado Postre.")
            pedido.append("Postre")
            eleccion=int(input("Buenos días, bienvenido a nuestro restaurante.¿Qué desea ordenar?\t" \
"\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n4. Bebida\n5. Postre\n6.Acabar el pedido. \n7. Salir\n"))
        case 6:
            print("Gracias por el pedido.Tiempo de preparacion estimada {math.random.randint(10,30)} minutos.") 
            break  
        case 7:
            print("Gracias por su visita, vuelva pronto.")    
            break
