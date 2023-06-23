""" Exercício 02 """

from classes import projeto

projeto1 = projeto.Projeto.from_string('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto2 = projeto.Projeto.from_string('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto3 = projeto.Projeto.from_string('2,Monitoria,Maria')

print(projeto1)
print(projeto2)
print(projeto3)
print('Projeto 1 e 2 são iguais:', projeto1 == projeto2)
