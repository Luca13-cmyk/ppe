# -*- coding: utf-8 -*-

# 1)

"""
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O número {num1} é maior que o {num2} ")
elif num2 > num1:
    print(f"O número {num2} é maior que o {num1} ")
elif num1 == num2:
    print("Os dois números são iguais")


"""

# 2)

"""

import math

num = int(input("Digite um número: "))

if num > 0:
    print(f"A raiz quadrada do número é igual a: {math.sqrt(num)}")
elif num <= 0:
    print(f"Número inválido")
"""

# 3)

"""
import math

num = int(input("Digite um número: "))

if num > 0:
    print(f"{math.sqrt(num)}")
elif num <= 0:
    print(f"{num ** 2}")
"""

# 4)
"""
import math

num = int(input("Digite um número: "))

if num > 0:
    print(f"{num ** 2} | {math.sqrt(num)}")
"""

# 5)

"""
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("É par")
elif num % 2 > 0:
    print("É impar")
"""

# 6)

"""
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2} e a diferença é de {num1 - num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1} e a diferença é de {num2 - num1}")
"""

# 7)

"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1}")
elif num1 == num2:
    print("São iguais")
"""

# 8)

"""
num1 = int(input("Digite as notas: "))
num2 = int(input("Digite outro número: "))

# if num1 and num2 >= 0:
#     if num1 < 0:
#         print("Número 1 inválido")
#     elif num2 < 0:
#         print("Número 2 inválido")
#     else:
#         print(f"A média destas notas é: {(num1 + num2) / 2}")
# elif num1 and num2 < 0:
#     print("Números inválidos! ")

if num1 >= 0:
    if num2 >= 0:
        print(f"A média destas notas é: {(num1 + num2) / 2}")
else:
    print("Números inválidos")

"""


# 9)

"""
sala = float(input("Digite o salário: "))
presta = float(input("Digite a prestação: "))
por = presta * 100 / sala

if por > 20:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
"""

# 10)

"""
sexo = str(input("Digite seu sexo [Homem ou Mulher]: "))
sexo = sexo.lower()
H = float(input("Digite a sua áltura: "))
if sexo == 'homem':
    print(f"Seu peso ideal é de: {(72.7 * H) - 58}")
elif sexo == 'mulher':
    print(f"Seu peso ideal é de: {(62.1 * H) - 44.7}")

"""

# 11)

"""
num = input("Digite o número: ")

if int(num) > 0:
    soma = 0
    for a in num:
        soma += int(a)
    print(f"A soma é {soma}")
else:
    print(f"Número {num} inválido")

"""






# Bônus)
"""
def con(val):
    arr = []
    mensa = ''
    print(f"O número é: {val}")
    b = 0
    while b < len(val):
        arr.append(val[b])

        b += 1
    print(f"os valores são {arr[::]}")
    soma = 0
    for n in range(len(val)):
        soma += int(num[n])
    print(f"A soma dos algarismos  é igual a {soma}")
    if int(val) % 2 == 0:
        som = 0
        mensa = 'O número' + ' ' + val + ' ' + ' é par'
        for n in range(len(val)):
            som += int(num[n])
        if som % 3 == 0:
            mensa = 'O número é par e é divisivel por 3'
        print(mensa)
    elif int(val) % 2 > 0:
        mensa = 'O número' + ' ' + mensa + ' ' + ' é ímpar'
        print(mensa)


num = input("Digite o número: ")

if int(num) > 0:
    con(num)
else:
    print(f"Número inválido")

"""

# 12)

"""
from math import log

x = int(input("Digite o logarítimo: "))
b = int(input("Digite a base: "))

if x > 0:
    print(f"O logarítimo do número é: {log(x) / log(b)}")

"""

# 13)

"""
notas = input("Digite as nostas: ")
arr = notas.split()

b = 0
soma = 0
while b < len(arr):
    soma += float(arr[b])
    b += 1
if soma / 3 >= 60:
    print(f"Você passou! a sua média foi {soma / 3}")
else:
    print(f"Vocẽ não passou! a sua média foi {soma / 3}")

"""

# 14)

"""
notaFinal = 0
def notafilal():
    notas = input("Digite as notas: ")
    arr = notas.split()

    b = 0
    soma = 0
    while b < len(arr):
        soma += float(arr[b])
        b += 1
    notaFinal = soma / 3
    if notaFinal <= 2.9:
        print(f"Reprovado, a sua nota final foi {notaFinal}")
    elif notaFinal >= 3 and notaFinal < 5:
        print(f"Recuperação, a sua nota final foi {notaFinal}")
    elif notaFinal >= 5:
        print(f"Aprovado, a sua nota final foi {notaFinal}")
notafilal()

"""

# 15)










