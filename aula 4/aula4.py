# Herança 

class Veiculo:
    def andar(self):
        print ('Andando')
class Carro(Veiculo):
    _nrodas = 4

gol = Carro()
gol.andar()


class Animal:
    def __init__(self, fome, saude):
        self.fome = fome
        self.saude = saude

class Mamifero(Animal):
    def __init__(self, fome, saude, idade):
        super().__init__(fome, saude)
        self.idade = idade
    
class Ave(Animal):
    def __init__(self, fome, saude, idade):
        super().__init__(fome, saude)
        self.idade = idade

class Gaviao(Ave):
    def __init__(self, fome, saude, idade):
        super().__init__(fome, saude, idade)

class Cuica(Ave):
    def __init__(self, fome, saude, idade):
        super().__init__(fome, saude, idade)

class Cachorro(Mamifero):
    def __init__(self, fome, saude, idade):
        super().__init__(fome, saude, idade)

class Gato(Mamifero):
    def __init__(self, fome, saude, idade):
        super().__init__(fome, saude, idade)

# EXERCICIO

class Aluno:
    def __init__(self, g1, g2):
        self._g1 = g1
        self._g2 = g2
        self._media = 0

    def calcularMedia(self):
        self._media = (self._g1 + self._g2) / 2
    
class AlunoG(Aluno):
    def __init__(self, g1, g2, g3):
        super().__init__(g1, g2)
        self._g3 = g3

    def calcularMedia(self):
        self._media = (self._g1 + self._g2 + self._g3) / 3

class AlunoP(Aluno):
    def __init__(self, g1, g2, g3, g4):
        super().__init__(g1, g2)
        self._g3 = g3
        self._g4 = g4

    def calcularMedia(self):
        self._media = (self._g1 + self._g2 + self._g3 + self._g4) / 4


teste = AlunoG(1, 2, 3)
teste.calcularMedia()
print(teste._media)

teste = AlunoP(1, 2, 3, 4)
teste.calcularMedia()
print(teste._media)

# Exercicio 2
# Crie uma classe chamada Forma, que possui os atributos area e perimetro.
# Implemente as subclasses retangulo e triangulo que devem conter os métodos calculaArea e calculaPerimetro. A classe triangulo deve ter também o atributo altura.
# No código de teste crie um objeto classe triangulo e outro da classe retangulo verifique se os dois sao mesmo instancias de forma use instanceof e calcule a area de cada um

class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0
    
class Retangulo(Forma):
    def __init__(self, altura, largura):
        super().__init__()
        self.altura = altura
        self.largura = largura
    
    def calcular_area(self):
        self.area = self.altura * self.largura
    
    def calcular_perimetro(self):
        self.perimetro = (self.altura + self.largura) * 2
    
class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        self.area = self.base * self.altura / 2
    
    def calcular_perimetro(self):
        self.perimetro = self.base * 3

    
triangulo = Triangulo(3, 4)

triangulo.calcular_area()

triangulo.calcular_perimetro()

print(triangulo.area, triangulo.perimetro)
print(isinstance(triangulo, Forma ))

retangulo = Retangulo(3, 4)

retangulo.calcular_area()

retangulo.calcular_perimetro()

print(retangulo.area, retangulo.perimetro)
print(isinstance(retangulo, Forma ))