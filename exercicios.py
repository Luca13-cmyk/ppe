# -*- coding: utf-8 -*-

# 6) graus celsius para fahrenheit
"""
 graus = int(input("Quantos graus está: "))

print(f"Em F é: {graus * (9.0/5.0) + 32.0}")

"""

# 7) fahrenheit para  graus celsius

"""
f = int(input("Digite a temperatura em F: "))

print(f"Essa temperatura para G fica: {int(5.0 * (f - 32.0) / 9.0)}")

"""

# 8) Kelvin para  graus celsius

"""
Kelvin = int(input("Digite a temperatura em Kelvin: "))

print(f"Essa temperatura em G fica: {int(Kelvin - 273.15)}")

"""

# 9)  graus celsius para Kelvin

"""
G = int(input("Digite a temperatura em graus celsius: "))

print(f"Essa temperatura em K fica: {G + 273.15}")

"""

# 10)  km/h para m/s

"""
kmH = int(185)
print(f"O carro estava numa velocidade de {kmH} km/h e {int(kmH / 3.6)} m/s")

"""

# 11)  m/s para km/h

"""
ms = int(51)

print(f"O carro está a {ms} m/s e a {int(ms * 3.6)} km/h")
"""
# Bônus) Calcule a Velocidade Média

"""
print("Cálculo de VM")
print("\n")

DSf = int(input("Digite o DSf: "))
DSi = int(input("Digite o DSi: "))
Tf = int(input("Digite a Tf: "))
Ti = int(input("Digite a Ti: "))
print(f"A velocidade média é de {(DSf - DSi) / (Tf - Ti)} km/h")

"""


# 12)  milhas para km

"""
Milhas = int(input("Digite a distância em Milhas "))

print(f"Essas milhas convertidas em KM fica: {1.61 * Milhas} KM")
"""

# 13)   km para milhas

"""
KM = int(input("Digite a distãncia em KM "))

print(f"Essa distãncia em Milhas ficam: {KM / 1.61}")
"""

# 14) Graus em radianos

"""
import math

pi = math.pi
graus = float(input("Digite o GRAUS: "))

print(f"A resoluçao de graus para radianos fica igual a: {graus * pi/180}")
"""

# 15) Radianos para Graus

"""
import math

pi = math.pi

radianos = float(input("Digite o radiano: "))

print(f"A resolução de radiano para graus fica igual a: {radianos * 180/pi}")

"""

# 16) polegadas para centimetros

"""
Polegada = int(input("Digite o valor da polegada: "))
print(f"Essa polegada convertida em CM fica igual a: {Polegada * 2.54}")

"""

# 17) centimetros para polegada

"""
C = float(input("Digite os centimetros: "))
print(f"Esse valor para polegadas é igual a: {C / 2.54}")

"""

# 18) m³ para litros

"""
M3 = float(input("Digite o valor do m³: "))
print(f"Esse valor transformado em L é igual a: {1000 * M3}")
"""

# 19) L para m³

"""
L = float(input("Digite o valor em litros: "))
print(f"Esse valor convertido em m³ fica igual a: {L / 1000}")

"""

# 20) KG para libras

"""
KQ = float(input("Digite o valor em KG: "))
print(f"Esse valor convertido em libras fica igual a: {KQ / 0.45}")

"""

# 21) Libras para KQ

"""
L = float(input("Digite o valor em Libras: "))
print(f"Esse valor em KQ fica igual a: {L * 0.45}")

"""

# 22) jardas para metros

"""
J = float(input("Digite o valor em jardas: "))
print(f"Esse valor convertido em metros é igual a: {0.91 * J}")

"""

# 23) metros para jardas

"""
M = int(input("Digite o valor em Metros: "))
print(f"Esse valor convertido em jardas é igual a: {M / 0.91}")
"""

# 24) m² em acres

"""
M2 = int(input("Digite o valor em m²: "))
print(f"Esse valor convertido em acres é igual a: {M2 * 0.000247}")
"""

# 25) acres em m²

"""
A = float(input("Insira o valor em acres: "))
print(f"Esse valor convertido para m2: {A * 4048.58}")
"""

# 26) m² para hectares

"""
M2 = int(input("Dê o valor em m²: "))
print(f"Esse valor convertido para hectares é igual a: {M2 * 0.0001}")

"""

# 27) hectares para m²

"""
H = float(input("Dê o valor em hectar: "))
print(f"Esse valor convertido em m² é igual a: {H * 10000}")

"""

# 28) Soma dos quadrados de três valores

"""

val1 = 2
val2 = 3
val3 = 4

print(f"A soma do quadrado dos três valores é igual a; "
      f"{(val1 ** 2) + (val2 ** 2) + (val3 ** 2)}")

"""

# 29) Calcule a média de 4 notas

"""
nota1 = 10
nota2 = 10
nota3 = 10
nota4 = 9

print(f"A média das notas é igual a: {(nota1 + nota2 + nota3 + nota4) / 4}")
"""

# 30) Real para dolar

"""
print(int(1200 * 3.85))

"""

# 31) Imprimir o antecessor e sucessor

"""
num = 3
print(f"O número é {num} e seu antecessor 2 e sucessor 4")

"""

# 32)

"""
i = 15
resultado_suce = (i * 3) + 1
resultado_ante = (i * 2) - 1

print(f"{resultado_suce + resultado_ante}")

"""

# 33) Calcular o m2 da área

"""
comprimento = float(input("Digite o comprimento em cm: "))
largura = int(input("Digite a largura em cm: "))
M1 = comprimento / 100
M2 = largura / 100

print(f"O m² é da área é de: {M1  * M2}")

"""

# 34) O valor do raio com a saída a área do circulo correspondete
"""
import math

R = int(input("Digite o valor do raio: "))
print(f"A área do circulo corresponde a: {math.pi * (R ** 2)}")

"""

# 35)
"""

a = int(input("A: "))
b = int(input("B: "))
print(f"{((a ** 2) + (b ** 2) ** 2)}")

"""

# 36) Volume de um cilindro circular

"""

import math

H = float(input("Digite a altura: "))
R = float(input("Digite o raio: "))


print(f"O volume é de: {math.pi * (R ** 2) * H}")

"""