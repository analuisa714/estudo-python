""" Exercício 01 """

from classes import aluno

aluno1 = aluno.Aluno.from_string('SP0101,João,joao@email.com')
aluno2 = aluno.Aluno.from_string('SP0101,João,joao@email.com')
aluno3 = aluno.Aluno.from_string('SP0102,Ana Luisa,analu@email.com')

print(aluno1)
print(aluno2)
print(aluno3)
print('Aluno 1 e 2 são iguais:', aluno1 == aluno2)
