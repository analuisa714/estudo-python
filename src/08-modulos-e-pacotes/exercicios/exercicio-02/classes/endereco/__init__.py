""" Classe Endereco """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self) -> str:
        return f'Cep[cep={self.cep}, numero={self.numero}]'
    