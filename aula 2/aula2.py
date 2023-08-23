class conta:
    def __init__(self, titular, saldo, limite, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        self.limite = limite
    
    def mostrar(self):
        return (f''' Titular: {self.titular},\n Saldo: {self.saldo},\n Limite: {self.limite},\n Numero: {self.numero}\n''')

    def depositar(self, valor):
        self.saldo += valor

cc = conta('Marco', 500, 1000, 123)

print(cc.mostrar())
cc.depositar(100)
print(cc.mostrar())

