""" Classe Telefone """

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero
    
    def __str__(self) -> str:
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'