class Coche:
    ruedas=4
    def __init__(self,color ,aceleracion):
        self.aceleracion=aceleracion
        self.color=color
        self.velocidad=0
    def acelera(self):
        self.velocidad+=self.aceleracion
class CocheVolador(Coche):
    ruedas=6
    def __init__(self, color, aceleracion,esta_volando=False):
        super().__init__(color, aceleracion)
        self.esta_volando=esta_volando
    def vuela(self):
        self.esta_volando=True
cv1=CocheVolador("Verde",100)
cv1.acelera()
print(cv1.esta_volando)
# Verificación explícita de tipos con isinstance e issubclass
print("¿cv1 es instancia de CocheVolador ?: ", isinstance(cv1, CocheVolador)) # True
print("¿cv1 es instancia de Coche ?: ", isinstance(cv1, Coche))#True
print("¿CocheVolador es subclase de Coche ?: ", issubclass (Coche, CocheVolador)) # True
print("¿CocheVolador es subclase de Coche ?: ", issubclass (Coche, CocheVolador)) # False