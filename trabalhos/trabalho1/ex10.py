# 10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#   1. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#       1. tipoCombustivel.
#       2. valorLitro
#       3. quantidadeCombustivel
#   2. Possua no mínimo esses métodos:
#       1. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
#       quantidade de litros que foi colocada no veículo
#       2. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
#       mostra o valor a ser pago pelo cliente.
#       3. alterarValor( ) – altera o valor do litro do combustível.
#       4. alterarCombustivel( ) – altera o tipo do combustível.
#       5. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
# combustível total na bomba.

class Bomba:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_combustivel = quantidade_combustivel

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel
    
    @property
    def valor_litro(self):
        return self.__valor_litro
    
    @valor_litro.setter
    def valor_litro(self, valor_litro):
        self.__valor_litro = valor_litro
    
    @property
    def quantidade_combustivel(self):
        return self.__quantidade_combustivel
    
    @quantidade_combustivel.setter
    def quantidade_combustivel(self, quantidade_combustivel):
        self.__quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self):
        valor = input('Digite o valor a ser abastecido: ')
        try:
            valor = float(valor)
            litros_abastecidos = valor / self.valor_litro
            
            if(litros_abastecidos > self.quantidade_combustivel):
                print(f'Quantidade indisponível, atualmente restam {self.quantidade_combustivel} litros')
                self.abastecer_por_valor()

            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        
        except:
            print('Valor inválido')
            return self.abastecer_por_valor()
    
    def abastecer_por_litro(self):
        litros = input('Digite a quantidade de litros: ')
        try:
            litros = float(litros)

            if(litros > self.quantidade_combustivel):
                print(f'Quantidade indisponível, atualmente restam {self.quantidade_combustivel} litros')
                self.abastecer_por_litro()

            valor_abastecido = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            return valor_abastecido
        except:
            print('Valor inválido')
            return self.abastecer_por_litro()
        
    def alterar_valor(self):
        valor = input('Digite o valor do litro: ')
        try:
            valor = float(valor)
            self.valor_litro = valor
            return self.valor_litro
        
        except:
            print('Valor inválido')
            return self.alterar_valor()
    
    def alterar_combustivel(self):
        tipo_combustivel = input('Digite o tipo de combustível: ')
        self.tipo_combustivel = tipo_combustivel
        
        return self.tipo_combustivel
    
    def alterar_quantidade_combustivel(self):
        quantidade_combustivel = input('Digite a quantidade de combustível: ')
        try:
            quantidade_combustivel = float(quantidade_combustivel)
            self.quantidade_combustivel = quantidade_combustivel
            return self.quantidade_combustivel
        
        except:
            print('Valor inválido')
            return self.alterar_quantidade_combustivel()
        
bomba = Bomba('Gasolina', 10, 100)

while(True):
    print(f'O tipo de combustível é: {bomba.tipo_combustivel}\tValor do litro é: {bomba.valor_litro}\tA quantidade de combustível é: {bomba.quantidade_combustivel}')
    opc = input('1 - Abastecer por valor\n2 - Abastecer por litro\n3 - Alterar valor\n4 - Alterar combustível\n5 - Alterar quantidade de combustível\n6 - Sair\nDigite a opção desejada: ')
    match opc: 
        case '1':
            bomba.abastecer_por_valor()
        case '2':
            bomba.abastecer_por_litro()
        case '3':
            bomba.alterar_valor()
        case '4':
            bomba.alterar_combustivel()
        case '5':
            bomba.alterar_quantidade_combustivel()
        case '6':
            break
        case _:
            print('Opção inválida')



    
