from abc import ABC, abstractmethod


class evento(ABC):
    def __init__(self, nome, data, aluguel, custo):
        self.nome = nome
        self.data = data
        self.aluguel = aluguel
        self.custo = custo
    
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def calcular_custo(self):
        pass


class palestra(evento):
    def __init__(self, nome, data, aluguel, palestrante, entrada, ouvintes, valor_palestrante, custo = 0):
        super().__init__(nome, data, aluguel, custo)
        self.palestrante = palestrante
        self.valor_palestrante = valor_palestrante
        self.entrada = entrada
        self.ouvintes = ouvintes
    

    def mostrar(self):
        print('nome: ', self.nome)
        print('data: ', self.data)
        print('custo: ', self.custo)

    
    def calcular_custo(self):
        custo = (self.ouvintes * self.entrada) - (self.aluguel + self.valor_palestrante)
        self.custo = custo

class workshop(evento):
    def __init__(self, nome, data, aluguel, valor_workshop, alunos, custo = 100):
        super().__init__(nome, data, aluguel, custo)
        self.valor_workshop = valor_workshop
        self.alunos = alunos
    
    def calcular_custo(self):
        custo = (self.valor_workshop * self.alunos) - self.aluguel
        self.custo = custo

    def mostrar(self):
        print('nome: ', self.nome)
        print('data: ', self.data)
        print('custo: ', self.custo)


workshop_ = workshop('workshop', '2022-01-01', 100, 100, 3)
palestra_ = palestra('palestra', '2022-01-01', 100, 'palestrante', 10, 10, 100)
eventos = [workshop_, palestra_]

for evento_ in eventos:
    evento_.calcular_custo()
    evento_.mostrar()      