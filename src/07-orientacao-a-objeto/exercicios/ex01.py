""" Exercício 01 - classe Aluno """


class Aluno:
    def __init__(self, prontuario, nome, email):
        self.nome = nome
        self.prontuario = prontuario
        self.email = email

    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(sep=',')
        return cls(prontuario, nome, email)

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
        if self.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo nome")
        else:
            self._nome = value

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if self.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo prontuário")
        else:
            self._prontuario = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo email")
        else:
            self._email = value

    def __str__(self):
        return f'Aluno[nome={self.nome}, prontuario={self.prontuario}, email={self.email}]'
    
    def esta_vazio(self, value):
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


aluno1 = Aluno.from_string('SP0101,João,joao@email.com')
aluno2 = Aluno.from_string('SP0101,João,joao@email.com')
aluno3 = Aluno.from_string('SP0102,Ana Luisa,analu@email.com')

print(aluno1)
print(aluno2)
print(aluno3)
print('Aluno 1 e 2 são iguais:', aluno1 == aluno2)
