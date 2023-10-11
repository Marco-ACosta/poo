from abc import ABC, abstractmethod


class mamifero(ABC): 
    @abstractmethod
    def som(self):
        print('som')

class homem(mamifero):
    def som(self):
        print('oi')

class cachorro(mamifero):
    def som(self):
        print('auuuu')

class gato(mamifero):
    def som(self):
        print('miau')


# mamifero = mamifero()
# mamifero.som()

animais = [homem(), cachorro(), gato()]

for animal in animais:
    animal.som()
