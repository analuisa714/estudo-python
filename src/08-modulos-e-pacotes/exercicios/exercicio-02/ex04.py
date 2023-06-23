""" Exercício 04 """

from classes import aluno, projeto, participacao


aluno1 = aluno.Aluno.from_string('SP0101,João,joao@email.com')
aluno2 = aluno.Aluno.from_string('SP2020,Maria,maria@email.com')

projeto1 = projeto.Projeto.from_string(
    '10,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto2 = projeto.Projeto.from_string(
    '20,LabHardware,Sônia Andrade')

participacao1 = participacao.Participacao(
    1, '10/11/2023', '10/03/2024', aluno1, projeto1)
participacao2 = participacao.Participacao(
    2, '10/11/2023', '10/03/2024', aluno2, projeto1)
participacao3 = participacao.Participacao(
    3, '10/11/2023', '10/03/2024', aluno1, projeto2)

projeto1.add_participacao(participacao1)
projeto1.add_participacao(participacao2)
projeto1.print_participacoes()

projeto2.add_participacao(participacao3)
projeto2.print_participacoes()
