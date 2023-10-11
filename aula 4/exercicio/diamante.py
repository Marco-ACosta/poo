class atleta:
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso
    
    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        self.peso = self.peso - 0.1


class nadador(atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def nadar(self):
        print('nadando')

class corredor(atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def correr(self):
        print('correndo')

class ciclista(atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def pedalar(self):
        print('pedalando')


class tri_atleta(corredor, nadador, ciclista):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    


tri_at = tri_atleta(True, 80)

tri_at.pedalar()
tri_at.correr()
tri_at.nadar()