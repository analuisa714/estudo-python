""" Aula 08 - Herança """

from classes.pessoa import pessoa08 as pessoa

programador = pessoa.Programador("José", "Augusto", "123.123.123-12", 5000.00, 200)
print(programador.obtem_nome_completo())
print(programador.calcula_pagamento())
print(type(programador))

# funcionario = Funcionario("José", "Augusto", "123.123.123-12", 5000.00)
# print(funcionario.obtem_nome_completo())
# print(funcionario.calcula_pagamento())

# cliente = Cliente("Paulo", "Mulotto", "123.123.123-12")
# print(cliente.obtem_nome_completo())
