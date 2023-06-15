""" Exercício 06 - aquário """

comprimento = float(input('Comprimento do aquário (cm): '))
altura = float(input('Altura do aquário (cm): '))
largura = float(input('Largura do aquário (cm): '))
temperatura_desejada = float(
    input('Digite a temperatura que você quer manter o aquário: '))
temperatura_ambiente = float(
    input('Digite a temperatura ambiente de onde ele vai ficar: '))

aquario = {
    'altura': altura,
    'comprimento': comprimento,
    'largura': largura
}


def calcular_volume(aquario):
    volume = (aquario['comprimento'] * aquario['altura']
              * aquario['largura']) / 1000
    return volume


aquario['volume'] = calcular_volume(aquario)


def calcular_potencia(aquario, temperatura_desejada, temperatura_ambiente):
    potencia = aquario['volume'] * 0.05 * \
        (temperatura_desejada - temperatura_ambiente)
    if potencia < 0:
        potencia = potencia * -1
    return potencia


def qtidade_filtragem(aquario):
    filtragem = [str(aquario['volume'] * 2)]
    filtragem.append(str(aquario['volume'] * 3))
    return filtragem


qtidade_filtragem(aquario)

print(f'O volume do aquário é: {aquario["volume"]} litros')

print(f'A potência do aquário deve ser: {calcular_potencia(aquario,temperatura_desejada, temperatura_ambiente)} watts')

print(
    f'A quantidade de filtragem necessária deverá ser entre {qtidade_filtragem(aquario)[0]} e {qtidade_filtragem(aquario)[1]} litros.')
