# 5. Crie uma classe Pessoa com os atributos nome, idade e email. Crie uma lista
# de objetos Pessoa e implemente métodos para adicionar pessoas, listar todas
# as pessoas cadastradas e buscar por idade. Interaja com o usuário para
# realizar essas ações.

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def mostrar(self):
        return (f''' Nome: {self.nome},\n Idade: {self.idade},\n Email: {self.email}\n''')
    def listar(self, pessoas):
        print('Pessoas:\n')
        n = 0
        for pessoa in pessoas:
            n += 1
            print(f'{n} - {pessoa.mostrar()}\n\n')
    def localizar(self, pessoas, idade):
        print('Pessoas:\n')
        n = 0
        for pessoa in pessoas:
            if(pessoa.idade == idade):
                n += 1
                print(f'{n} - {pessoa.mostrar()}\n\n')
        if(n == 0):
            print('Idade inexistente')

pessoas = []

while(True):
    opc = input(f'''\nDigite a opção que pretende realizar: \n1 - Adicionar pessoa \n2 - Listar pessoas \n3 - Localizar pessoa \n4 - Sair\n''')
    match opc:
        case '1':
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            email = input('Digite o email: ')
            pessoa = Pessoa(nome, idade, email)
            pessoas.append(pessoa)
            print('Pessoa adicionada com sucesso!')
        case '2':
            pessoas[0].listar(pessoas)
        case '3':
            idade = int(input('Digite a idade: '))
            pessoas[0].localizar(pessoas, idade)
        case '4':
            print('Adeus e obrigado pelos peixes!')
            break
        case _:
            print('Opção inválida')