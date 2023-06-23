""" Aula 06 - equals e hash code """

from classes.pessoa import pessoa06 as pessoa

nome1 = 'João'
nome2 = 'João'

print(nome1 == nome2)

pessoa1 = pessoa.Pessoa('100100100-10', 'João')
pessoa2 = pessoa.Pessoa('100100100-10', 'João')
pessoa3 = pessoa.Pessoa('100100100-11', 'Maria')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)
print(pessoa1 == pessoa2)

pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)

print(pessoas_lista.count(pessoa1))