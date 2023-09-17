# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa
# pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome='', idade=0, peso=0, altura=0):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def envelhecer(self, anos):
        while(self.idade < 21):
            self.idade += 1
            self.crescer(0.5)
            anos -= 1
        self.idade += anos

    def crescer(self, cm):
        self.altura += cm

    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        if(self.peso - kg <= 0 ):
            return(f'Peso não pode ser igual ou menor que 0')
        
        self.peso -= kg
    
    def validar_valor_flutuante(self):
        valor = input('Digite o valor: ')
        try:
            valor = float(valor)
            return valor
        except:
            print('Valor inválido')
            return self.validar_valor_flutuante()
    
    def validar_valor_inteiro(self):
        valor = input('Digite o valor: ')
        try:
            valor = int(valor)
            return valor
        except:
            print('Valor inválido')
            return self.validar_valor_inteiro()
    
    def inserir_dados(self):
        self.nome = input('Inisira o seu nome: ')
        print('Informe sua idade em anos:')
        self.idade = self.validar_valor_inteiro()
        print('Informe seu peso em kg:')
        self.peso = self.validar_valor_flutuante()
        print('Informe sua altura em cm:')
        self.altura = self.validar_valor_flutuante()

pessoa = Pessoa()
pessoa.inserir_dados()

while(True):
    print(f'Dados da pessoa:\tNome: {pessoa.nome}\tIdade: {pessoa.idade}\tPeso: {pessoa.peso}\tAltura: {pessoa.altura}\tIdade: {pessoa.idade}\n')
    opc = input ('\t1 - Envelhecer\n\t2 - Engordar\n\t3 - Emagrecer\n\t4 - Crescer\n\t5 - Sair\n\nDigite a opção que deseja realizar: ')
    match opc:
        case '1':
            print('Informe quantos anos deseja envelhecer: ')
            anos = pessoa.validar_valor_inteiro()
            pessoa.envelhecer(anos)
        case '2':
            print('Informe quantos kg deseja engordar: ')
            kg = pessoa.validar_valor_flutuante()
            pessoa.engordar(kg)
        case '3':
            print('Informe quantos kg deseja emagrecer: ')
            kg = pessoa.validar_valor_flutuante()
            pessoa.emagrecer(kg)
        case '4':
            print('Informe quantos cm deseja crescer: ')
            cm = pessoa.validar_valor_flutuante()
            pessoa.crescer(cm)
        case '5':
            break
        case _:
            print('Opção inválida')