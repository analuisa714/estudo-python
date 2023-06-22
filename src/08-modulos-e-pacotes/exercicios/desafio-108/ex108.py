""" Desafio 108 """

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'A dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% de {moeda.moeda(preco)} é {moeda.moeda(moeda.aumentar(preco,10))}')
print(f'Diminuindo 13% de {moeda.moeda(preco)} é {moeda.moeda(moeda.diminuir(preco,13))}')
