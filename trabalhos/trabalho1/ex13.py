# 13. Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string)
# e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
# para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    def mostrar(self):
        return f'Nome: {self.__nome}, Salário: {self.__salario}'

functionario = Funcionario('João', 1000)
print(functionario.mostrar())

functionario2 = Funcionario('Maria', 2000)
print(functionario2.mostrar())

functionario3 = Funcionario('Pedro', 3000)
print(functionario3.mostrar())

