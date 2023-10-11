from abc import ABC, abstractmethod
from random import randint


class Veiculo(ABC):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def listarVerificacoes(self):
        pass

    @abstractmethod
    def ajustar(self):
        pass

    @abstractmethod
    def limpar(self):
        pass

class Bicicleta(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)
    
    def listarVerificacoes(self):
        print('a bicicleta foi verificada')
    
    def ajustar(self):
        print('a bicicleta foi ajustada')
    
    def limpar(self):
        print('a bicicleta foi limpa')
    
class Automovel(Veiculo):

    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)

    def listarVerificacoes(self):
        print('o automovel foi verificado')
    
    def ajustar(self):
        print('o automovel foi ajustado')
    
    def limpar(self):
        print('o automovel foi limpo')

    def mudarOleo(self):
        print('o automovel teve o seu oleo trocado')

class oficina:
    def proximo(self, veiculos: []):
        return veiculos[ randint(0, len(veiculos) - 1)]
    
    def manutencao(self, veiculo: Veiculo):
        veiculo.listarVerificacoes()
        veiculo.ajustar()
        veiculo.limpar()
        if(isinstance(veiculo, Automovel)):
            veiculo.mudarOleo()
        print('Manutenção do veiculo feita com sucesso')


carro = Automovel('Gol', 2019)
bike = Bicicleta('Gol', 2019)
veic = oficina().proximo([carro, bike])
oficina().manutencao(veic)