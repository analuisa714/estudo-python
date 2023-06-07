""" Aula 02 - instrução if """

# python
# if condicao:
#    instrucao
#    instrucao
#    instrucao

# C, Java, C# outras
# if (){
#     condicao
# condicao
# }

codigo_cliente = 32
valor_desconto = 19.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print('Desconto especial')
    print(codigo_cliente)
else:
    print('Sem desconto especial')

# nome tem que ter pelo menos três caracteres
nome = 'Lo'

print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3
NOME_VALIDO = len(nome) >= 3

if NOME_INVALIDO:
    print('O nome deve ter pelo menos três caracteres')
else:
    print('Nome válido')

if NOME_VALIDO:
    print('Nome válido')
else:
    print('O nome deve ter pelo menos três caracteres')

if not NOME_INVALIDO:
    print('Nome válido')
else:
    print('O nome deve ter pelo menos três caracteres')

# nome tem que ter pelo menos três caracteres
# idade tem que ser maior igual a 18
# exibir todos os erros no final apenas
nome = 'Lo'
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos três caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade deve ser maior ou igual a 18 anos')

# False: False, None, 0, 0.0, string vazia '', lista, tupla ou set vazio
# True: todo o resto
if erros:
    print(erros)
else:
    print('Dados válidos')

# if elif else

# Verifica se um número é positivo ou negativo ou zero
numero = -4

#  _____________ _ _________
# -N -4 -3 -2 -1 0 1 2 3 4 N
if numero > 3:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')

# calcule a média e verifique se as duas notas são válidas antes do cálculo

n1 = 5.6
n2 = 10.0

# Cuidado com ifs aninhados
if n1 >= 0 and n1 <= 10:
    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2
        if media >= 6:
            print('Aprovado')
        elif media >= 4:
            print('Recuperação')
        else:
            print('Reprovado')
else:
    print('Notas inválidas')

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')
