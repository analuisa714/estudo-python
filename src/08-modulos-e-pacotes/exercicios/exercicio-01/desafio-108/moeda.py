def metade(valor):
    return valor / 2

def dobro(valor):
    return valor * 2

def aumentar(valor, porcentagem):
    return valor + (porcentagem/100 * valor)

def diminuir(valor, porcentagem):
    return valor - (porcentagem/100 * valor)

def moeda(valor):
    valor_string = (str(valor)).split(sep='.')

    if len(valor_string[1]) < 2:
        valor_string[1] = valor_string[1] + '0'

    return 'R$' + valor_string[0] + ',' + valor_string[1]
