# 1. Crie uma classe chamada Aluno com os atributos nome, idade e nota.
# Em seguida, crie dois objetos dessa classe, preenchendo os atributos, e
# exiba as informações dos alunos na tela.

class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    def mostrar(self):
        return (f''' Nome: {self.nome},\n Idade: {self.idade},\n Nota: {self.nota}\n''')

aluno1 = Aluno('José', 19, 8.5)
aluno2 = Aluno('Maria', 18, 7.5)
print(aluno1.mostrar())
print(aluno2.mostrar())
