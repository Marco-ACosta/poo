# 3. Crie uma classe chamada ContaBancaria com o atributo saldo.
# Implemente métodos para depositar e sacar dinheiro, considerando a
# lógica para evitar saques com saldo insuficiente. Crie um objeto da
# classe e realize operações de depósito e saque.

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo < valor:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
    def mostrar(self):
        return self.saldo

conta = ContaBancaria(0)
conta.depositar(100)
conta.sacar(50)
print(conta.saldo)
conta.sacar(100)
print(conta.saldo)