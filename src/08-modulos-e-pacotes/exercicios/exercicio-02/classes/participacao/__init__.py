""" Classe Participacao """

from classes import aluno, projeto
import uteis

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto_associado):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto_associado = projeto_associado

    def __str__(self):
        return f'Participacao[codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno}, projeto_associado={self.projeto_associado}]'

    @classmethod
    def from_string(cls, rep_participacao):
        codigo, data_inicio, data_fim, aluno, projeto_associado = rep_participacao.split(
            sep=',')
        return cls(codigo, data_inicio, data_fim, aluno, projeto_associado)

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value <= 0:
            raise ValueError(
                "Digite apenas números interos positivos para o campo código")
        else:
            self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        if uteis.esta_vazio(value):
            raise ValueError(
                'Não foi atribuído algum valor ao campo "data de início"')
        else:
            self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):
        if uteis.esta_vazio(value):
            raise ValueError(
                'Não foi atribuído algum valor ao campo "data de encerramento" ')
        else:
            self._data_fim = value

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, value):
        if not isinstance(value, aluno.Aluno):
            raise ValueError(
                'Não foi atribuído algum aluno ao campo "aluno"')
        else:
            self._aluno = value

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, value):
        if not isinstance(value, projeto.Projeto):
            raise ValueError(
                'Não foi atribuído algum projeto ao campo "projeto"')
        else:
            self._projeto = value
    
    def __repr__(self):
        return f'Participacao({self.codigo},{self.data_inicio},{self.data_fim},{self.aluno},{self.projeto_associado})'

