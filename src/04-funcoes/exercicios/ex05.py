""" Exercício 05 - retorna a soma dos números usando args """

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

individuo = {
    'altura': altura,
    'peso': peso
}


def calcular_imc(individuo):
    imc = round(individuo['peso'] / (individuo['altura'] * individuo['altura']), 2)
    return imc


individuo['imc'] = calcular_imc(individuo)


def obter_classificacao(imc):
    PESO_BAIXO = imc < 18.5
    PESO_NORMAL = 18.5 <= imc <= 24.9
    PESO_EXCESSO = 25 <= imc < 29.9
    OBESIDADE_1 = 30 <= imc < 34.9
    OBESIDADE_2 = 35 <= imc < 39.9

    classificacao = ''

    if PESO_BAIXO:
        classificacao = 'baixo peso'
        return classificacao
    elif PESO_NORMAL:
        classificacao = 'peso normal'
        return classificacao
    elif PESO_EXCESSO:
        classificacao = 'excesso de peso'
        return classificacao
    elif OBESIDADE_1:
        classificacao = 'obesidade de classe 1'
        return classificacao
    elif OBESIDADE_2:
        classificacao = 'obesidade de classe 2'
        return classificacao
    else:
        classificacao = 'obesidade de classe 3'
        return classificacao


classificacao = obter_classificacao(individuo['imc'])


def situacao_individuo(imc):
    PESO_BAIXO = imc < 18.5
    PESO_NORMAL = 18.5 <= imc <= 24.9
    PESO_ALTO = 25 <= imc

    situacao = ''

    if PESO_BAIXO:
        situacao = 'ganhar peso'
        return situacao
    elif PESO_NORMAL:
        situacao = 'normal'
        return situacao
    else:
        situacao = 'perder peso'
        return situacao


situacao = situacao_individuo(individuo['imc'])

print(f'Seu IMC é: {individuo["imc"]}')

print(f'Sua classificação é: {classificacao}')

print(f'Sua situação se enquadra como: {situacao}')
