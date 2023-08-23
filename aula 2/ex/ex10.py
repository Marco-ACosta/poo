# 10. Crie uma classe LancamentoDados que simule o lançamento de dois dados de seis
# lados. Implemente um método para lançar os dados e mostrar a soma dos resultados. Crie
# um loop para realizar 3 lançamentos e exibir as somas.

import random


class LancamentoDados:
    def __init__(self, lados=6):
        self.lados = lados

    def lancar(self):
        return random.randint(1, self.lados)
    
    def lancar2(self):
        dado1 = self.lancar()
        dado2 = self.lancar()
        print(f'Dado 1: {dado1}\nDado 2: {dado2}\nSoma: {dado1 + dado2}\n\n')

for i in range(3):
    LancamentoDados().lancar2()

        