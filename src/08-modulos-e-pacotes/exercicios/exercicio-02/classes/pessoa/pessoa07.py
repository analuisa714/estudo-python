""" Classe Pessoa """

class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_enderecos(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}]'
    