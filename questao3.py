class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

# Programa principal
print("Informe as medidas do local:")
comprimento = float(input("Comprimento do local em metros: "))
largura = float(input("Largura do local em metros: "))

local = Retangulo(comprimento, largura)

area_local = local.calcularArea()
perimetro_local = local.calcularPerimetro()

# Suponha que o tamanho do piso seja 1 metro por 1 metro
tamanho_piso = 1  # em metros

# Calculando a quantidade de pisos necessários
quantidade_pisos = area_local / tamanho_piso

# Suponha que o rodapé tenha 10 centímetros de altura
altura_rodape = 0.1  # em metros

# Calculando a quantidade de rodapés necessários
perimetro_rodape = perimetro_local * altura_rodape
quantidade_rodapes = perimetro_rodape / tamanho_piso

print(f"Área do local: {area_local} metros quadrados")
print(f"Perímetro do local: {perimetro_local} metros")
print(f"Quantidade de pisos necessários: {quantidade_pisos} peças")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes} peças")
