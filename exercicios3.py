# -*- coding: utf-8 -*-

# 1)

"""
for n in range(1, 5+1):
    print(3 * n)
"""

# 2)

"""
# for _ in range(3):
#     for n in range(1, 100+1):
#         print(n)
# b = 0
# while b < 3:
#     print(list(range(1, 100+1)))
#     b += 1
"""

# 3)

"""
b = 10

while b > -1:
    print(f"{b}")
    b -= 1
print("Fim")

"""

# 4)

"""

valor = int(0)

while valor < 100000:
    valor += 1000
    print(valor)
print(valor)

"""

# 5)

"""
valores = input("Digite dez valores: ")
arr = valores.split()
soma = 0
for n in arr:
    soma += int(n)
print(f"Os valores {arr} somados é igual a; {soma}")

"""

# 6)

"""
valores = input("Digite dez valores: ")

arr = valores.split()
soma = 0
for n in arr:
    soma += int(n)
print(f"A média é {soma / len(arr)}")
"""

# 7)
"""
# import os
# 
# op = ''
# print(f"Bem vindo(a)")
# while op != 's':
#     op = input("Se desejar sair [s] para sair [c] para continuar: ")
#     if op == 'c':
#         num = input("Digite números inteiros positivos: ")
#         print("Calculando a média desses números...")
#         arr = num.split()
#         arr2 = []
#         soma = 0
#         certo = True
# 
#         for n in arr:
#             arr2.append(float(n))
#         for n in arr2:
#             if n < 0:
#                 certo = False
#                 break
#             else:
#                 soma += n
# 
#         if certo:
#             print(f"A média é: {soma / len(arr2)}")
#         else:
#             print("Inválido")


"""

# 8)

"""
numeros = input("Digite os números: ")
arr = numeros.split()
arr2 = []
for n in arr:

    arr2.append(int(n))
arr2.sort()
# com = len(arr2)
print(arr2[0], arr2[len(arr2) - 1])

"""

# 9)

"""
# numero = int(input("Digite o N: "))
# arr = []
# for n in range(1, numero+1):
#     if n % 2 > 0:
#         arr.append(int(n))
#
#
# print(f"Os  números naturais ímpares são: {arr}")

# ar = list(range(0, 10))
# print(ar)
# ar = list(range(0, 10, 2))
# print(ar)

"""

# 10)

"""
arr = []

for n in range(1, 50+1):
    if n % 2 == 0:
        arr.append(int(n))
print(arr)
print(f'A soma é: {sum(arr)}')


"""

# 11)

"""
num = int(input("Digite o N: "))

for n in range(0, num+1):
    print(n, end='')
"""
# 12)

"""
num = int(input("Digite o N: "))
arr = []
for n in range(num, -1, -1):
    arr.append(n)
print(arr)

"""
# 13)


"""
num = int(input("Digite o N: "))
arr = []

for n in range(0, num+1):
    if n % 2 == 0:
        arr.append(n)
print(arr)

"""

# 14)
"""
num = int(input("Digite o N: "))
arr = []

for n in range(num, -1, -1):
    if n % 2 == 0:
        arr.append(n)
print(arr)

"""
# 15)

"""
num = int(input("Digite o N: "))
arr = []

for n in range(1, num):
    if n % 2 > 0:
        arr.append(n)
print(arr)

"""
# bonus)
"""
arr = []
b = 0
while b < 1000:
    for n in range(0, 2):
        print(n, end='')
    b += 1
print('\n')

"""

# 16)

"""
num = int(input("Digite o N: "))
arr = []

for i in range(num, 0, -1):
    if i % 2 > 0:
        arr.append(i)
print(arr)

"""

# 17)

"""
num = int(input("Digite o N: "))
arr = []

for n in range(0, num+1):
    arr.append(n)
print(arr)
print(sum(arr))

"""

# 18)



# 19)

"""
num = '105'

for n in num:
    print(n)

"""