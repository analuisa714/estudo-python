""" Aula 02 - Atributos de classe e instância """

from classes.pessoa import pessoa02 as pessoa

pessoa1 = pessoa.Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = pessoa.Pessoa('João Santos', 'joao@email.com')
pessoa3 = pessoa.Pessoa('Pedro Santos', 'joao@email.com')


pessoa1.especie = 'Alienígena'


pessoa.Pessoa.especie = 'Alienígenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)


print(pessoa.Pessoa.especie)
