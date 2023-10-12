class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        if self.bucho:
            print(f"Bucho de {self.nome}: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está de bucho vazio")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para digerir.")

macaco1 = Macaco("Macaco A")
macaco2 = Macaco("Macaco B")

while True:
    print("\nMenu:")
    print("1 - Alimentar Macaco A")
    print("2 - Alimentar Macaco B")
    print("3 - Ver Bucho do Macaco A")
    print("4 - Ver Bucho do Macaco B")
    print("5 - Digerir Macaco A")
    print("6 - Digerir Macaco B")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        alimento = input("Digite o alimento para Macaco A: ")
        macaco1.comer(alimento)
    elif escolha == "2":
        alimento = input("Digite o alimento para Macaco B: ")
        macaco2.comer(alimento)
    elif escolha == "3":
        macaco1.verBucho()
    elif escolha == "4":
        macaco2.verBucho()
    elif escolha == "5":
        macaco1.digerir()
    elif escolha == "6":
        macaco2.digerir()
    elif escolha == "0":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
