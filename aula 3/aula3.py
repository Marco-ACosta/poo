class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome # publico -> todos acessam
        self._idade = idade # privado -> apenas essa classe acessa 
        self.__cpf = cpf # protegido -> apenas essa classe acessa e seus filhos

    def get_idade(self): # metodo getter -> consegue acessar atributos, protegidos e privados
        return self._idade
    def set_idade(self, idade): # metodo setter -> consegue escrever/modificar atributos, protegidos e privados
        self._idade = idade

class Aluno:

    def __init__(self):
        self._g1 = 0
        self._g2 = 0
        self._media = 0
    
    def _get_notas(self):
        return self._g1, self._g2
    
    def _set_g1(self, g1):
        self._g1 = g1
    def _set_g2(self, g2):
        self._g2 = g2

    def define_g1(self):
        g1 = input('Digite a nota da g1: ')
        try:
            g1 = float(g1)
            self._set_g1(g1)
        except:
            print('Valor inválido')
            self._define_g1()
    
    def define_g2(self):
        g2 = input('Digite a nota da g2: ')
        try:
            g2 = float(g2)
            self._set_g2(g2)
        except:
            print('Valor inválido')
            self._define_g2()
    
    def set_media(self):
        g1, g2 = self._get_notas()
        self.media = (g1 + g2) / 2
    def get_media(self):
        return self.media

    

aluno = Aluno()
aluno.define_g1()
aluno.define_g2()
aluno.set_media()
print(aluno._get_media())