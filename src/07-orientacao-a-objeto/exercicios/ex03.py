""" Exercício 03 - classe Participacao """


def esta_vazio(value):
    ATRIBUTO_INVALIDO = True

    if len(value) != 0:
        for caractere in value:
            if caractere != " ":
                ATRIBUTO_INVALIDO = False
        if ATRIBUTO_INVALIDO:
            return ATRIBUTO_INVALIDO
        else:
            return False
    else:
        return ATRIBUTO_INVALIDO


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
        if esta_vazio(value):
            raise ValueError(
                'Não foi atribuído algum valor ao campo "data de início"')
        else:
            self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):
        if esta_vazio(value):
            raise ValueError(
                'Não foi atribuído algum valor ao campo "data de encerramento" ')
        else:
            self._data_fim = value

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, value):
        if not isinstance(value, Aluno):
            raise ValueError(
                'Não foi atribuído algum aluno ao campo "aluno"')
        else:
            self._aluno = value

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, value):
        if not isinstance(value, Projeto):
            raise ValueError(
                'Não foi atribuído algum projeto ao campo "projeto"')
        else:
            self._projeto = value


class Aluno:
    def __init__(self, prontuario, nome, email):
        self.nome = nome
        self.prontuario = prontuario
        self.email = email

    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(sep=',')
        return cls(prontuario, nome, email)

    def __repr__(self):
        return f'Aluno({self.prontuario},{self.nome},{self.email})'

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo nome")
        else:
            self._nome = value

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo prontuário")
        else:
            self._prontuario = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo email")
        else:
            self._email = value

    def __str__(self):
        return f'Aluno[nome={self.nome}, prontuario={self.prontuario}, email={self.email}]'


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.titulo = titulo
        self.codigo = codigo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(sep=',')
        return cls(codigo, titulo, responsavel)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo título")
        else:
            self._titulo = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if esta_vazio(value):
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
        if esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo responsável")
        else:
            self._responsavel = value

    def __str__(self):
        return f'Projeto[titulo={self.titulo}, codigo={self.codigo}, responsavel={self.responsavel}]'

    def __repr__(self):
        return f'Projeto({self.codigo}, {self.titulo}, {self.responsavel})'


aluno1 = Aluno.from_string('SP0101,João,joao@email.com')

projeto1 = Projeto.from_string(
    '1,Laboratório de Desenvolvimento de Software,Pedro Gomes')

participacao = Participacao(
    1, '10/11/2023', '10/03/2024', aluno1, projeto1)
print(participacao)
