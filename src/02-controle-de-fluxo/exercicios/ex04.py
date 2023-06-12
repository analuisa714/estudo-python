""" Exercício 04 - verificar identificador apresentando erros """

identificador = list(input('Digite seu identificador: '))

erros = []

NUMERO_INVALIDO = True

TAMANHO_VALIDO = len(identificador) == 7

if TAMANHO_VALIDO:
    for i in range(2, 6):
        if identificador[i].isdigit():
            identificador[i] = int(identificador[i])
            if (0 <= identificador[i]) and (i != 5):
                NUMERO_INVALIDO = False
            elif (1 <= identificador[i]) and (i == 5):
                NUMERO_INVALIDO = False
            else:
                erros.append('O identificador não apresenta números inteiros entre 0001 e 9999.')
else:
    erros.append('O identificador não apresenta números inteiros entre 0001 e 9999.')

if identificador[0] != 'B' or identificador[1] != 'R':
    erros.append('O identificador não inicia com a sequência "BR"')

FINAL_INVALIDO = identificador[len(identificador) - 1] != 'X'
if FINAL_INVALIDO:
    erros.append('O identificador não termina com o caractere "X"')

if erros:
    print('Identificador inválido. Os seguintes erros foram encontrados: ')
    for erro in erros:
        print(erro, sep='\n')
else:
    print('Identificador válido')
