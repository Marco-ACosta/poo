# 7. Crie uma classe ConversorMoedas que converta valores entre real e dólar, considerando
# uma taxa fixa. Implemente métodos para conversão de real para dólar e vice-versa.
# Interaja com o usuário para realizar as conversões.

class ConversorMoedas:
    def __init__(self, taxa):
        self.taxa = taxa
    def real_para_dolar(self, valor):
        return valor / self.taxa
    def dolar_para_real(self, valor):
        return valor * self.taxa
def definir_taxa():
    taxa = input('Digite a taxa de conversão: ')
    try:
        taxa = float(taxa)
        return taxa
    except:
        print('Valor inválido')
        return definir_taxa()
    

taxa = definir_taxa()
conversor = ConversorMoedas(taxa)
while(True):   
    opc = input('Digite a opção que pretende realizar: \n1 - Real para Dólar \n2 - Dólar para Real\n')
    match opc:
        case '1':
            valor = input('Digite o valor a ser convertido: ')
            try:
                valor = float(valor)
                print(f'{valor} reais equivalem a {conversor.real_para_dolar(valor)} dólares')
            except:
                print('Valor inválido')
                valor = 0
        case '2':
            valor = input('Digite o valor a ser convertido: ')
            try:
                valor = float(valor)
                print(f'{valor} dólares equivalem a {conversor.dolar_para_real(valor)} reais')
            except:
                print('Valor inválido')
                valor = 0
                
        case _:
            print('Opção inválida')
