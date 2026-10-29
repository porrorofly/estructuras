# =============================================================================
# EJERCICIOS DE PREPARACIÓN PARA EL EXAMEN (RESUELTOS)
# Cada ejercicio lleva su enunciado como comentario y, debajo, la solución.
# =============================================================================


# =============================================================================
# EJERCICIO 1: Predice la salida (operadores y lógica)
#
# ENUNCIADO:
#   Sin ejecutar el código, escribe qué imprime cada línea y justifica por qué.
#   Después modifica c.append(4) y explica qué valen a, b y c, y por qué.
#
#       a = [1, 2, 3]
#       b = [1, 2, 3]
#       c = a
#       print(a == b)
#       print(a is b)
#       print(a is c)
#       print(bool(""), bool(" "), bool([]), bool(0.0), bool("False"))
#       print(17 // 5, 17 % 5, 2 ** 3 ** 2)
#       print(5 > 3 > 1, 5 > 3 > 4)
#       print("apple" < "Apple", "apple" < "apples")
#       print(None or 0 or "Hola" or 5)
#       print("Py" in "Python", "java" not in ["Python", "PHP"])
# =============================================================================
def ejercicio_1():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(a == b)   # True  -> == compara VALORES
    print(a is b)   # False -> is compara IDENTIDAD: son dos objetos distintos
    print(a is c)   # True  -> c apunta al mismo objeto que a

    # "" falsy | " " truthy (tiene un carácter) | [] falsy | 0.0 falsy
    # "False" truthy (es un string no vacío)
    print(bool(""), bool(" "), bool([]), bool(0.0), bool("False"))
    # -> False True False False True

    # // división entera | % resto | ** asocia por la derecha: 3**2=9 -> 2**9=512
    print(17 // 5, 17 % 5, 2 ** 3 ** 2)   # -> 3 2 512

    # Comparación encadenada: (5>3 and 3>1) -> True | (5>3 and 3>4) -> False
    print(5 > 3 > 1, 5 > 3 > 4)           # -> True False

    # 'a' (97) es mayor que 'A' (65) -> "apple" < "Apple" es False
    # "apple" es prefijo más corto de "apples" -> True
    print("apple" < "Apple", "apple" < "apples")   # -> False True

    # or devuelve el primer valor truthy (None y 0 son falsy)
    print(None or 0 or "Hola" or 5)       # -> Hola

    print("Py" in "Python", "java" not in ["Python", "PHP"])   # -> True True

    # Tras c.append(4):
    c.append(4)
    print(a, b, c)
    # a y c -> [1, 2, 3, 4]  (son el MISMO objeto: aliasing)
    # b     -> [1, 2, 3]     (es otro objeto distinto, no cambia)


# =============================================================================
# EJERCICIO 2: Validador de registro (condicionales y strings)
#
# ENUNCIADO:
#   Pide al usuario un nombre, una edad y un correo. Antes de validar,
#   sanitiza las entradas con .strip() y .lower() donde proceda.
#   Muestra un único mensaje de error según el primer fallo, usando
#   if-elif-else:
#     - Si el nombre o el correo están vacíos: "ERROR: campos vacíos".
#     - Si la edad no es un número entero (.isdigit()): "ERROR: edad no válida".
#     - Si el correo no tiene exactamente una @ o contiene espacios:
#       "ERROR: correo no válido".
#     - Si todo es correcto, clasifica la edad con match-case con guardas
#       (case e if e < 18, etc.) en "Menor", "Adulto" o "Jubilado" (>= 65)
#       y muestra: Registro OK: Ana (Adulto) - ana@mail.com
#   EXTRA: usa un operador ternario para añadir "(mayoría de edad)" o
#          "(menor)" al mensaje final.
# =============================================================================
def ejercicio_2():
    nombre = input("Nombre: ").strip()
    edad = input("Edad: ").strip()
    correo = input("Correo: ").strip().lower()

    if nombre == "" or correo == "":
        print("ERROR: campos vacíos")
    elif not edad.isdigit():                      # .isdigit() ANTES de int()
        print("ERROR: edad no válida")
    elif correo.count("@") != 1 or " " in correo:
        print("ERROR: correo no válido")
    else:
        edad_num = int(edad)

        # Las guardas se evalúan de arriba abajo: gana la primera que se cumple
        match edad_num:
            case e if e < 18:
                categoria = "Menor"
            case e if e < 65:
                categoria = "Adulto"
            case _:
                categoria = "Jubilado"

        extra = "(mayoría de edad)" if edad_num >= 18 else "(menor)"   # ternario
        print(f"Registro OK: {nombre.title()} ({categoria}) - {correo} {extra}")


# =============================================================================
# EJERCICIO 3: Cajero con reintentos (bucles)
#
# ENUNCIADO:
#   Simula un cajero automático:
#   1. El PIN correcto es "1234". El usuario tiene 3 intentos (usa while con
#      contador y condición compuesta).
#   2. Si acierta, entra en un menú infinito (while True) con las opciones:
#        1 -> ingresar dinero (suma al saldo)
#        2 -> retirar dinero (si no hay saldo suficiente, usa continue y
#             muestra un aviso)
#        3 -> salir (break) y mostrar el saldo final
#   3. Si agota los intentos sin acertar, usa el else del bucle para mostrar
#      "Tarjeta bloqueada".
#   EXTRA: guarda los movimientos en una lista y, al salir, imprímelos
#          numerados con enumerate(movimientos, start=1).
# =============================================================================
def ejercicio_3():
    PIN = "1234"
    intentos = 0

    while intentos < 3:
        if input("PIN: ").strip() == PIN:
            print("Acceso concedido")
            break
        intentos += 1
        print(f"PIN incorrecto. Intentos restantes: {3 - intentos}")
    else:
        # El else del while solo se ejecuta si el bucle terminó SIN break
        print("Tarjeta bloqueada")
        return

    saldo = 0
    movimientos = []

    while True:
        print("\n1. Ingresar  2. Retirar  3. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cantidad = input("Cantidad: ").strip()
            if not cantidad.isdigit():
                print("Cantidad no válida")
                continue
            saldo += int(cantidad)
            movimientos.append(f"Ingreso: +{cantidad}")
        elif opcion == "2":
            cantidad = input("Cantidad: ").strip()
            if not cantidad.isdigit():
                print("Cantidad no válida")
                continue
            if int(cantidad) > saldo:
                print("Saldo insuficiente")
                continue
            saldo -= int(cantidad)
            movimientos.append(f"Retirada: -{cantidad}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

    print(f"\nSaldo final: {saldo}")
    for i, mov in enumerate(movimientos, start=1):
        print(f"{i}. {mov}")


# =============================================================================
# EJERCICIO 4: Funciones y list comprehensions
#
# ENUNCIADO:
#   Escribe estas funciones con docstring y sin variables globales:
#
#   a) estadisticas(*numeros) devuelve tres valores (suma, media, máximo)
#      mediante un return múltiple. Si no recibe números, hace un return
#      anticipado devolviendo (0, 0, None).
#
#   b) filtrar_palabras(palabras, min_letras=4) devuelve, con una list
#      comprehension, las palabras con al menos min_letras letras, en
#      mayúsculas.
#
#   c) crear_multiplicador(factor) devuelve una función interna (closure)
#      que multiplica por factor. Crea triplicar = crear_multiplicador(3)
#      y prueba triplicar(7).
#
#   d) Detecta el bug y corrígelo. Explica qué imprime y por qué es un
#      error de diseño:
#          def agregar(item, lista=[]):
#              lista.append(item)
#              return lista
#          print(agregar(1))
#          print(agregar(2))
# =============================================================================
def estadisticas(*numeros):
    """Devuelve (suma, media, máximo) de los números recibidos."""
    if not numeros:                  # return anticipado
        return 0, 0, None
    suma = sum(numeros)
    return suma, suma / len(numeros), max(numeros)   # return múltiple (tupla)


def filtrar_palabras(palabras, min_letras=4):
    """Devuelve en mayúsculas las palabras con al menos min_letras letras."""
    return [p.upper() for p in palabras if len(p) >= min_letras]


def crear_multiplicador(factor):
    """Devuelve una función que multiplica su argumento por factor."""
    def multiplicar(numero):
        return numero * factor       # closure: recuerda 'factor'
    return multiplicar


# d) BUG: la lista por defecto se crea UNA SOLA VEZ, al definir la función,
#    y se reutiliza en todas las llamadas. Al ser mutable, acumula el estado:
#        agregar(1) -> [1]
#        agregar(2) -> [1, 2]   (¡esperábamos [2]!)
#
#    CORRECCIÓN: usar None como valor por defecto y crear la lista dentro.
def agregar(item, lista=None):
    """Añade item a una lista (nueva si no se pasa ninguna)."""
    if lista is None:
        lista = []
    lista.append(item)
    return lista


def ejercicio_4():
    print(estadisticas(4, 8, 6))      # (18, 6.0, 8)
    print(estadisticas())             # (0, 0, None)
    print(filtrar_palabras(["sol", "mar", "elefante", "luz", "casa"]))
    # ['ELEFANTE', 'CASA']
    triplicar = crear_multiplicador(3)
    print(triplicar(7))               # 21
    print(agregar(1))                 # [1]
    print(agregar(2))                 # [2]


# =============================================================================
# EJERCICIO 5: Teletubbies con herencia (POO)
#
# ENUNCIADO:
#   Parte de tu clase PersonajeTeletubby (con saludo_oficial, atributos
#   públicos, __nivel_hambre y __nivel_felicidad privados, y __str__/__repr__)
#   y amplíala:
#
#   a) Crea la subclase TeletubbyDeportista(PersonajeTeletubby) con un
#      atributo extra __energia = 100. Usa super().__init__(...) en el
#      constructor.
#   b) Sobrescribe jugar() para que llame primero a super().jugar() y además
#      reduzca la energía en 30. Si la energía es menor que 30, debe imprimir
#      que está cansado y NO jugar (return anticipado).
#   c) Añade un método descansar() que restaure la energía a 100.
#   d) En el main, crea una lista con un PersonajeTeletubby y un
#      TeletubbyDeportista, recórrela con un for llamando a jugar() en cada
#      uno (polimorfismo) e imprime la lista completa (¿se usa __str__ o
#      __repr__?).
#   e) TEORÍA:
#        - ¿Qué ocurre si haces po.__nivel_hambre = 0 desde fuera de la
#          clase? ¿Cómo se llama el mecanismo y cómo se podría acceder
#          realmente al atributo?
#        - Si class Cyborg(Humano, Robot) y ambas tienen accion_principal(),
#          ¿cuál se ejecuta y cómo lo compruebas?
# =============================================================================
class PersonajeTeletubby:
    saludo_oficial = "¡Tubby abrazo!"      # atributo de clase

    def __init__(self, nombre, color, antena, objeto_favorito):
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        self.__nivel_hambre = 50           # privado -> _PersonajeTeletubby__nivel_hambre
        self.__nivel_felicidad = 100

    def saludar(self):
        print(f"¡Oh-oh! Soy {self.nombre}, soy {self.color} y mi antena es "
              f"{self.antena}. {self.saludo_oficial}")

    def jugar(self):
        print(f"{self.nombre} juega con su {self.objeto_favorito}.")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10

    def comer_tubby_papilla(self):
        print(f"{self.nombre} se come la Tubby Papilla. ¡Slurp!")
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20

    def ver_estado(self):
        return (f"Felicidad: {self.__nivel_felicidad} | "
                f"Hambre: {self.__nivel_hambre}")

    def __str__(self):
        return f"Teletubby {self.nombre} ({self.color}) - {self.ver_estado()}"

    def __repr__(self):
        return (f"{type(self).__name__}('{self.nombre}', '{self.color}', "
                f"'{self.antena}', '{self.objeto_favorito}')")


# a) Subclase con energía privada
class TeletubbyDeportista(PersonajeTeletubby):
    def __init__(self, nombre, color, antena, objeto_favorito):
        super().__init__(nombre, color, antena, objeto_favorito)
        self.__energia = 100               # -> _TeletubbyDeportista__energia

    # b) jugar() sobrescrito
    def jugar(self):
        if self.__energia < 30:            # return anticipado
            print(f"{self.nombre} está cansado y no puede jugar.")
            return
        super().jugar()
        self.__energia -= 30

    # c) descansar()
    def descansar(self):
        self.__energia = 100
        print(f"{self.nombre} ha descansado.")


def ejercicio_5():
    # d) Lista con ambos tipos y polimorfismo
    po = PersonajeTeletubby("Po", "Rojo", "Círculo", "Patinete")
    dipsy = TeletubbyDeportista("Dipsy", "Verde", "Antena recta", "Sombrero")

    lista = [po, dipsy]
    for p in lista:
        p.jugar()              # cada objeto ejecuta SU versión de jugar()

    print(lista)               # usa __repr__ (las listas muestran sus
                               # elementos con repr, no con str)
    print(po)                  # print(objeto) usa __str__

    # e) TEORÍA
    # 1) po.__nivel_hambre = 0 desde fuera NO modifica el atributo real.
    #    Fuera de la clase no se aplica el name mangling, así que Python
    #    crea un atributo NUEVO llamado literalmente "__nivel_hambre".
    #    El real es _PersonajeTeletubby__nivel_hambre (name mangling) y se
    #    podría tocar con: po._PersonajeTeletubby__nivel_hambre = 0
    #    El mangling evita accidentes y colisiones; no es seguridad real.
    #
    # 2) En class Cyborg(Humano, Robot) se ejecuta la de HUMANO: el MRO busca
    #    de izquierda a derecha: [Cyborg, Humano, Robot, object].
    #    Se comprueba con Cyborg.mro() o Cyborg.__mro__.


# =============================================================================
# MAIN: descomenta el ejercicio que quieras probar
# =============================================================================
if __name__ == "__main__":
    ejercicio_1()
    ejercicio_4()
    ejercicio_5()
    # ejercicio_2()    # pide datos por teclado
    # ejercicio_3()    # pide datos por teclado