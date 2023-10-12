class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")

conta = ContaCorrente(numero_conta="123456", nome_correntista="Alice", saldo=1000)

print(f"Número da conta: {conta.numero_conta}")
print(f"Nome do correntista: {conta.nome_correntista}")
print(f"Saldo: R${conta.saldo:.2f}")

conta.alterarNome("Bob")
print(f"Novo nome do correntista: {conta.nome_correntista}")

conta.deposito(500)
print(f"Saldo após depósito: R${conta.saldo:.2f}")

conta.saque(200)
print(f"Saldo após saque: R${conta.saldo:.2f}")
