class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            print("Quantidade de combustível insuficiente na bomba.")
            return 0

    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            return valor_pagar
        else:
            print("Quantidade de combustível insuficiente na bomba.")
            return 0

    def alterarValor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

bomba = BombaCombustivel(tipo_combustivel="Gasolina", valor_litro=5.50, quantidade_combustivel=1000)

print("Bomba de Combustível")
print("Tipo de Combustível:", bomba.tipo_combustivel)
print("Valor por Litro: R$", bomba.valor_litro)
print("Quantidade de Combustível: ", bomba.quantidade_combustivel, "litros")

bomba.alterarValor(5.70)
bomba.alterarCombustivel("Álcool")
bomba.alterarQuantidadeCombustivel(1500)

print("\nApós alterações:")
print("Tipo de Combustível:", bomba.tipo_combustivel)
print("Valor por Litro: R$", bomba.valor_litro)
print("Quantidade de Combustível: ", bomba.quantidade_combustivel, "litros")

abastecidos = bomba.abastecerPorValor(50)
print("\nLitros abastecidos:", abastecidos)
print("Quantidade de Combustível após abastecimento: ", bomba.quantidade_combustivel, "litros")

valor_pagar = bomba.abastecerPorLitro(15)
print("\nValor a ser pago: R$", valor_pagar)
print("Quantidade de Combustível após abastecimento: ", bomba.quantidade_combustivel, "litros")
