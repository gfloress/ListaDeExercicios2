class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros

# Criando uma conta de investimento com saldo inicial de R$1000,00 e taxa de juros de 10%
conta = ContaInvestimento(saldo_inicial=1000, taxa_juros=10)

# Aplicando o método adicioneJuros() cinco vezes
for _ in range(5):
    conta.adicioneJuros()

# Imprimindo o saldo resultante
print("Saldo após aplicar juros:")
print("R$", conta.saldo)
