# 9. Crie uma classe Livro com os atributos titulo, autor e ano. Crie uma lista de objetos Livro
# e implemente métodos para adicionar livros e listar todos os livros cadastrados. Interaja
# com o usuário para realizar essas ações.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    def mostrar(self):
        return (f'''Titulo: {self.titulo},\n Autor: {self.autor},\n Ano: {self.ano}\n''')
    def listar(self, livros):
        print('Livros:\n')
        n = 0
        for livro in livros:
            n += 1
            print(f'{n} - {livro.mostrar()}\n\n')
livros = []
while(True):
    opc = input(f'''\nDigite a opção que pretende realizar: \n1 - Adicionar livro \n2 - Listar livros \n3 - Sair\n''')
    match opc:
        case '1':
            titulo = input('Digite o titulo: ')
            autor = input('Digite o autor: ')
            ano = int(input('Digite o ano: '))
            livro = Livro(titulo, autor, ano)
            livros.append(livro)
            print('Livro adicionado com sucesso!')
        case '2':
            livros[0].listar(livros)
        case '3':
            print('Adeus e obrigado pelos peixes!')
            break
        case _:
            print('Opção inválida')