""" Aula 04 - Variáveis, Constantes e Literais """

# Variável: container para guardar dados
# inferência de tipo

numero = 10
print(numero, type(numero))

# alterar valor de uma variável
numero = 20
print (numero)

# múltiplas atribuições

nome, idade, endereco = 'Maria', 20, 'Rua dos...'
print(nome, numero, endereco)

nome = 'Maria'
idade = 20
endereco = 'Rua dos...'

print(nome, numero, endereco)

# atribui o mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

# Variáveis
# snake_case
id_funcionario = 209
salario_atual = 5000.50
print(id_funcionario, salario_atual)

# Constantes
# Upper case - snake_case
PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais
idade = 27
print(idade)
print(27)

# Numéricos
print (10, type(10))
print (10, type(-10))
print (10.5, type(10.5))

# String
print('Maria', type('Maria'))
print("Maria", type("Maria"))

# Booleano
print (True, type(True))
print (False, type(False))

# None
print (None, type(None))

# Coleções

# Lista (list)
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla (tuple) #imutável
emails = ('joao@gmail.com', 'maria@gmail.com')
print(emails, type(emails))

# Conjunto (set)
nomes = {'maria', 'joão', 'pedro', 'maria'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'prontuario' : 123456,
    'nome' : 'Maria',
    'idade' : 25 
}
print(aluno, type(aluno))