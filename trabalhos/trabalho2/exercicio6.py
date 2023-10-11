from abc import ABC, abstractmethod
from random import randint

class faixa:
    def __init__(self, faixa, veiculos:[]):
        self.faixa = faixa
        self.veiculos = veiculos
    
    def mostrar(self):
        print('\nfaixa: ', self.faixa)
        for veiculo in self.veiculos:
            print('----------------------------')
            veiculo.mostrar()

class veiculo(ABC):
    def __init__(self, modelo, marca, placa, velocidade, aceleracao, faixa):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.velocidade = velocidade
        self.aceleracao = aceleracao
        self.faixa = faixa
    @abstractmethod
    def acelerar(self):
        pass
    @abstractmethod
    def frenar(self):
        pass
    @abstractmethod
    def mudar_faixa(self):
        pass
    @abstractmethod
    def ultrapassar(self):
        pass
    @abstractmethod
    def mostrar(self):
        pass

class carro(veiculo):
    def __init__(self, modelo, marca, placa, velocidade, aceleracao, faixa):
        super().__init__(modelo, marca, placa, velocidade, aceleracao, faixa)
    def acelerar(self):
        self.velocidade += self.aceleracao
    def frenar(self):
        self.velocidade -= self.aceleracao
    def mudar_faixa(self, faixa):
        self.faixa.veiculos.remove(self)
        self.faixa = faixa
        faixa.veiculos.append(self)
    def ultrapassar(self):
        posicao = self.faixa.veiculos.index(self)
        if posicao != 0:
            self.faixa.veiculos[posicao], self.faixa.veiculos[posicao - 1] = self.faixa.veiculos[posicao - 1], self.faixa.veiculos[posicao]
    def mostrar(self):
        print('modelo: ', self.modelo)
        print('marca: ', self.marca)
        print('placa: ', self.placa)
        print('velocidade: ', self.velocidade)
        print('aceleracao: ', self.aceleracao)
    
class moto(veiculo):
    def __init__(self, modelo, marca, placa, velocidade, aceleracao, faixa):
        super().__init__(modelo, marca, placa, velocidade, aceleracao, faixa)
    def acelerar(self):
        self.velocidade += self.aceleracao
    def frenar(self):
        self.velocidade -= self.aceleracao
    def mudar_faixa(self, faixa):
        self.faixa.veiculos.remove(self)
        self.faixa = faixa
        faixa.veiculos.append(self)
    def ultrapassar(self):
        posicao = self.faixa.veiculos.index(self)
        if posicao != 0:
            self.faixa.veiculos[posicao], self.faixa.veiculos[posicao - 1] = self.faixa.veiculos[posicao -1], self.faixa.veiculos[posicao]
    def mostrar(self):
        print('modelo: ', self.modelo)
        print('marca: ', self.marca)
        print('placa: ', self.placa)
        print('velocidade: ', self.velocidade)

class caminhao(veiculo):
    def __init__(self, modelo, marca, placa, velocidade, aceleracao, faixa):
        super().__init__(modelo, marca, placa, velocidade, aceleracao, faixa)
    def acelerar(self):
        self.velocidade += self.aceleracao
    def frenar(self):
        self.velocidade -= self.aceleracao
    def mudar_faixa(self, faixa):
        self.faixa.veiculos.remove(self)
        self.faixa = faixa
        faixa.veiculos.append(self)
    def ultrapassar(self):
        posicao = self.faixa.veiculos.index(self)
        if posicao != 0:
            self.faixa.veiculos[posicao], self.faixa.veiculos[posicao - 1] = self.faixa.veiculos[posicao - 1], self.faixa.veiculos[posicao]
    def mostrar(self):
        print('modelo: ', self.modelo)
        print('marca: ', self.marca)
        print('placa: ', self.placa)
        print('velocidade: ', self.velocidade)
faixa1 = faixa(1, [])
faixa2 = faixa(2, [])
faixa3 = faixa(3, [])

carro1 = carro('gol', 'volkswagen', 'abc1234', 0, 10, faixa1)
carro2 = carro('palio', 'volkswagen', 'abc1234', 0, 20, faixa1)
moto1 = moto('bis', 'honda', 'abc1234', 0, 10, faixa2)
moto2 = moto('civic', 'honda', 'abc1234', 0, 20, faixa2)
caminhao1 = caminhao('volks', 'volkswagen', 'abc1234', 0, 10, faixa3)
caminhao2 = caminhao('palio', 'volkswagen', 'abc1234', 0, 20, faixa3)
veiculos = [carro1, carro2, moto1, moto2, caminhao1, caminhao2]
faixas = [faixa1, faixa2, faixa3]

for veiculo_ in veiculos:
    veiculo_.mostrar()
    veiculo_.acelerar()
    veiculo_.acelerar()
    veiculo_.frenar()
    veiculo_.mudar_faixa(faixas[randint(0, 2)])
    veiculo_.ultrapassar()
    veiculo_.faixa.mostrar()

