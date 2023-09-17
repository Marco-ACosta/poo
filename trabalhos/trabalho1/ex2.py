# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
    @property
    def lado(self):
        return self.__lado
    @lado.setter
    def lado(self, lado):
        self.__lado = lado
    def calcular_area(self):
        return self.__lado ** 2
    
quadrado = Quadrado(5)
print(quadrado.lado)
print(quadrado.calcular_area())
quadrado.lado = 10
print(quadrado.lado)
print(quadrado.calcular_area())