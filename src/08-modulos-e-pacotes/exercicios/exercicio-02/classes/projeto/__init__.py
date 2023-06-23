""" Classe projeto """

import uteis

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.titulo = titulo
        self.codigo = codigo
        self.responsavel = responsavel
        self.participacoes = []

    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(sep=',')
        return cls(codigo, titulo, responsavel)

    def __str__(self):
        return f'Projeto[titulo={self.titulo}, codigo={self.codigo}, responsavel={self.responsavel}]'

    def __repr__(self):
        return f'Projeto({self.codigo},{self.titulo},{self.responsavel})'

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def print_participacoes(self):
        for participacao in self.participacoes:
            print(participacao, end='\n\n')

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if uteis.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo título")
        else:
            self._titulo = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if uteis.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo código")
        elif (not value.isdigit()) or (value == '0'):
            raise ValueError(
                "Digite apenas números interos positivos para o campo código")
        else:
            self._codigo = int(value)

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if uteis.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo responsável")
        else:
            self._responsavel = value
