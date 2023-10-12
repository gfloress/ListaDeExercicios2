class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def imprimir_menu():
    print("\nMenu:")
    print("1 - Alterar ponto inicial do retângulo")
    print("2 - Alterar largura do retângulo")
    print("3 - Alterar altura do retângulo")
    print("4 - Calcular e mostrar centro do retângulo")
    print("0 - Sair")


# Função principal
ponto_inicial = Ponto(0, 0)
largura = 0
altura = 0

while True:
    imprimir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        x = int(input("Digite a coordenada x do ponto inicial: "))
        y = int(input("Digite a coordenada y do ponto inicial: "))
        ponto_inicial = Ponto(x, y)
    elif escolha == "2":
        largura = int(input("Digite a largura do retângulo: "))
    elif escolha == "3":
        altura = int(input("Digite a altura do retângulo: "))
    elif escolha == "4":
        retangulo = Retangulo(ponto_inicial, largura, altura)
        centro = retangulo.encontrar_centro()
        print("Centro do retângulo:")
        centro.imprimir()
    elif escolha == "0":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
