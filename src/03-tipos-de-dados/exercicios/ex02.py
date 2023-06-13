""" Exercício 02 - meses do ano com tupla """

MESES = (
    'Janeiro', 
    'Fevereiro', 
    'Março', 
    'Abril', 
    'Maio', 
    'Junho', 
    'Julho', 
    'Agosto', 
    'Setembro', 
    'Outubro', 
    'Novembro', 
    'Dezembro'
    )

mes = int(input('Digite um mês do ano, em formato numérico: '))

MES_VALIDO = 1 <= mes <= 12

if MES_VALIDO:
    print(MESES[mes-1])
else:
    print('Mês digitado inválido. O número deve ser de 1 a 12!')
