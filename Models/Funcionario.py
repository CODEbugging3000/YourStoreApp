class Funcionario:
    def __init__(self, id_funcionario, nome, cargo, salario):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_salario(self): # Retornar o salario atual do funcionario
        return f"O salário atual do {self.nome} é R${self.salario:.2f}"

    def atualizar_cargo(self, novo_cargo): # Mudar o cargo do funcionario
        cargo_antigo = self.cargo
        self.cargo = novo_cargo
        return f"Cargo de {self._nome} foi atualizado de {cargo_antigo} para {novo_cargo}"
