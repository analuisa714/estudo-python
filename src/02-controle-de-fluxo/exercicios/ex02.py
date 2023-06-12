""" Exercício 02 - média aritmética de notas """

notas = input('Digite as notas: ')
notas = notas.split(sep=',')

soma = 0.0

for nota in notas:
    NOTA_VALIDA = 0 <= float(nota) <= 10
    if NOTA_VALIDA:
        soma = soma + float(nota)
    else:
        print('Digite apenas notas válidas (entre 0 e 10)')

media = soma/len(notas)

if media >= 6:
    print('Aprovado')
elif media >= 4:
    print('Recuperação')
else:
    print('Reprovado')
