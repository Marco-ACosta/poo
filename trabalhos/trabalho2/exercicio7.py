from abc import ABC, abstractmethod

class gerenciavel(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class projeto(gerenciavel):
    def __init__(self, nome, tarefas: []):
        self.nome = nome
        self.tarefas = tarefas
    
    def concluir_tarefa(self, nome_tarefa):
        for tarefa in self.tarefas:
            if tarefa.nome == nome_tarefa:
                tarefa.concluido = True
                for recurso in tarefa.recursos:
                    if recurso.quantidade < 0:
                        recurso.quantidade -= 1
        
    def mostrar(self):
        print(f'Nome: {self.nome}')
        concluidas = 0
        for tarefa in self.tarefas:
            tarefa.mostrar()
            if tarefa.concluido:
                concluidas += 1
        print(f'{(concluidas/len(self.tarefas)) * 100:.2f}% concluído')

class tarefa(gerenciavel):
    def __init__(self, nome, descricao, recursos:[]):
        self.nome = nome
        self.descricao = descricao
        self.recursos = recursos
        self.concluido = False
    
    def concluir_tarefa(self):
        self.concluido = True
    
    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Descrição: {self.descricao}')
        print(f'Concluído: {self.concluido}')
        for recurso in self.recursos:
            recurso.mostrar()

class recurso(gerenciavel):
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Quantidade: {self.quantidade}')

recurso1 = recurso('Recurso 1', 10)
recurso2 = recurso('Recurso 2', 20)

tarefa1 = tarefa('Tarefa 1', 'Descrição da tarefa 1', [recurso1, recurso2])
tarefa2 = tarefa('Tarefa 2', 'Descrição da tarefa 2', [recurso2])
tarefa3 = tarefa('Tarefa 3', 'Descrição da tarefa 3', [recurso1])

projeto1 = projeto('Projeto 1', [tarefa1, tarefa2, tarefa3])
projeto1.mostrar()
projeto1.concluir_tarefa('Tarefa 1')
projeto1.concluir_tarefa('Tarefa 2')
projeto1.mostrar()

elementos = [recurso1, tarefa1, projeto1]

for elemento in elementos:
    elemento.mostrar()
