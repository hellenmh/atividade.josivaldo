class Conta():
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"o salvo atual de conta {self.numero} e de r$ {self.saldo}")
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"o saldo atual de conta {self.numero} e de R$ {self.saldo}")
        else:
            print("saldo insuficiente")
    def mostrar(self):
        print(f"o saldo atual da conta {self.numero} e de R$ {self.saldo}")
if __name__ == "__main__":
    conta1 = Conta(1234, "edril", 1000)
    conta1.depositar(1240)
    conta1.sacar (200)
    conta1.mostrar