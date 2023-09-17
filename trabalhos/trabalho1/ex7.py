# Classe Bichinho Virtual: Crie uma classe que modele um Tamagotchi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
# Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em
# consideração, o Humor do nosso Tamagotchi, este humor é uma combinação entre os atributos
# Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
# armazenar esta informação por que ela pode ser calculada a qualquer momento.

class Tamagotchi:
    def __init__(self, nome='', fome=50, saude=50, idade = 0):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
    
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

    def mostrar(self):
        return f'''Nome: {self.nome}, \tFome: {self.fome}%, \tSaude: {self.saude}%, \tIdade: {self.idade}, \tHumor: {self.calcular_humor()}%'''
    
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

    def calcular_humor(self):
        return (self.saude+self.fome)/2
    
    def validar_valor(self):
        valor = input('Digite um valor: ')
        try:
            valor = float(valor)
            return valor
        except:
            print('Valor inválido')
            return self.validar_valor()
    
    def criar_tamagotchi(self):
        self.nome = input('Digite o nome do Tamagotchi: ')

tamagotchi = Tamagotchi()
tamagotchi.criar_tamagotchi()
while(True):
    print(tamagotchi.mostrar())
    opc = input('Digite a opção desejada:\n\t1 - Alterar nome\n\t2 - Alterar fome\n\t3 - Alterar saude\n\t4 - Alterar idade\n\t5 - Sair\n\t: ')
    match opc:
        case '1':
            nome = input('Digite o novo nome: ')
            tamagotchi.alterar_nome(nome)
        case '2':
            tamagotchi.alterar_fome(tamagotchi.validar_valor())
        case '3':
            tamagotchi.alterar_saude(tamagotchi.validar_valor())
        case '4':
            tamagotchi.alterar_idade(tamagotchi.validar_valor())
        case '5':
            break
        case _:
            print('Opção inválida')
    