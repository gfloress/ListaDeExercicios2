class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

# Exemplo de uso da classe Funcionario
funcionario1 = Funcionario(nome="Alice", salario=50000.0)
funcionario2 = Funcionario(nome="Bob", salario=60000.0)

print("Nome do funcionário 1:", funcionario1.obterNome())
print("Salário do funcionário 1:", funcionario1.obterSalario())

print("Nome do funcionário 2:", funcionario2.obterNome())
print("Salário do funcionário 2:", funcionario2.obterSalario())
