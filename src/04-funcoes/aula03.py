""" Aula 03 - *args e **kwargs """

# args são utilizados para flexibilizar 
# a quantidade de parâmetros permitidos para uma função;
# nesse caso, o nome dos argumentos não importa.

# cria uma função que exibe quantos títulos da copa tem um país
def world_cup_titles(country, *args):
    print ('Country: ', country)

    for title in args:
        print('year: ', title)

# exemplo de chamada com 5 parâmetros de títulos
world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

# exemplo de chamada com 1 parâmetro de título
world_cup_titles('Espanha', '2010')



# kwargs são utilizados para flexibilizar a quantidade de
# parametros permitidos, os tornando opcionais;
# nesse caso, porém, o nome dos argumentos importa

# cria uma função que calcula e retorna um preço, aceitando desconto ou taxa (como opcionais);
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')

    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

# chamada passando só o valor
final_price = calculate_price(100.0)
print(final_price)

# chamada passando o valor e um desconto
final_price = calculate_price(100.0, discount=5.0)
print(final_price)

# chamada passando o valor e uma taxa
final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

# chamada passando o valor, uma taxa e um desconto
final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)
