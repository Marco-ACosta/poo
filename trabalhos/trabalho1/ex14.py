# 14. Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
# (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
# harry=funcionário("Harry",25000)
# harry.aumentarSalario(10)

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

    def aumentar_salario(self, porcentual_aumento):
        self.__salario += self.__salario * porcentual_aumento / 100


marco =  Funcionario('Marco', 1000)
print(marco.mostrar())
marco.aumentar_salario(10)
print(marco.mostrar())
marco.aumentar_salario(10)
print(marco.mostrar())
marco.aumentar_salario(10)
print(marco.mostrar())