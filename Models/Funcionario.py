class Funcionario(object):
    def __init__(self, id_funcionario, nome, cargo, salario):
        self._id_funcionario = id_funcionario
        self._nome = nome
        self._cargo = cargo
        self._salario = salario

    def calcular_salario(self): #retornar o salario atual do funcionario
        pass

    def atualizar_cargo(self, novo_cargo): #Mudar o cardo do funcionario
        pass
