""" Desafio 107 """

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'A dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10% de {preco} é {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 13% de {preco} é {moeda.diminuir(preco, 13)}')
