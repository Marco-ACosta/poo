from abc import ABC, abstractmethod
from random import randint
class entidade(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    @abstractmethod
    def atacar(self):
        pass
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def sofrer_dano(self):
        pass

class heroi(entidade):
    def __init__(self, nome, vida, defesa, classe):
        super().__init__(nome, vida)
        self.defesa = defesa
        self.classe = classe
    
    def mostrar(self):
        print('nome: ', self.nome)
        print('vida: ', self.vida)
        print('defesa: ', self.defesa)
    
    def atacar(self, arma):
        chance = randint(1, 20)
        if chance == 20:
            return arma.dano * 2
        if chance == 1:
            self.vida = arma.dano - (arma.dano * 0.1)
            return 0
        return arma.dano
    
    def sofrer_dano(self, dano):
        self.vida = self.vida + self.defesa - dano
    
class monstro(entidade):
    def __init__(self, nome, vida, defesa, especie):
        super().__init__(nome, vida)
        self.defesa = defesa
        self.especie = especie
    
    def mostrar(self):
        print('nome: ', self.nome)
        print('vida: ', self.vida)
        print('defesa: ', self.defesa)

    def atacar(self, arma):
        chance = randint(1, 20)
        if chance == 20:
            return arma.dano * 2
        if chance == 1:
            self.vida = arma.dano - (arma.dano * 0.05)
            return 0
        return arma.dano

    def sofrer_dano(self, dano):
        self.vida = self.vida + self.defesa - dano
    
class arma:
    def __init__(self, tipo, dano):
        self.tipo = tipo
        self.dano = dano


guerreiro = heroi('guerreiro', 100, 10, 'guerreiro')
orc = monstro('orc', 100, 10, 'orc')
espada = arma('espada', 10)
macharma = arma('machado', 20)
arco = arma('arco', 30)
tacape = arma('tacape', 40)
armas = [espada, macharma, arco, tacape]
combatentes = [guerreiro, orc]

turno = 0
while guerreiro.vida > 0 and orc.vida > 0:
    print('----------------')
    turno += 1
    print(f'turno: {turno}')
    print('MONSTRO:')
    orc.mostrar()
    print('HEROI:')
    guerreiro.mostrar()
    print('\n\n')
    dano_heroi = guerreiro.atacar(armas[randint(0, 3)])
    print('Dano Heroi', dano_heroi)
    orc.sofrer_dano(dano_heroi)

    dano_monstro = orc.atacar(armas[randint(0, 3)])
    print('Dano Monstro', dano_monstro)
    guerreiro.sofrer_dano(dano_monstro)
    print('----------------')
