""" Exercício 01 - média aritmética de 3 notas """

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10
NOTA3_VALIDA = 0 <= n3 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA and NOTA3_VALIDA:
    media = (n1 + n2 + n3)/3
    print('A média aritmética das notas é: ', media)
else:
    print('Digite notas válidas (entre 0 e 10)')