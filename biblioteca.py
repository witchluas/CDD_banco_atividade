class Banco:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            print(f"DEPÓSITO CONCLUÍDO, seu novo saldo é R${self.saldo}")
        else:
            print("Sua conta está desativada. Ative sua conta antes de depositar.")

    def sacar(self, valor):
        if self.status:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"SAQUE EFETUADO, você sacou R${valor}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Sua conta está desativada. Ative sua conta antes de sacar.")

    def ativarconta(self):
        if not self.status:
            self.status = True
            print("Parabéns, sua conta foi ativada com sucesso!")
        else:
            print("Sua conta já estava ativada.")

    def desativarconta(self):
        if self.status:
            self.status = False
            print("Sua conta está desativada.")
        else:
            print("Sua conta já estava desativada.")

    def verificarsaldo(self):
        if self.status:
            print(f"Saldo da conta de R${self.nome}: {self.saldo}")
        else:
            print("Sua conta está desativada. Ative sua conta para verificar o saldo.")

    def definirlimite(self, creditospecial):
        self.limite = creditospecial
        if self.status:
            self.limite = creditospecial
            print(f"LIMITE DE CRÉDITO ESPECIAL DEFINIDO: R${creditospecial}")
        else:
            print("Sua conta está desativada. Ative sua conta antes de definir o limite de crédito especial.")


