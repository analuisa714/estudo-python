""" Exercício 03 - meses do ano com dict """

meses = {
    '1': 'Janeiro', 
    '2':'Fevereiro', 
    '3':'Março', 
    '4':'Abril', 
    '5':'Maio', 
    '6':'Junho', 
    '7':'Julho', 
    '8':'Agosto', 
    '9':'Setembro', 
    '10':'Outubro', 
    '11':'Novembro', 
    '12':'Dezembro'
    }

mes = input('Digite um mês do ano, em formato numérico: ')

if mes in meses:
    print(meses[mes])
else:
    print('Mês digitado inválido. O número deve ser de 1 a 12!')
