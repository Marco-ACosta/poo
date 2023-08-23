# 4. Crie uma classe Tarefa com os atributos descrição e status (concluída ou
# não). Crie uma lista de objetos Tarefa e implemente métodos para adicionar,
# listar e marcar tarefas como concluídas. Teste os métodos interagindo com o
# usuário.

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.status = 'pendente'
    def marcar(self):
        self.status = 'concluída'
    def mostrar(self):
        return (f'''Descrição: {self.descricao},\n Status: {self.status}\n''')
    def listar(self, tarefas):
        print('Tarefas:\n')
        n = 1
        for tarefa in tarefas:
            print(f'{n} - {tarefa.mostrar()}\n\n')
            n += 1
        
    
tarefas = []

while(True):
    
    opc = input(f'''\nDigite a opção que pretende realizar: \n1 - Adicionar tarefa \n2 - Listar tarefas \n3 - Marcar tarefa como concluída \n4 - Sair\n''')
    match opc:
        case '1':
            tarefa = input('Digite uma tarefa: ')
            if (tarefa != ''):
                tarefas.append(Tarefa(tarefa))
                print('Tarefa adicionada com sucesso!')
            else:
                print('Tarefa vazia')
        case '2':
            tarefas[0].listar(tarefas)
        case '3':
            print('Digite a tarefa que pretende marcar como concluída:')
            tarefas[0].listar(tarefas)
            marcar = int(input())
            if(not marcar > len(tarefas)+1 or not marcar < 0):
                tarefas[marcar-1].marcar()
                print('Tarefa marcada como concluída!')
            print('Tarefa inexistente')

        case '4':
            print('Adeus e obrigado pelos peixes!')
            break

        case _:
            print('Opção inválida')