# 6. Crie uma classe Dado que simule um dado de seis lados. Implemente um
# método para lançar o dado e mostrar o resultado. Crie um loop para lançar o
# dado 5 vezes e exibir os resultados.

import random


class Dado:
    def __init__(self, lados = 6):
        self.lados = lados
    
    def lancar(self):
        return random.randint(1, self.lados)
    
for i in range(5):
    print(f'{i+1}º lançamento: {Dado().lancar()}')