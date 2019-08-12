# -*- coding: utf-8 -*-

# Recebendo dados do usuário
# import os
# print("Digite seu nome: ")
# nome = input()
# print("Digite sua idade: ")
# idade = input()
#
# print(f"Seu nome é {nome} e sua idade é {idade}")

#print("Digite um número: ")
#num1 = input()
# print("Digite o outro numero: ")
# num2 = input()

# print(f"o primeiro numero é {num1} o segundo é {num2}")
# print(f"a soma dos dois é: {int(num1) + int(num2)}")
#
# os.system(f"echo o primeiro numero é {num1}")
#
# if 4 > 0 and 5 > 2 and \
#     6 < 8:
#     print("deu certo")
# import os
# import sys
# import random
# import time as  t
# from colorama import Fore, init
#
# logo_design_1 = ('''
#   {0}/  /
#  {1}/  /
# {2}/ _/''').format(Fore.GREEN, Fore.RED, Fore.WHITE)
#
# print(logo_design_1)

# if 256 % 3 >= 1:
#     print("A divisão deu um número ímpar")
# else:
#     print("A divisão deu um número  par")
#
#
# gg = False
#
# print(not gg)




# nome = str(input("Digite seu nome "))
# idade = int(input("Digite sua idade "))

# print(f"Seu nome é {nome} e sua idade é {idade}")
# print(f"Você nasceu em {2019 - idade}")




# nome = 'Gina\'s Bar'
# print(nome)
# print(type(nome))
#
#
# print(nome[2::-1])


#for n in range(len(val)):
   #     soma += int(num[n])

# num = '102030'
# soma = 0
# for a in num:
#     soma += int(a)
# print(soma)

# arr = [1, 2, 3, 5, 10]
#
# for a in arr:
#     print(a)

# nome = 'Luca Antonio'

# for i, l in enumerate(nome):
#     print(f'{i} + {l}')

# for i, _ in enumerate(nome):
#     print(i)

# for valor in enumerate(nome):
#     print(valor)

# qtd = int(input("Digite a quantidade de loop: "))
# soma = 0
# for n in range(1, qtd+1):
#     soma += n
# print(soma)

# notas = input("Digite as notas: ")
#
# arr = notas.split()
#
# print("As notas são: ")
# for n in arr:
#     print(f"[ {n} ] ", end='')



# for _ in range(3):
#     for n in range(1, 11):
#         print("\U0001F60D" * n, end='')

# Inverso
# for n in range(50, -1, -5):
#     print(n)

# lista = list(range(2, 52, 2))
#
# print(lista[2])
#
#
#
# resposta = ''
#
# while resposta != 'sim':
#     resposta = input("Já acabou Jéssica? ")


# for n in range(1, 50):
#     if n == 4:
#         break
#     else:
#         print(n)
#
# while True:
#     resposta = str(input("Digite [s] para sair ou [n] para continuar[s/n]: "))
#     if resposta == 's':
#         break
#     elif resposta == 'n':
#         print("Continuando...")

# arr = list(range(1, 11))
# arr.insert(0, 0)
# arr.insert(0, 'Meu array')
# arr.extend([11, 12, 13, 14, 15, 16, 17])
# arr.append(18)
# arr.append(list("Novo Array"))
#
# lista2 = [1, 2, 75, 36, 99, 5, 13, 17]
#
# lista2.sort()
# lista2.reverse()
# print(lista2)
# # remove o ultimo
# lista2.pop()
# print(lista2)
#
# lista2.clear()
# print(lista2)


# arr = 'Luca é lindo: Jade é sua esposa: '
# lista1 = list(arr)
# # lista2 = arr.split(':')
# # print(lista1)
# # print(lista2)
#
# print(lista1)
# # Convertendo um array para uma string
# poema = ''.join(lista1)
# print(poema)


# arr = ['Luca', 'e', 'Jade', 'se', 'amam']
#
# print(arr)
#
# poema = '$'.join(arr)
# print(poema)
# poema2 = ' '.join(arr)
# print(poema2)
#
# arr2 = [['M', 'S', 'N'], ['Luca', 'e', 'Jade'], 0, 5, 7, {'color': True}]
# print(arr2[1][0])
# print(arr2[len(arr2) - 1]['color'])
# print(arr2[-1])
# print(arr2[-1]['color'])



# arr = ['b', 'g', 'c', 'f', 'a', 't', 'l', 'w', 'a']

# print(arr)

# for i, l in enumerate(arr):
#     if l == 'a':
#         local = i
#         arr.pop(local)
# print(arr)


# print(arr.index('a'))

# try:
#     print(arr.index('z'))
# except:
#     print("N tem")


# print(arr.index('a', 5))

# print(arr.index('a', 6, len(arr)))

# valores = input('Digite os valores: ')
# arr = valores.split()
# arr2 = []
# for n in arr:
#     arr2.append(int(n))
# print(arr2)
# print(f'O maior valor: {max(arr2)}')
# print(f'A soma é: {sum(arr2)}')
# print(f'O minimo valor é: {min(arr2)}')
# print(f'O comprimento é: {len(arr2)}')

# Desempacotamento de listas
# num1, num2, num3 = arr2
#
# print(num1, num2, num3)

# Deep Copy
# nova = arr2.copy()
#
# nova.append("Teste")
# print(nova)

# Shallow Copy

# tupla = tuple(range(11))
# print(tupla)
# print(type(tupla))
#
# tupla2 = 2, 5, 7, 9
# print(tupla2)

# val = input('Digite algo max = 2: ')
# arr = val.split()
#
# teo, teol = arr
# print(teo, teol)
#
# print(arr.count('luca'))

paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'ARG': 'Argentina'

}
# print(paises)
# print(type(paises))

# arg = paises.get('ARG', None)
# if arg:
#     print(f"Encontrei o país {arg}")
# else:
#     print("Não encontrei")

# ru = paises.get("ru", None)
# if ru:
#     print(f"Encontrei o país {ru}")
# else:
#     print("Não encontrei o país")

# if 'br' in paises:
#     brasil = paises['br']
#
#
#
# if brasil:
#     print(brasil)
#

# localidades = {
#     'Ilheus': 'Bahia',
#     'CEP': [
#         '01547',
#         'Affonso',
#         '7777777',
#         255
#     ],
#     'cartao': {
#         'postal': 'fixo'
#     }
# }
#
# print(localidades)
# print(localidades.get('CEP')[0])
# print(localidades.get('cartao').get('postal'))

maps = {
    'Tokyo': (175.45877, 555.7484),
    'Nova York': (544.7584, 333.5555),
    'São Paulo': (45.1058754, 35.75575)
}

# print(maps.get('Tokyo')[0])
# print(maps.get('Tokyo')[1])

# if 'Tokyo' in maps:
#     longe = maps.get('Tokyo')[0]
#     lati = maps.get('Tokyo')[1]
# else:
#     print("Não tem")
#
# print(longe, lati)

# coord = maps.get('Tokyo', None)
#
#
# if coord:
#     lati = maps.get('Tokyo')[0]
#     longe = maps.get('Tokyo')[1]
#     print(lati, longe)
#
# else:
#     print("Não tem")

# print(maps)
# # adicionando chaves/valores ao objeto(dicionário) 'maps'
# maps['Rio de Janeiro'] = (155.87456, 33.15151317)
# print(maps)
# print(maps.get('Rio de Janeiro'))
# # adicionando método 2
# novo_dado = {'Brasilia': (99.87878, 55.131313)}
# maps.update(novo_dado)
# print(maps)
# print(maps.get('Brasilia'))


# atualizando um array
# arr = ['carro', 'bicicleta']
#
# print(arr)
# arr[0] = 'feijao'
# print(arr)

# print(maps)
#
# # maps.clear()
# #
# # print(maps)
#
# maps2 = maps.copy()
#
# print


# for chave in maps.keys():
#     print(f'A cidade {chave} tem as coordenadas {maps[chave]}')
#
# for valor in maps.values():
#     print(valor)
#
# for chave, valor in maps.items():
#     print(f'Chave {chave} valor {valor}')


# conjunto (set)

# con = set({1, 50, 75, 8, 6})
# print(con)
# print(type(con))
#
# con = ['arr', 0, 4, 70, True]
#
# jj = set(con)
# print(jj)
# print(type(jj))

# ca = False
#
# while ca == False:
#     palavra = list('Luca e jade se amam')
#     print(palavra)
#     resposta = input('Digite-a corretamente: ')
#
#     if resposta == 'Luca e jade se amam':
#         print('Acertou')
#         ca = True
#     else:
#         print("Errou")




# dic = {}.fromkeys([50, 45, 100, 145, 85], 'dict')
# print(dic)


# Con = {1, 50, 75, 80}
# print(Con)
# Con.add(199)
# Con.add(666)
# print(Con)
# Con.remove(666)
# print(Con)
#
#
#
# ret = maps.pop('Tokyo')
# print(ret)

# alunos_python = {'Luca Negrette', 'Carlos Alexandre', 'Bianca Madeira', 'Jade Picon', 'Luca Antonio'}
# alunos_java = {'Brenda Loguercio', 'João da Silva', 'Luca Negrette', 'Jade Picon'}
#
# unicos1 = alunos_python.union(alunos_java)
# print(unicos1)
# print(len(unicos1))
#
# unicos2 = alunos_java | alunos_python
# print(unicos2)
#
#
# ambos = alunos_python.intersection(alunos_java)
# print(ambos)
#
# ambos2 = alunos_java & alunos_python
# print(ambos2)
#
# so_python = alunos_python.difference(alunos_java)
# so_java = alunos_java.difference(alunos_python)
# print(so_python)
# print(so_java)

#
# tupla = 2, 2, 5, 7, 7
# print(tupla)
# print(type(tupla))

# from collections import Counter
#
# lista = [17, 17, 17, 17, 15, 15, 1, 2, 100, 150]
#
# ret = Counter(lista)
#
# print(ret)
#
# for chave, valor in ret.items():
#     print(f'O {chave} possuí {valor} sequências')

from collections import Counter

# frase = ('O  O serviço gratuito do Google traduz instantaneamente '
#          'palavras, frases e páginas da Web entre o inglês e mais de 100 outros idiomas.')
#
#
# print(frase)

# retun = Counter(frase)
# print(retun)
# for chave, valor in retun.items():
#     if chave == 'a':
#         print(chave, valor)


# arr = frase.split()
#
# cont = Counter(arr)
#
# print(cont.most_common(2))

#
# alunos_celular = {'Luca Negrette', 'Brenda Loguercio', 'Carlos Alexandre', 'Erick Soares'}
# alunos_pc = {'Jade Picon', 'Luca Negrette', 'Erick Soares', 'Bianca Madeira', 'Laís Fonseca'}
#
#
# alunos_total = alunos_celular.union(alunos_pc)
# arr = []
#
# for n in alunos_total:
#     arr.append(n)
#
#
# print(arr)
# print('\n')
#
# print(f'Os alunos na escola são: ')
# for a in arr:
#
#     print(a)
# print(f'A quantidade é {len(alunos_total)}')
#
#
# ambos_cursos = alunos_pc.intersection(alunos_celular)
# arr = []
#
# for a in ambos_cursos:
#     arr.append(a)
#
# print('\n')
# print('Os alunos que fazem os dois cursos são: ')
#
# for a in arr:
#     print(a)
# print(f'A quantidade é {len(arr)}')
#
# print('\n')
# so_pc = alunos_pc.difference(alunos_celular)
# so_celular = alunos_celular.difference(alunos_pc)
#
#
# print('Os alunos que só fazem curso de computador: ')
# for n in so_pc:
#     print(n)
# print(f'O tamanho é {len(so_pc)}')
# print('\n')
# print(f'Os alunos que só fazem curso de celular: ')
# for n in so_celular:
#     print(n)
# print(f'O tamanho é {len(so_celular)}')


#
# from collections import OrderedDict
#
# dic = OrderedDict({
#     'a': 1,
#     'b': 2,
#     'c': 3
# })
#
#
# print(dic)
# print(type(dic))
# print(dic.get('a'))
#
# dic['d'] = 4
# print(dic)
# print(dic.get('d'))
#
# from collections import namedtuple
#
# cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])
#
# sol = cachorro(idade=15, raca='Fofinho', nome='Sol')
#
# print(sol)
# print(sol[1])

# lista = list('Geek')
# print(lista)

from collections import deque

# arr = deque([['carro', 2, False], 'arroz', 'feijão'])
# print(arr)
# print(arr[0])


#
# def quadrado_de_7():
#     return (7 ** 2)
#
#
# retu = quadrado_de_7()
#
# print(retu)
#
# def soma(val):
#     return  val + 49
# print(soma(quadrado_de_7()) + 2)



#
# nomes = 'luca', 'jade', 'beca', 'bucetinha marota'
#
#
#
# print(nomes)
# print(type(nomes))

# nome = 'luca'
#
# nomes = f'Jadee e {nome}'
#
# print(nomes)

"""
(•_•)
∫\ \___( •_•)
_∫∫ _∫∫ \ \

"""

#
# def mensa(nome, mulher='Jade'):
#     print(f'O {nome} se casou com a {mulher}')
# mensa('Luca')
# mensa('Luca', 'Yennefer')
# soma = 0
# def incremento():
#     global soma
#     soma = soma + 1
#     return soma
# print(incremento())
#
#
# def lala():
#     """É uma docstring"""
#     global soma
#     soma += 2
#     return soma
# print(lala())
# print(lala.__doc__)

# from ferramentas import sum_of_arrays
#
#
#
# arr1 = [2, 5, 7, 8]
# arr2 = [5, 7, 8, 4]
# arr3 = [1, 1, 1, 1]
#
#
# print(sum_of_arrays(*arr1, *arr2, *arr3))


#
# numeros = [2, 5, 4, 7]
#
# res = {n: ("par" if n % 2 == 0 else "impar") for n in numeros}
#
# print(res)

#
# num = input("Digite os numeros: ")
# num = num.split(' ')
# pares = [n for n in num if int(n) % 2 == 0]
# impares = [n for n in num if int(n) % 2 != 0]
# print(f"Os numeros pares sao {pares}, os numeros impares sao {impares}")

#
# numeros = {x: x** 2 for x in range(10)}
# print(numeros)
#
# from collections import Counter
#
# letras = "Geek University"
#
# print(Counter(letras))
#
# calc = lambda x: \
#     3 * x + 1
#
# print(calc(4))
#
#
# nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
#
# print(nome_completo(' luca', ' Negrette'))


autores = ['Luca Negrette', 'Jade Picon', 'Rober Jr', 'Adressa Carvalho']
#
# autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
# print(autores)
#
#
# def sort_sobrenome(arr):
#     return arr.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
#
#
# sort_sobrenome(autores)
# print(autores)
#
#
# def qualquer():
#     return lambda x: x+x
#
#
# print(qualquer()(2))
#

#
# def area(val):
#     return val * 2
#
#
# valores = [40, 2, 5, 7, 45]
# resul = []
#
# for v in valores:
#     resul.append(area(v))
# print(resul)
#
#
# resul = list(map(area, valores))
# print(resul)

#
# valores = [40, 2, 5, 7, 45]
#
# resul = list(map(lambda val: val ** 2, valores))
# print(resul)
#
# resul = [n ** 2 for n in valores]
# print(resul)
#


#
# nomesI = [("Jessica", 13), ("Luca", 18), ("Jade", 18)]
#
# print(list(map(lambda dado: f"Idade: {dado[1]} Nome: {dado[0]}", nomesI)))
#
# resul = [[f"Nome: {n[0]} Idade: {n[1]}"] for n in nomesI]
# print(resul)

#
# valores = input("Digite os valores: ")
# valores = valores.split(' ')

# resul = list(map(lambda dado: int(dado) ** 2, valores))
# print(resul)
# import statistics
# resul = [int(n) ** 2 for n in valores]
# print(resul)
# print(f"A media e: {statistics.mean(resul)}")
# print(f"OS valores acima da media sao: {list(filter(lambda x: x > statistics.mean(resul), resul))}")

#
# paisess = ['', 'Brasil', 'Israel', 'EUA', '']
#
# print(list(filter(None, paisess))) # remove os dados vazios

#
# valores = input("Digite os valores: ")
# valores = valores.split(' ')
# print(valores)
# valores = list(filter(None, valores))
# print(valores)

#
# valores = input("Digite os valores: ")
# valores = valores.split()
# valores = filter(None, valores)
# valores = list(filter(lambda x: int(x) > 3.5, valores))
# print(valores)


dados = [
    {"Username": "Angelica", "Logado": True},
    {"Username": "Luca", "Logado": False},
    {"Username": "Jade", "Logado": True}
]
# inativos = list(filter(lambda l: not l["Logado"], dados))
# print(inativos)
# ativos = list(filter(lambda l: l["Logado"], dados))
# print(ativos)

inativos = list(map(lambda x: x, filter(lambda x: not x.get("Logado"), dados)))
print(inativos)
ativos = list(map(lambda x: x, filter(lambda x: x.get("Logado"), dados)))
print(ativos)









