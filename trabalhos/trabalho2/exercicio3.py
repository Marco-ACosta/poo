from abc import ABC, abstractmethod


class produto(ABC):
    def __init__(self, preco):
        self.preco = preco
    
    @abstractmethod
    def calcular_preco(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

class voo(produto):
    def __init__(self, origem, destino, data, assento, preco = 0):
        super().__init__(preco)
        self.origem = origem
        self.destino = destino
        self.data = data
        self.assento = assento

    def calcular_preco(self, classe, distancia):
        self.preco = classe * distancia
        return self.preco
    
    def mostrar(self):
        print(f'origem: {self.origem}, destino: {self.destino}, data: {self.data}, assento: {self.assento}, preco: {self.preco}')

class hotel(produto):
    def __init__(self, endereco, tipo, diaria, preco = 0):
        super().__init__(preco)
        self.endereco = endereco
        self.tipo = tipo
        self.diaria = diaria
    
    def calcular_preco(self, dias, classe):
        self.preco = dias * self.diaria * classe
        return self.preco
    
    def mostrar(self):
        print(f'endereco: {self.endereco}, tipo: {self.tipo}, preco: {self.preco}')

class pacote_de_viagem(produto):
    def __init__(self, voo: voo, hotel: hotel, preco = 0):
        super().__init__(preco)
        self.voo = voo
        self.hotel = hotel

    
    def calcular_preco(self, dias, distancia, classe_voo, classe_hotel):
        preco = self.voo.calcular_preco(classe_voo, distancia) + self.hotel.calcular_preco(dias, classe_hotel)
        self.preco = preco - (preco * 0.1)
        return self.preco
    
    def mostrar(self):
        print('pacote de viagem:')
        print('Voo')
        self.voo.mostrar()
        print('Hotel')
        self.hotel.mostrar()
        print(f'preco: {self.preco}, obs, ao contratar esse pacote você tem 10% de desconto')

voo_ = voo('SP', 'RJ', '10/10/2020', 'A1', 100)
hotel_ = hotel('rua 1', 'luxo', 100)
pacote_ = pacote_de_viagem(voo_, hotel_)

print(pacote_.calcular_preco(10, 100, 2, 3))
pacote_.mostrar()