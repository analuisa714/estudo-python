""" Classe Pessoa """

class Pessoa:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa({self.cpf},{self.nome})'
    