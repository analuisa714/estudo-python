""" Aula 05 - Tipos de dados """

# Numéricos 
# int, float

idade = 20
peso = 70.5

print (idade, type(idade))
print (peso, type(peso))

# String
nome = 'Pedro'
sobrenome = 'dos Santos'
nome_completo = nome + " " + sobrenome
print(nome_completo)

produto = 'Coca-cola'

# o cliente nome_completo comprou o produto produto
# interpolação de variáveis

print(f'O cliente {nome} {sobrenome} comprou o produto {produto}')

print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())

# separador para exibir
print (1, 3, 5, 6, 7, 'adsdasdd', sep='   ')

# Boolean
ligado = True
print(ligado, type(ligado))

resultado = 9 == 10
print(resultado, type(resultado))

# Listas 
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
# print(frutas[3]) #Index Error

frutas[0] = 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# Tuplas
codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])

# codigos[0] = 'SP05' # TypeError

print(len(codigos))

# Conjuntos
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)
# não garante ordenação

# Dicionários

funcionario = {
    'codigo' : 123,
    'nome' : 'Maria da Silva',
    'salario': 7000.00
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())
# retorna um objeto

funcionario['salario'] = 9000.00
print(funcionario)