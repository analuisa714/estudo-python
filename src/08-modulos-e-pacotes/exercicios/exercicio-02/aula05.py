""" Aula 05 - Métodos especiais """

from classes import retangulo

retangulo1 = retangulo.Retangulo(10.0, 5.0)
retangulo2 = retangulo.Retangulo(3.0, 14.0)

print(retangulo1.__repr__())
retangulo3 = eval('retangulo.Retangulo(7.5,12.3)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)
