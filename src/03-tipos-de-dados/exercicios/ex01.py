""" Exercício 01 - menor e maior elemento """

numeros = []

for i in range(3):
    numero = input(f'Digite o {i+1}º número: ')
    numeros.append(float(numero))

menor = numeros[0]
maior = numeros[0]

for numero in numeros:
    if menor > numero:
        menor = numero
    if maior < numero:
        maior = numero

print(f'O menor número é: {menor}, enquanto o maior número é: {maior}')
