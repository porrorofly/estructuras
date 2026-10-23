class Teletubbies:
    def __init__(self,nombre,color,antena,objeto_favorito):
        self.nombre=nombre
        self.color=color
        self.antena=antena
        self.objeto_favorito=objeto_favorito
        self.saludo_oficial="!Tubby abrazo¡"
        self.__nivel_hambre=50
        self.__nivel_felicidad=100
    def saludar(self):
        return f"Hola, soy {self.nombre} tengo {self.color} de piel!!! Y mi antena es {self.antena}"
    def jugar(self):
        print(f"{self.nombre} está jugando con {self.objeto_favorito}")
        self.__nivel_hambre+=20
        self.__nivel_felicidad+=10
    def comer_tubby_papilla(self):
        self.__nivel_hambre==0
        self.__nivel_felicidad+=20
        print(f"{self.nombre} está comiendo")
    def ver_estado(self):
        return f"{self.nombre} tiene Felicidad {self.__nivel_felicidad} y de hambre {self.__nivel_hambre}"
    def __str__(self):
        return f"{self.nombre,self.color,self.antena}"