""" Classe Pessoa e subclasses Cliente, Funcionario e Programador """

class Pessoa: 
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
class Cliente(Pessoa): 
    def __init__ (self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

class Funcionario(Pessoa):
    def __init__ (self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)
    
class Programador(Funcionario): 
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus  

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento() 
        return pagamento_salario + self.bonus
    