""" Exercício 04 - retorna a soma dos números usando args """

def somar(*args):
    soma = 0.0
    for numero in args:
        soma += numero
    return(soma)

print('A soma de números usando o args é', somar(1, 2, 3))
