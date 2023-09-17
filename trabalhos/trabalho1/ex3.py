# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de
# um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de
# rodapés necessárias para o local.

class Retangulo: 
    def __init__(self, altura=0, largura=0):
        self.__altura = altura
        self.__largura = largura
    
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    @property
    def largura(self):
        return self.__largura
    @largura.setter
    def largura(self, largura):
        self.__largura = largura
    
    def calcular_area(self):
        area = self.__altura * self.__largura
        return area
    
    def calcular_perimetro(self):
        perimetro = (self.__altura + self.__largura) * 2
        return perimetro

    def definir_altura(self):
        altura = input('Digite a altura: ')
        try:
            self.altura = float(altura)
        except:
            print('Valor inválido')
            return self.definir_altura()
    
    def definir_largura(self):
        largura = input('Digite a largura: ')
        try:
            self.largura = float(largura)
        except:
            print('Valor inválido')
            return self.definir_largura()

    def definir_retangulo (self):
        self.definir_largura() 
        self.definir_altura()

local = Retangulo()
azuleijo = Retangulo()
rodape = Retangulo()
print('Vamos definir as medidas do local')
local.definir_retangulo()
while(True):
    print(f'Medidas do local:\nAltura: {local.altura}\nLargura: {local.largura}\nArea: {local.calcular_area()}\nPerimetro: {local.calcular_perimetro()}')
    opc = input('\n1 - Editar altura\n2 - Editar largura\n3 - Definir medida dos azuleijos\n4 - Definir medidas dos rodapés\n5 - Calcular total de azuleijos para preencher a área total do local\n6 - Calcular total de rodapés para preencher o permímetro do local\n7 - Sair\nDigite a opção que deseja realizar:')
    match opc:
        case '1':
            local.definir_altura()
        case '2':
            local.definir_largura()
        case '3':
            azuleijo.definir_retangulo()
        case '4':
            azuleijo.definir_retangulo()
        case '5':
            area_local = local.calcular_area()
            area_azuleijo = azuleijo.calcular_area()
            print(f'Total de azuleijos necessários para preencher a área total do local: {area_local/area_azuleijo:.2f}')
        case '6':
            perimetro_local = local.calcular_perimetro()
            print(f'Total de rodapés necessários para preencher o perímetro do local: {perimetro_local/rodape.largura:.2f}')
        case '7':
            break
        case _:
            print('Opção inválida')