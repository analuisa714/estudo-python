""" Aula 03 - Métodos de classe """

from classes import retangulo

retangulo1 = retangulo.Retangulo(10.0, 5.0)
retangulo2 = retangulo.Retangulo(6.0, 3.0)
retangulo3 = retangulo.Retangulo.from_list([20.0, 3.5])
retangulo4 = retangulo.Retangulo.from_string('55.4,13.5')

print(retangulo3.base, retangulo3.altura, retangulo3.calcular_area())
print(retangulo4.base, retangulo4.altura, retangulo3.calcular_area())
