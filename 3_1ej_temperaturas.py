tem=float(input("Introduce la temperatura en grados centígrados: "))
if 18<=tem<=27:
    print("La temperatura es optima")
elif tem>27:
    print("ALERTA CALOR")
elif tem<18:
    print("ALERTA FRIO")