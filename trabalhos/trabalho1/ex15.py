# 15. Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário
# especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o
# bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class Tamagotchi:
    def __init__(self, nome='', fome=50, saude=50, idade = 0, tedio = 50):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        self.__tedio = tedio
    
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

    def mostrar(self):
        return f'''Nome: {self.nome}, \tFome: {self.fome:.2f}%, \tSaude: {self.saude:.2f}%, \tIdade: {self.idade:.2f}, \tTedio: {self.tedio:.2f}%, \tHumor: {self.calcular_humor():.2f}%'''
    
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

    def reduzir_propriedades(self, alimentado, brincou, cuidado ):
        if (alimentado):
            fome = self.fome - self.fome * 0.01
        else:
            fome = self.fome - self.fome * 0.05

        if(brincou):
            tedio = self.tedio + self.tedio * 0.01
        else:
            tedio = self.tedio + self.tedio * 0.05

        if(cuidado):
            saude = self.saude - self.saude * 0.01
        else:
            saude = self.saude - self.saude * 0.05
        
        if(alimentado or brincou):
            saude = self.saude - self.saude * 0.01
        else:
            saude = self.saude - self.saude * 0.05
        
        self.alterar_fome(fome)
        self.aleterar_tedio(tedio)
        self.alterar_saude(saude)

    def calcular_humor(self):
        return (self.saude * 0.3 + self.fome * 0.3 + (100 - self.tedio) * 0.4)
    
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
    tamagotchi_brincou = tamagotchi_alimentado = tamagotchi_cuidado = False
    print(tamagotchi.mostrar())

    opc = input(f'Digite a opção desejada:\n\t1 - Alterar nome\n\t2 - Alimentar {tamagotchi.nome}\n\t3 - Brincar com {tamagotchi.nome}\n\t4 - Cuidar de {tamagotchi.nome}\n\t5 - Sair\n\t: ')
    match opc:
        case '1':
            nome = input('Digite o novo nome: ')
            tamagotchi.alterar_nome(nome)
        case '2':
            print(f'Digite a quantidade de comida que deseja dar a {tamagotchi.nome} (em gramas):')
            tamagotchi.alimentar(tamagotchi.validar_valor())
            tamagotchi_alimentado = True
        case '3':
            print(f'Digite a quantidade de tempo que deseja brincar com {tamagotchi.nome} (em minutos):')
            tamagotchi.brincar(tamagotchi.validar_valor())
            tamagotchi_brincou = True
        case '4':
            print(f'Digite a quantidade de tempo que deseja cuidar de {tamagotchi.nome} (em minutos):')
            tamagotchi.cuidar(tamagotchi.validar_valor())
            tamagotchi_cuidado = True
        case '5':
            break
        case _:
            print('Opção inválida')
        
    if(opc >= '1' and opc <= '4'):
        tamagotchi.reduzir_propriedades(tamagotchi_alimentado, tamagotchi_brincou, tamagotchi_cuidado)
        tamagotchi.alterar_idade(tamagotchi.idade + 0.1)
    