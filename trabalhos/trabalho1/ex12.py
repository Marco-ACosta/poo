# 12. Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe
# contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor
# que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem
# parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
# poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o
# método adicioneJuros() cinco vezes e imprime o saldo resultante.


class ContaInvestimento:
    def __init__(self,numero_conta, titular, saldo=0, taxa_juros=0):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__taxa_juros = taxa_juros
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def taxa_juros(self):
        return self.__taxa_juros

    def adicione_juros(self):
        self.saldo += self.saldo * self.taxa_juros/100

conta_investimento = ContaInvestimento(1234, 'Marco', 1000, 10)

conta_investimento.adicione_juros()
conta_investimento.adicione_juros()
conta_investimento.adicione_juros()
conta_investimento.adicione_juros()
conta_investimento.adicione_juros()
print(conta_investimento.saldo)
