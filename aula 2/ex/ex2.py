# 2. Crie uma classe chamada Calculadora com métodos para adição,
# subtração, multiplicação e divisão de números. Crie um objeto dessa
# classe e realize operações básicas com valores informados pelo usuário.

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def soma(self):
        return self.num1 + self.num2
    def subtracao(self):
        return self.num1 - self.num2
    def multiplicacao(self):
        return self.num1 * self.num2
    def divisao(self):
        return self.num1 / self.num2

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
calculadora = Calculadora(num1, num2)
print(f'Soma: {calculadora.soma()}')
print(f'Subtração: {calculadora.subtracao()}')
print(f'Multiplicação: {calculadora.multiplicacao()}')
print(f'Divisão: {calculadora.divisao()}')