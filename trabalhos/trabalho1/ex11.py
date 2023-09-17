# 11. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#   1. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
#   quantidade de combustível no tanque.
#   2. O consumo é especificado no construtor e o nível de combustível inicial é 0.
#   3. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
#   reduzindo o nível de combustível no tanque de gasolina.
#   4. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#   5. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
#   meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
#   meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
#   meuFusca.andar(100); # anda 100 quilômetros.
#   meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, consumo, combustivel=0):
        self.__consumo = consumo
        self.__combustivel = combustivel
    
    @property
    def consumo(self):
        return self.__consumo
    
    @consumo.setter
    def consumo(self, consumo):
        self.__consumo = consumo
    
    @property
    def combustivel(self):
        return self.__combustivel
    
    @combustivel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel
    
    def andar(self, distancia):
        consumo = self.consumo * distancia
        if(consumo > self.combustivel):
            return (f'Quantidade indisponível, atualmente restam {self.combustivel} litros no tanque, que é possível andar cerca de {self.combustivel / self.consumo:.2f} km')
        self.combustivel -= consumo

    def obter_gasolina(self):
        return self.combustivel
    
    def adicionar_gasolina(self, quantidade):
        self.combustivel += quantidade
        print(f'{quantidade} litros abastecidos')
    
carro = Carro(15)
while(True):
    opc = input('1 - andar\n2 - obter gasolina\n3 - adicionar gasolina\n4 - sair\nEscolha uma opção: ')
    match opc:
        case '1':
            carro.andar(float(input('Distancia: ')))
        case '2':
            print(f'Gasolina: {carro.obter_gasolina()}')
        case '3':
            carro.adicionar_gasolina(float(input('Quantidade: ')))
        case '4':
            break
        case _:
            print('Opção inválida')
