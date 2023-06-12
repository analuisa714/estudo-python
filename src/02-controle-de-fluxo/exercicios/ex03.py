""" Exercício 03 - verificar identificador """

identificador = input('Digite seu identificador: ')
identificador = list(identificador)

NUMERO_INVALIDO = True

for i in range(2, 6):
    if identificador[i].isdigit():
        identificador[i] = int(identificador[i])
        if (0 <= identificador[i] <= 9) and (i != 5):
            NUMERO_INVALIDO = False
        elif (1 <= identificador[i] <= 9) and (i == 5):
            NUMERO_INVALIDO = False
        else:
            NUMERO_INVALIDO = True

if len(identificador) != 7:
    print('Identificador inválido')
elif identificador[0] != 'B' or identificador[1] != 'R':
    print('Identificador inválido')
elif identificador[len(identificador) - 1] != 'X':
    print('Identificador inválido')
elif NUMERO_INVALIDO:
    print('Identificador inválido')
else:
    print('Identificador válido')
