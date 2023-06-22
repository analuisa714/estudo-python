""" Aula 01 - Módulos e pacotes """

# outra forma de fazer a importação só de alguns métodos, modularizando; não recomendada:
# from uteis import fatorial, dobro 

# importando pacote
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
