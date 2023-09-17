# Retangulo: Faça um programa completo utilizando funções e classes que:
# 1. Possua uma classe chamada Ponto, com os atributos x e y.
# 2. Possua uma classe chamada Retangulo, com os atributos largura e altura.
# 3. Possua uma função para imprimir os valores da classe Ponto
# 4. Possua uma função para encontrar o centro de um Retângulo.
# 5. Você deve criar alguns objetos da classe Retangulo.
# 6. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
# retângulo, que deve ser um objeto da classe Ponto.
# 7. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
# ponto que indique os valores de x e y para o centro do objeto.
# 8. O valor do centro do objeto deve ser mostrado na tela
# 9. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
    
    def imprimir_valores(self):
        print(f'x:{self.x} y:{self.y}')

class Retangulo:
    retangulos = []
    def __init__(self, id, altura=0, largura=0):
        self.__id = id
        self.__altura = altura
        self.__largura = largura
        self.__vertice_inicial = Ponto(0, 0)

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

    @property
    def vertice_inicial(self):
        return self.__vertice_inicial.x, self.__vertice_inicial.y

    @property
    def id(self):
        return self.__id

    def calcular_meio(self):
        (self.meio_x, self.meio_y) = (self.largura / 2, self.altura / 2)
        return self.meio_x, self.meio_y
    
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
    
    def imprimir_valores (self):
        return f'Id: {self.id} Altura: {self.altura} Largura: {self.largura}'

def mostrar_retangulos():
    for retangulo in Retangulo.retangulos:
        print(retangulo.imprimir_valores())

def definir_id():
    id = input('Digite o id do retangulo: ')
    try:
        id = int(id)
        return id
    except:
        print('Valor inválido')
        return definir_id()

while(True):
    opc = input('\n1 - Adicionar um retangulo\n2 - Mostrar todos retangulos \n3 - Calcular centro de um retangulo\n4 - Mudar altura de um retangulo\n5 - Mudar largura de um retangulo\n6 - Sair\nDigite a opção que deseja realizar: ')
    match opc:
        case '1':
            if(len(Retangulo.retangulos) == 0):
                Retangulo.retangulos.append(Retangulo(1))
                Retangulo.retangulos[0].definir_retangulo()
            else:
                Retangulo.retangulos.append(Retangulo(Retangulo.retangulos[-1].id + 1))
                Retangulo.retangulos[-1].definir_retangulo()

        case '2':
            mostrar_retangulos()

        case '3':
            print('Qual retangulo deseja ver o centro?')
            mostrar_retangulos()
            id = definir_id()
            i = False

            for retangulo in Retangulo.retangulos:
                if(retangulo.id == id):
                    (x, y) = retangulo.calcular_meio()
                    ponto = Ponto(x, y)
                    ponto.imprimir_valores()
                    ponto = None
                    i = True
            id = None
            if(not i):
               print('Nenhum retangulo encontrado')

        case '4':
            print('Qual retangulo deseja mudar a altura?')
            mostrar_retangulos()
            id = definir_id()
            i = False
    
            for retangulo in Retangulo.retangulos:
                if(retangulo.id == id):
                    retangulo.definir_altura()
                    i = True

            id = None
            if(not i):
                print('Nenhum retangulo encontrado')

        case '5':
            print('Qual retangulo deseja mudar a largura?')
            mostrar_retangulos()
            id = definir_id()
            i = False

            for retangulo in Retangulo.retangulos:
                if(retangulo.id == id):
                    retangulo.definir_largura()
                    i = True

            id = None
            if(not i):
                print('Nenhum retangulo encontrado')

        case '6':
            print('Saindo...')
            break

        case _:
            print('Opção inválida')