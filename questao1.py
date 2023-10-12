class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

minha_bola = Bola(cor="vermelha", circunferencia=10, material="couro")
print("Cor da bola:", minha_bola.mostraCor())  # Saída: Cor da bola: vermelha

minha_bola.trocaCor("azul")
print("Nova cor da bola:", minha_bola.mostraCor())  # Saída: Nova cor da bola: azul
