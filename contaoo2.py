class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo: {self.__saldo} do titular {self.__titular} na conta {self.__numero}")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Valor depositado: {valor}")

    def sacar(self, valor):
        if valor <= self.__saldo + self.__limite:
            self.__saldo -= valor
            print(f"Valor retirado: {valor}")
        else:
            print("Saldo insuficiente para o saque.")

    def transferir(self, valor, destino):
        if valor <= self.__saldo + self.__limite:
            self.sacar(valor)
            destino.depositar(valor)
            print(f"Transferência de {valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente para a transferência.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite