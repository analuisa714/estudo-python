""" Aula 02 - Manipulando arquivos """

# Abrindo e escrevendo em arquivos

# arq = open('arquivos.txt', 'w')

# arq.write('Olá, tudo bem?')
# arq.write('Caio\nMarcos\nJoão')

# x = ['Caio', 'João', 'Marcos']
# arq.writelines(x)
# for nome in x:
#     arq.write(nome + '\n')

# arq.close()

# Abrindo e fechando arquivos automaticamente com o with

# with open('arquivo.txt', 'a') as arq:
#     arq.write('\ncaio')

# with open('arquivo.txt', 'r') as arq:
#     x = arq.read()
#     print(type(x))

# with open('arquivo.txt', 'r') as arq:
#     x = arq.readlines()
#     print(type(x))

# Trabalhando com leitura em binário
# with open('arquivo.txt', 'rb') as arq:
#     x = arq.read()
#     print(type(x))
#     print(x.decode())
#     print(type(x.decode()))

with open('arquivo.txt', 'r') as arq:
    # for i in arq:
    #     print(i)
    print(next(arq))
    print(next(arq))
