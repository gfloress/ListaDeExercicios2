class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            # A cada ano que a pessoa envelhece, e a idade é menor que 21 anos, ela cresce 0.5 cm
            self.altura += 0.5 * anos

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

pessoa = Pessoa(nome="Alice", idade=18, peso=60, altura=165)

print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso, "kg")
print("Altura:", pessoa.altura, "cm")

# Simulando a passagem de um ano e verificando o crescimento
pessoa.envelhecer(1)

print("\nDepois de um ano:")
print("Idade:", pessoa.idade)
print("Altura:", pessoa.altura, "cm")

# Simulando ganho de peso e altura
pessoa.engordar(5)
pessoa.crescer(2)

print("\nDepois de ganhar peso e altura:")
print("Peso:", pessoa.peso, "kg")
print("Altura:", pessoa.altura, "cm")
