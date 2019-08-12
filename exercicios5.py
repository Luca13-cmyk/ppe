# 1)
"""

def inteiro(x):
    return (x * 2)

print(inteiro(10))
"""
# 2)
"""

def datas(dia, mes, ano):
    meses = ["Janeiro", "Fevereiro", "Marco", "Abril",  "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
             "Novembro",
             "Dezembro"]
    return f"{dia} de {meses[mes-1]} de {ano}"

print(datas(13, 3, 2001))
"""

# 3)
"""
def posinega(numero):
    if numero > 0:
        return "Positivo"
    elif numero == 0:
        return numero
    return "Negativo"

print(posinega(0))

"""
# 4)
"""
import math


def quadradoPerfeito(valor):
    if valor > 0:
        sqrt = int(math.sqrt(valor))
        if (sqrt ** 2) == valor:
            return "Quadrado perfeito"
        return "N e quadrado perfeito"


print(quadradoPerfeito(90))
print(quadradoPerfeito(81))
print(quadradoPerfeito(64))
# print(list(map(quadradoPerfeito, range(0, 101))))
# print(dict(map(quadradoPerfeito, range(0, 101))))
quadrado = {valor: quadradoPerfeito(valor) for valor in range(0, 101)}
print(quadrado)
print(list(map(quadradoPerfeito, range(0, 101))))
"""

# 5)
"""
from math import pi
def esfera(r):
    v = 4/3 * pi * (r ** 3)
    return v
print(pi)
print(esfera(4))
"""

# 6)
"""

def convertsToSeconds(hora, minuto, segundo):
    segH = hora * 3600
    segM = minuto * 60
    return segH + segM + segundo


print(convertsToSeconds(5, 25, 0))
"""


# 7)

def CtoF(c):
    f = c * (9.0/5.0) + 32.0
    return f

print(CtoF(24))

