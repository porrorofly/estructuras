nombre=(input("Ingrese su nombre: ")).strip().lower()
cp=(input("Ingrese su código postal: ")).strip()
if len(nombre)==0:
    print("El nombre no puede estar vacío.")
    nombre=(input("Ingrese su nombre: ")).strip()
elif len(str(cp))!=5 or not cp.isdigit():
    print("El código postal debe tener 5 dígitos y ser numérico.")
    cp=(input("Ingrese su código postal: ")).strip()
#if not nombre:
#    print("El nombre no puede estar vacío.")

else:
    print(f"Registro válido - Nombre: {nombre}, Código Postal: {cp}")
