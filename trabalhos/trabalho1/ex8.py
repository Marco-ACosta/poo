# 8. Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho
# (estômago) e, pelo menos, os métodos comer(), verBucho() e digerir(). Faça um programa ou
# teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3
# alimentos diferentes e verificando o conteúdo do estômago a cada refeição. Experimente fazer
# com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
        print(f"{self.nome} comeu {comida}.")

    def verBucho(self):
        if len(self.bucho) > 0:
            print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}")
        else:
            print('estômago vazio.')

    def digerir(self):
        if len(self.bucho) > 0:
            print(f"{self.nome} está digerindo {', '.join(self.bucho)}.")
            self.bucho = []
        else:
            print('estômago vazio.')

macaco1 = Macaco("Twelves")
macaco2 = Macaco("Cesar")

macaco1.comer('Banana')
macaco2.comer('Banana')

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer('Carne')
macaco2.comer('Carne')

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer('Pão')
macaco2.comer('Pão')

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()
