""" Aula 01 - Introdução a Orientação a Objetos """

from classes import retangulo


retangulo1 = retangulo.Retangulo(10.0, 5.0)
retangulo2 = retangulo.Retangulo(6.0, 3.0)

print(type(retangulo1), retangulo1)
print(type(retangulo2), retangulo2)

print(
    retangulo1.base,
    retangulo1.altura,
    retangulo1.calcular_area(),
    retangulo1.calcular_perimetro()
)
print(
    retangulo2.base,
    retangulo2.altura,
    retangulo2.calcular_area(),
    retangulo2.calcular_perimetro()
)
