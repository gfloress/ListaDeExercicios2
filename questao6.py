class TV:
    def __init__(self):
        self.canal = 1  # Canal inicial
        self.volume = 50  # Nível de volume inicial

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("Canal inválido")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo")


# Programa principal
minha_tv = TV()

while True:
    print("\n\tCONTROLE REMOTO DA TV")
    print("1 - Mudar Canal")
    print("2 - Aumentar Volume")
    print("3 - Diminuir Volume")
    print("0 - Desligar TV")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_canal = int(input("Digite o número do canal (1-100): "))
        minha_tv.mudarCanal(novo_canal)
    elif opcao == "2":
        minha_tv.aumentarVolume()
    elif opcao == "3":
        minha_tv.diminuirVolume()
    elif opcao == "0":
        print("TV desligada. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
