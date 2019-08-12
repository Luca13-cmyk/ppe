# -*- coding: UTF-8 -*-

from collections import deque


# 1)

"""
vetor = deque([1, 0, 5, -2, -5, 7])

valores = [vetor[0], vetor[1], vetor[5]]
soma = sum(valores)

vetor[4] = 100

for n in vetor:
    print(n, end='\n')
"""
# 2)

"""
valores = str(input('Digite os 6 valores: '))
arr = valores.split()

for n in arr:
    print(n)

"""

# 3)

"""
import math
valores = str(input('Digite os 10 valores: '))
arr = valores.split()

vetor2 = []
for n in arr:
    vetor2.append(math.sqrt(int(n)))
print(vetor2)

"""

# 4)

"""
arr = deque([10, 45, 75, 65, 12, 15, 7, 2])
dig = input('Digite os lugares [x][y]: ')
digArr = dig.split()

x = None
y = None
i = 0


while i < len(digArr):
    if i == 0:
        x = int(digArr[0])
    elif i == 1:
        y = int(digArr[1])
    i += 1

print(f'A soma dos valores é {arr[x] + arr[y]}')

"""

# Bônus)

"""
def somaArray(array, valores):

    digArr = valores.split()

    x = None
    y = None
    i = 0

    while i < len(digArr):
        if i == 0:
            x = int(digArr[0])
        elif i == 1:
            y = int(digArr[1])
        i += 1

    print(f'A soma dos valores é {array[x] + array[y]}')


arr = deque([20, 45, 75, 65, 12, 15, 7, 2])
dig = input('Digite os lugares [x][y]: ')

somaArray(arr, dig)

"""

# 5)
"""
vetor = list(range(0, 50+1))
arr = []
for n in vetor:
    if n % 2 == 0:
        arr.append(n)
print(arr)
print(sum(arr))

# soma = 0
#
# for n in arr:
#     soma += n
# print(soma)

"""

# 6)

"""
dados = input('Digite um vetor com 10 números: ')
vetor = dados.split()
vetor_numero = []

for n in vetor:
    vetor_numero.append(int(n))
print(f'O maior número é o {max(vetor_numero)} e o menor é o {min(vetor_numero)}')
"""

# 7)

"""
arr = [12, 45, 75, 100, 80, 58, 7, 8, 9, 10]

print(arr)
maior = max(arr)
print(maior)
print(arr.index(maior))

# com outra forma

# arr = deque([12, 45, 75, 100, 80, 58, 7, 8, 9, 10])
# print(arr)
# maior = max(arr)
# print(maior)
# print(arr.index(maior))
"""


# 8)

"""

arr = [0, 1, 2, 3, 4, 5, 6]
arr.reverse()
print(arr)

"""

# 9)

"""

arr = [0, 1, 2, 3, 4, 5, 6]
arr2 = []
for n in arr:
    if n % 2 == 0:
        arr2.append(n)
arr2.reverse()
print(arr2)

"""

# 10)

"""
notas = str(input('Digite as notas dos alunos: '))
arr = notas.split()
arr2 = []

for n in arr:
    arr2.append(int(n))
quantos = len(arr2)
media = (sum(arr2) / quantos)
print(media)
"""

# 11)

"""
vetor = [-5, 2, 14, -11, 5, 17, 7, 8, 9.45, 10]
negativos = []
positivos = []
for n in vetor:
    if n < 0:
        negativos.append(n)
    elif n > 0:
        positivos.append(n)
print(negativos)
print(sum(positivos))
"""
#
# arr = [2, 2, 4, 5]
#
# def soma(array):
#     soma = 0
#     for n in array:
#         soma += n
#     return soma
#
# print(soma(arr))




"""
l_. Luca Negrette ._l
"""
"""


╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║ 0 0 ║
║┏┓║┏━╣┗╣┗╣╰°╯║
╚┛┗╩━━╩━╩━╩-2K19?

"""

# print("""
#
# ┈┈▕▔╲┈┈┈╱▔▏┈┈┈┈┈
# ┈┈▕┃╲▔▔▔╲┃▏┈┈┈┈┈
# ┈┈╱┊┳▅╮╭▅┳▏┈┈┈┈┈
# ┈╱┊╲┊▔┊┊▔┊▏┈┈┈┈┈
# ╱┊┊▕┊╱◥◤╲┊▏┈OS┈X┈
# ┊┊┊┊╲╲╱╲╱╱┈Welcome┈
# ┊┊┊┊┊▔▔▔▔▏┈┈Lion┈┈
#
# """)

# 12)

"""
valores = deque([10, 10, 10, 10, 5, 5])
print(f'{valores}, O maior número é o {max(valores)}, o menor {min(valores)}, a média '
      f'{(sum(valores) / len(valores))}')

"""

# 13)

"""
valores = deque([11, 10, 10, 10, 5])
maior = max(valores)
menor = min(valores)

print(valores.index(maior), valores.index(menor))
"""

# 14)

"""
from collections import Counter

valores = deque([11, 11,  10, 10, 10, 5, 5, 5])
repeticoes = Counter(valores)
print(repeticoes.most_common(2))
"""

# 15)

"""
from collections import Counter

valores = [11, 11,  10, 10, 10, 5, 5, 5, 2, 3, 4]
repeticoes = Counter(valores)

valores = []
for chave, valor in repeticoes.items():
    if valor == 1:
        valores.append(chave)

print(valores)


"""



# ****************** COLORS
# print(f'\033[1;36;0mOlá, Mundo\033[m')

from colorama import Fore, init, Style
import os


print(f"""{Fore.LIGHTCYAN_EX}
 
   ┈┈▕▔╲┈┈┈╱▔▏┈┈┈┈┈
   ┈┈▕┃╲▔▔▔╲┃▏┈┈┈┈┈                              
   ┈┈╱┊┳▅╮╭▅┳▏┈┈┈┈┈                              
   ┈╱┊╲┊▔┊┊▔┊▏┈┈┈┈┈                              
   ╱┊┊▕┊╱◥◤╲┊▏┈OS┈X┈                              
    ┊┊┊╲╲╱╲╱╱┈Welcome┈                             
    ┊┊┊┊▔▔▔▔▏┈┈{os.system('echo $HOME')}┈┈                                                           
 
 """)
#
# print(f'{Style.BRIGHT} {Fore.CYAN} Hello World')
# print('Csa')
#
# page_1 = '''\n
# {0}[{1}1{0}] {2}Show Connected Devices      {0}[{1}6{0}] {2}Screen record a phone               {0}[{1}11{0}] {2}Uninstall an app
# {0}[{1}2{0}] {2}Disconect all devices       {0}[{1}7{0}] {2}Screen Shot a picture on a phone    {0}[{1}12{0}] {2}Show real time log of device
# {0}[{1}3{0}] {2}Connect a new phone         {0}[{1}8{0}] {2}Restart Server                      {0}[{1}13{0}] {2}Dump System Info
# {0}[{1}4{0}] {2}Access Shell on a phone     {0}[{1}9{0}] {2}Pull folders from phone to pc       {0}[{1}14{0}] {2}List all apps on a phone
# {0}[{1}5{0}] {2}Install an apk on a phone   {0}[{1}10{0}] {2}Turn The Device off                {0}[{1}15{0}] {2}Run an app
#
#
# {0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}p{0}] Next Page                           v1.2
# '''.format(Fore.CYAN, Fore.RED, Fore.GREEN)
#
# print(page_1)

# *******************




# 16)

"""
vetor = [1, 2, 3, 4, -5]
cod = ''
while cod != 0:
    cod = int(input('{2}Digite o código {0}[0]{1} para sair {0}[1] {1}para ordem direta {0}[2]{1} para ordem inversa: '
                    .format(Fore.GREEN, Fore.RED, Fore.LIGHTCYAN_EX)))
    if cod == 1:
        vetor.sort()
        print(f'{Fore.WHITE} {Style.BRIGHT} {vetor}')
    if cod == 2:
        vetor.reverse()
        print(vetor)
"""


