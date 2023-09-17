# 17. Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle
# deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis
# que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
# Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos
# (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de
# fome e tédio.

import random


class Tamagotchi:
    fazenda = []
    parte_dia = 0
    def __init__(self, id, nome='', fome=50, saude=50, idade = 0, tedio = 50):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        self.__tedio = tedio
        self.__comeu = False
        self.__brincou = False
        self.__cuidado = False
        self.id = id
    
    def __str__(self):
        return f'Id: {self.id}, \n\tNome: {self.nome}, \n\tFome: {self.fome}, \n\tSaude: {self.saude}, \n\tIdade: {self.idade}, \n\tTedio: {self.tedio}, \n\tComeu: {self.comeu}, \n\tBrincou: {self.brincou}, \n\tCuidado: {self.cuidado}'
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def fome(self):
        return self.__fome
    
    @fome.setter
    def fome(self, fome):
        self.__fome = fome

    @property
    def saude(self):
        return self.__saude
    
    @saude.setter
    def saude(self, saude):
        self.__saude = saude

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def tedio(self):
        return self.__tedio
    
    @tedio.setter
    def tedio(self, tedio):
        self.__tedio = tedio

    @property
    def comeu(self):
        return self.__comeu
    
    @comeu.setter
    def comeu(self, comeu):
        self.__comeu = comeu

    @property
    def brincou(self):
        return self.__brincou
    
    @brincou.setter
    def brincou(self, brincou):
        self.__brincou = brincou

    @property
    def cuidado(self):
        return self.__cuidado
    
    @cuidado.setter
    def cuidado(self, cuidado):
        self.__cuidado = cuidado

    def mostrar(self):
        return f'Id: {self.id}\n\tNome: {self.nome},\n\tFome: {self.fome:.2f}%,\n\tSaude: {self.saude:.2f}%,\n\tIdade: {self.idade:.2f},\n\tTedio: {self.tedio:.2f}%,\n\tHumor: {self.calcular_humor():.2f}%'
 
    def alterar_nome(self, nome):
        if(nome == ''):
            return
        self.nome = nome

    def alterar_fome(self, fome):
        if(fome > 100):
            self.fome = 100
            return
        elif(fome < 0):
            self.fome = 0
            return
        self.fome = fome

    def alterar_saude(self, saude):
        if(saude > 100):
            self.saude = 100
            return
        elif(saude < 0):
            self.saude = 0
            return
        self.saude = saude

    def alterar_idade(self, idade):
        if(idade < 0):
            self.idade = 0
            return
        self.idade = idade

    def aleterar_tedio(self, tedio):
        if(tedio > 100):
            self.tedio = 100
            return
        elif(tedio < 0):
            self.tedio = 0
            return
        self.tedio = tedio

    def alimentar(self, quantidade):
        alimentacao = self.fome + quantidade * 0.1
        self.alterar_fome(alimentacao)

    def brincar(self, tempo):
        tedio = self.tedio - tempo * 0.5
        self.aleterar_tedio(tedio)

    def cuidar(self, tempo):
        saude = self.saude + tempo * 0.5
        self.alterar_saude(saude)

    def ouvir(self, tempo):
        saude = self.saude + tempo * 0.25
        self.alterar_saude(saude)

        tedio = self.tedio - tempo * 0.25
        self.aleterar_tedio(tedio)

    def reduzir_propriedades(self):
        if (self.comeu):
            fome = self.fome - self.fome * 0.01
        else:
            fome = self.fome - self.fome * 0.05

        if(self.brincou):
            tedio = self.tedio + self.tedio * 0.01
        else:
            tedio = self.tedio + self.tedio * 0.05

        if(self.cuidado):
            saude = self.saude - self.saude * 0.01
        else:
            saude = self.saude - self.saude * 0.05
        
        if(self.comeu or self.brincou):
            saude = self.saude - self.saude * 0.01
        else:
            saude = self.saude - self.saude * 0.05
        
        self.alterar_fome(fome)
        self.aleterar_tedio(tedio)
        self.alterar_saude(saude)

    def calcular_humor(self):
        return (self.saude * 0.3 + self.fome * 0.3 + (100 - self.tedio) * 0.4)
    
    def criar_tamagotchi(self):
        self.nome = input('Digite o nome do Tamagotchi: ')
        self.fome = random.randint(0, 100)
        self.saude = random.randint(0, 100)
        self.tedio = random.randint(0, 100)
        self.fazenda.append(self)

def mostrar_todos():
    for tamagotchi in Tamagotchi.fazenda:
        print(tamagotchi.mostrar())
  
def retornar_um_tamagotchi(id):
    try:
        id = int(id)
    except:
        return None

    for tamagotchi in Tamagotchi.fazenda:
        if(tamagotchi.id == id):
            return tamagotchi

def validar_valor():
    valor = input('Digite um valor: ')
    try:
        valor = float(valor)
        return valor
    except:
        print('Valor inválido')
        return validar_valor()
    
while(True):
    print(f'\nBem vindo a fazenda de Tamagotchi, faltam {8 -  Tamagotchi.parte_dia} horas para o dia de trabalho acabar')
    opc = input('\n1 - Adicionar um tamagotchi\n2 - Ver todos os tamagotchis\n3 - Brincar com um tamagotchi\n4 - Alimentar um tamagotchi\n5 - Cuidar um tamagotchi\n6 - Ouvir um tamagotchi\n7 - Brincar com todos os tamagotchis\n8 - Alimentar todos os tamagotchis\n9 - Cuidar todos os tamagotchis\n10 - Ouvir todos os tamoagotchis\n11 - Sair\n\nDigite a opcao que deseja realizar: ')

    match opc:
        case '1':
            if(len(Tamagotchi.fazenda) == 0):
                novo_tamagotchi = Tamagotchi(1)
            else:
                novo_tamagotchi = Tamagotchi(Tamagotchi.fazenda[-1].id + 1)
            
            novo_tamagotchi.criar_tamagotchi()

        case '2':
            mostrar_todos()

        case '3':
            mostrar_todos()
            tamagotchi = retornar_um_tamagotchi(input('Digite o id do tamagotchi que deseja brincar: '))
            if(not tamagotchi):
                print('Tamagotchi não encontrado')
                continue
            print(f'Digite a quantidade de tempo que deseja brincar com {tamagotchi.nome} (em minutos):')
            tamagotchi.brincar(validar_valor())
            tamagotchi.brincou = True
            Tamagotchi.parte_dia += 0.5

        case '4':
            mostrar_todos()
            tamagotchi = retornar_um_tamagotchi(input('Digite o id do tamagotchi que deseja alimentar: '))
            if(not tamagotchi):
                print('Tamagotchi não encontrado')
                continue
            print(f'Digite a quantidade de comida que deseja dar a {tamagotchi.nome} (em gramas):')
            tamagotchi.alimentar(validar_valor())
            tamagotchi.comeu = True
            Tamagotchi.parte_dia += 0.5

        case '5':
            mostrar_todos()
            tamagotchi = retornar_um_tamagotchi(input('Digite o id do tamagotchi que deseja cuidar: '))
            if(not tamagotchi):
                print('Tamagotchi não encontrado')
                continue
            print(f'Digite a quantidade de tempo que deseja cuidar {tamagotchi.nome} (em minutos):')
            tamagotchi.cuidar(validar_valor())
            tamagotchi.cuidado = True
            Tamagotchi.parte_dia += 0.5

        case '6':
            mostrar_todos()
            tamagotchi = retornar_um_tamagotchi(input('Digite o id do tamagotchi que deseja ouvir: '))
            if(not tamagotchi):
                print('Tamagotchi não encontrado')
                continue
            print(f'Digite a quantidade de tempo que deseja ouvir {tamagotchi.nome} (em minutos):')
            tamagotchi.ouvir(validar_valor())
            tamagotchi.brincou = True
            tamagotchi.cuidado = True
            Tamagotchi.parte_dia += 0.5

        case '7':
            valor =  validar_valor(input('Digite a quantidade de tempo que deseja brincar com todos os tamagotchis (em minutos): '))
            for tamagotchi in Tamagotchi.fazenda:
                tamagotchi.brincar(valor)
                tamagotchi.brincou = True
                Tamagotchi.parte_dia += 1

        case '8':
            valor =  validar_valor(input('Digite a quantidade de comida que deseja dat a todos os tamagotchis (em gramas): '))
            for tamagotchi in Tamagotchi.fazenda:
                tamagotchi.alimentar(valor)
                tamagotchi.comeu = True
                Tamagotchi.parte_dia += 1

        case '9':
            valor =  validar_valor(input('Digite a quantidade de tempo que deseja cuidar todos os tamagotchis (em minutos): '))
            for tamagotchi in Tamagotchi.fazenda:
                tamagotchi.cuidar(valor)
                tamagotchi.cuidado = True
                Tamagotchi.parte_dia += 1

        case '10':
            valor =  validar_valor(input('Digite a quantidade de tempo que deseja ouvir todos os tamagotchis (em minutos): '))
            for tamagotchi in Tamagotchi.fazenda:
                tamagotchi.ouvir(valor)
                tamagotchi.brincou = True
                tamagotchi.cuidado = True
                Tamagotchi.parte_dia += 1

        case '11':
            break

        case 'a resposta é 42':
            for tamagotchi in Tamagotchi.fazenda:
                print(tamagotchi)

        case _:
            print('Opção inválida')

    if(Tamagotchi.parte_dia >= 8):
        Tamagotchi.parte_dia = 0
        for tamagotchi in Tamagotchi.fazenda:
            tamagotchi.reduzir_propriedades()