class Perro:
    def sonido(self):
        print("GAF GAF")
class Gato:
    def sonido(self):
        print("MIAU MIAU")
class Vaca:
    def sonido(self):
        print("MUUUUU")
def oir_sonido(animales):
    for animal in animales:
        animal.sonido()

granja=[Perro(),Gato(),Vaca()]
oir_sonido(granja)