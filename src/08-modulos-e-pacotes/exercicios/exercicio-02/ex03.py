""" Exercício 03 """

from classes import aluno, projeto, participacao


aluno1 = aluno.Aluno.from_string('SP0101,João,joao@email.com')

projeto1 = projeto.Projeto.from_string(
    '1,Laboratório de Desenvolvimento de Software,Pedro Gomes')

participacao = participacao.Participacao(
    1, '10/11/2023', '10/03/2024', aluno1, projeto1)
print(participacao)
