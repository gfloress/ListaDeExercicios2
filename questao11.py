class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  # consumo em km/l
        self.combustivel = 0  # nível de combustível em litros

    def andar(self, distancia):
        autonomia = self.combustivel * self.consumo
        if distancia <= autonomia:
            self.combustivel -= distancia / self.consumo
            print(f"O carro percorreu {distancia} km.")
        else:
            print("Combustível insuficiente para percorrer a distância desejada.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros
        print(f"Foram adicionados {litros} litros de gasolina ao tanque.")

meu_carro = Carro(consumo=10)  # consumo de 10 km/l

meu_carro.adicionarGasolina(50)  # abastece 50 litros de gasolina
print("Nível de combustível:", meu_carro.obterGasolina(), "litros")

meu_carro.andar(200)  # percorre 200 km
print("Nível de combustível:", meu_carro.obterGasolina(), "litros")

meu_carro.andar(600)  # tenta percorrer 600 km, mas não tem combustível suficiente
print("Nível de combustível:", meu_carro.obterGasolina(), "litros")
