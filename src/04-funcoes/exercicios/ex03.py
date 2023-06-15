""" Exercício 03 - retorna a soma dos números usando tupla """

def somar(numeros):
    soma = 0.0
    for numero in numeros:
        soma += numero
    return(soma)

num = (7, 6, 4)
print('A soma de números de uma tupla é', somar(num))
