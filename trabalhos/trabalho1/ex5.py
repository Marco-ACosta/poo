# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
# seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero
# e os demais atributos são obrigatórios.

import random


class ContaCorrente:
    def __init__(self, numero_conta, titular, saldo=0):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
    
    ##Titular
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def numero_conta(self):
        return self.__numero_conta
    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta
    
    ##Saldo
    @property
    def saldo(self):
        return self.__saldo

    def _deposito(self, valor):
        self.__saldo += valor

    def _saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

print('Bem vindo ao essebanconaofazsentidobank!\npara começar a usar nossos serviços, faça seu cadastro rápido')
nome = input('Digite seu nome: ')
numero_conta = random.randint(1000, 9999)
print(f'Numero da conta será: {numero_conta}')
conta = ContaCorrente(numero_conta, nome)
while(True):
    print(f'Dados da conta:\nNumero da conta: {conta.numero_conta}\tTitular: {conta.titular}\tSaldo: {conta.saldo}')
    opc = input('O que deseja fazer?\n1 - Depositar\n2 - Sacar\n3 - Alterar nome\n4 - Sair\n')
    match opc:
        case '1':
            valor = float(input('Digite o valor a ser depositado: '))
            conta._deposito(valor)
        case '2':
            valor = float(input('Digite o valor a ser sacado: '))
            conta._saque(valor)
        case '3':
            conta.titular = input('Digite o novo nome: ')
        case '4':
            print('Saindo...')
            break
        case _:
            print('Opção inválida')
        
