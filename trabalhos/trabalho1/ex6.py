# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário
# deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de
# que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self, canal=1, volume=50):
        self.__canal = canal
        self.__volume = volume
    
    @property
    def canal(self):
        return self.__canal
    
    @canal.setter
    def canal(self, canal):
        self.__canal = canal

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def validar_valor(self):
        valor = input('Digite um valor: ')
        try:
            valor = int(valor)
            return valor
        except:
            print('Valor inválido')
            return self.validar_valor()
        
    def trocar_canal(self, canal):
        self.canal = canal

    def aumentar_volume(self, volume):
        if (self.volume + volume > 100):
            self.volume = 100
            return
        self.volume += volume

    def diminuir_volume(self, volume):
        if(self.volume - volume < 0):
            self.volume = 0
            return
        
        self.volume -= volume

televisor = TV()
while(True):
    print(f'Televisor\tCanal: {televisor.canal}\tVolume: {televisor.volume}')
    opc = input('\n\t1 - Trocar Canal\n\t2 - Aumentar Volume\n\t3 - Diminuir Volume\n\t4 - Sair\n\tDigite a opção desejada fazer:')
    match opc:
        case '1':
            print('Digite o número do canal:')
            canal = televisor.validar_valor()
            televisor.trocar_canal(canal)
        case '2':
            print('Digite o quanto quer aumentar o volume:')
            volume = televisor.validar_valor()
            televisor.aumentar_volume(volume)
        case '3':
            print('Digite o quanto quer diminuir o volume:')
            volume = televisor.validar_valor()
            televisor.diminuir_volume(volume)
        case '4':
            break
        case _:
            print('Opção inválida')