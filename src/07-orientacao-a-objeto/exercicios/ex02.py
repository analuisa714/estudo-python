""" Exercício 02 - classe Projeto """

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
        if self.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo título")
        else:
            self._titulo = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if self.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo código")
        elif (not value.isdigit()) or (value=='0'):
            raise ValueError(
                "Digite apenas números interos positivos para o campo código")
        else:
            self._codigo = int(value)

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if self.esta_vazio(value):
            raise ValueError(
                "Não foi atribuído algum valor para o campo responsável")
        else:
            self._responsavel = value

    def __str__(self):
        return f'Projeto[titulo={self.titulo}, codigo={self.codigo}, responsavel={self.responsavel}]'
    
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


projeto1 = Projeto.from_string('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto2 = Projeto.from_string('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto3 = Projeto.from_string('2,Monitoria,Maria')

print(projeto1)
print(projeto2)
print(projeto3)
print('Projeto 1 e 2 são iguais:', projeto1 == projeto2)
