# 8. Crie uma classe ContadorPalavras que conte a quantidade de palavras em uma frase
# informada pelo usuário. Implemente um método que receba a frase e retorne o número
# de palavras.

class ContadorPalavras:
    def __init__(self, frase):
        self.frase = frase
    def contar(self):
        return len(self.frase.split(' '))
    
contador = ContadorPalavras(input('Digite uma frase: '))
print(f'Quantidade de palavras: {contador.contar()}')