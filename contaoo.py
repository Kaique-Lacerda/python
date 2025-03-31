class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrair_saldo(self):
        print(f"Seu saldo é: {self.saldo}, do titular {self.titular}")
        
    def deposita(self, valor):
        self.saldo += valor
        print(f"Deposito de {valor} realizado com sucesso!")
        self.extrair_saldo()