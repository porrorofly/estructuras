codigo=int(input("Ingrese el código de controlador API REST:\n"))
match codigo:
    case 200 | 201:
        print("Solicitud exitosa.")
    case 400 | 401 | 403 | 404:
        print("Recurso no encontrado.")
    case 500 | 503:
        print("Error interno del servidor.")
    case 666:
        print("Error de conexión a la base de datos.")
        
    case _:
        print("Código de estado no reconocido.")