# -*- coding: utf-8 -*-

# numeros = [2, 5, 4, 7]
# soma = 0
# for n in numeros:
#     soma += n
# print(soma)
#
# from functools import reduce
#
# # print(reduce(lambda x, y: x + y, numeros))
# #
# # print(sum(numeros))
#
# print(reduce(lambda x, y: x * y, numeros))
#
# dados = [True, True, True]
# mod = all(dados)
# if mod:
#     print("Todos sao True")
# else:
#     print("Nem todos sao True")
#
# nomes = ["Rernanda", "Telipe", "Luca"]
# res = all([no[0] == "F" for no in nomes])
# print(res)
#
# res = any(no[0] == "F" for no in nomes)
# if res:
#     lista = list(filter(lambda x: x[0] == "F", nomes))
#     print(lista)
# else:
#     print("N tem")
#
# from sys import getsizeof
# numeros = (x * 10 for x in range(0, 50))  # generator  consume pouca memoria
# print(getsizeof(numeros))
#
# numeros = list(numeros)  # lista consume muita memoria em comparacao ao generator
# print(numeros)
# print(getsizeof(numeros))
# for n in numeros:
#     print(n)
#
# lista = [2, 5, 4, 7, 1, 3]
# lista.sort(reverse=True)
# tupla = 2, 5, 7, 8, 4, 1
# print(lista)
# print(sorted(tupla, reverse=True))
#
# usuarios = [
#     {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas", "Eu gozo rapido"]},
#     {"username": "carla", "tweets": ["Eu amo meu gato"]},
#     {"username": "jeff", "tweets": []},
#     {"username": "bob123", "tweets": [], "cor": "amarelo"},
#     {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
#     {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
# ]
#
# mais_tweets = list(sorted(usuarios, key=lambda t: len(t["tweets"]), reverse=True))
# print(mais_tweets[0])
# print(len(mais_tweets[0].get("tweets")))
# print(len(usuarios[0]["tweets"]))
#
#
# valores1 = [n for n in range(0, 10)]
# valores2 = [n for n in range(10, 20)]
#
# maior = max(valores1, valores2)


#
# musicas = [
#     {"titulo": "Thunderstruck", "tocou": 3},
#     {"titulo": "Dead Skin Mask", "tocou": 2},
#     {"titulo": "Back in Black", "tocou": 4},
#     {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
# ]
# # forma lenta
# mais = max(musicas, key=lambda musica: musica["tocou"])
# maisToca = mais.get("titulo")
# print(f"As mais tocada: {maisToca}")
#
# menos = min(musicas, key=lambda musica: musica["tocou"])
# menosToca = menos.get("titulo")
# print(f"A que menos toca: {menosToca}")
#
# # forma direta
# print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
# print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])


# sem max
# max = 0
# min = 0
# cache = []
# for m in musicas:
#     cache.append(m["tocou"])
# print(cache)
# for musica in musicas:
#     if musica["tocou"] in cache:
#         max = musica
# print(max)
#
# musicas = [
#     {"titulo": "Thunderstruck", "tocou": 3},
#     {"titulo": "Dead Skin Mask", "tocou": 2},
#     {"titulo": "Back in Black", "tocou": 4},
#     {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
# ]
# maisToca = max(musicas, key=lambda x: x["tocou"])["titulo"]
# print(maisToca)
# menosToca = min(musicas, key=lambda x: x["tocou"])["titulo"]
# print(menosToca)
# for l in reversed(menosToca):
#     print(l, end='')
# print(''.join(reversed(menosToca))) # transforma uma lista de strings em uma strig
#
# # EX
# strigs = ["l", "u", "c", "a"]
# print(''.join(strigs))
# --------------------------------

#
# num1 = [2, 5]
# num2 = [5, 5, 7, 8]
# num3 = 2, 4, 5, 6, 2, 4, 1, 14, 17
# print(list(zip(num1, num2, num3)))

#
# alunos = {"Luiz Carlos", "Jade Picon", "Luca Negrette"}
# nota1 = [50, 78, 65]
# nota2 = [75, 43, 99]
#
# final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, nota1, nota2)}
# print(final)
#
# alunos = str(input("Digite os nomes dos alunos: "))
# alunos = set(alunos.split(', '))
#
# nota1 = [50, 78, 65]
# nota2 = [75, 43, 99]
#
# final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, nota1, nota2)}
# print(final)
# maior = [n for n in final.values()]
# nome = [nome for nome, valor in final.items() if valor == max(maior)]
#
# print(f"A maior nota foi {max(maior)} e  do/a {nome[0]}")



# def soma(a,b):
#     return a + b
#
# somaL = lambda a, b: a.strip() + b.strip().title()
#
# print(soma("luca", "jade"))
# print(somaL("luca ", "jade "))
#
# nomecompleto = lambda nome, sobrenome: f"{nome.strip().title()} {sobrenome.strip().title()}"
#
# print(nomecompleto("luca", "jade "))




#
# autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
#            'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
#
# print(sorted(autores, key=lambda x: x.split(' ')[-1]))
# autores.sort(key=lambda x: x.split(' ')[-1])
#
# print(autores)

#
#
# numeros = [2, 4, 7, 8, 9]
#
# print(list(map(lambda x: x ** 2, numeros)))
#
# import math
#
#
# def area(r):
#     return math.pi * (r ** 2)
#
#
# raios = [2, 245, 2, 8, 4.2]
#
# print(list(map(lambda r: math.pi * (r ** 2), raios)))
# print(list(map(area, raios)))
# print(raios.count(2))
#
# tupla1 = 2, 4, 5
# tupla2 = 4, 8, 7
# print(tupla1 + tupla2)
# print(tupla1[2::-1])


#
# cidades = [("Londres", 14), ("Sao Paulo", 19), ("Rio de Janeiro", 30), ("Salvador", 32)]
#
# # print(list(map(lambda x: 9/5 * x + 32, filter(lambda x: x[1], cidades))))
# print(list(map(lambda x: 9/5 * x[1] + 32, cidades)))
#
# print(list(map(lambda x: (x[0], round(9/5 * x[1] + 32, 1)), cidades)))
#
# import statistics
# nomes = [("Jade", 75), ("Luca", 75), ("Luiz", 45), ("Antonio", 69)]
#
# media = list(map(lambda x: x[1], nomes))
# print(statistics.mean(media))
#
# print(statistics.mean([2, 4, 7, 8]))

#
# idades = [['Julia', 2], ['Pedro', 17], ['Jade', 18]]
# maior = sorted(idades, key=lambda x: x[1], reverse=True)
# print(dict(maior))

#
# alunos = [["Jade", 6.7], ["Luca", 7], ["Amanda", 8.4], ["Luiz", 4.7], ["Beto", 10]]
# passaram = [[a[0], a[1]] for a in alunos if a[1] > 5]
# print(passaram)
# nPassaram = [[a[0], a[1]] for a in alunos if a[1] <= 5]
# print(nPassaram)
#
#
# def completo(*args):
#     passaram = [[a[0], a[1]] for a in args if a[1] > 5]
#     nPassaram = [[a[0], a[1]] for a in args if a[1] <= 5]
#     print(f"Os alunos q passaram foram {passaram}")
#     print(f"Os alunos q n passaram foram {nPassaram}")
#
#
#
# completo(*alunos)

#
# todas = [["You aren't alone", 6], ["Mirror", 5],
#            ["Out of the blue", 2.45]]
# musicas = list([m[0], m[1]] for m in todas if m[1] <= 4)
# print(musicas)

# notas = [5, 4, 3, 4, 3, 4]
# passou = list(filter(lambda x: x > 5, notas))
# print(passou)
# nPssou = list(filter(lambda x: x < 5, notas))
# print(nPssou)
# print([n for n in notas if n > 5])
# print(n for n in notas if n > 5)
#
# passou = filter(lambda x: x > 5, notas)
# npassou = filter(lambda x: x > 5, notas)
# from sys import getsizeof
# print(type(passou))
# print(getsizeof(passou))


#
# paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela', 0, False, True]
#
#
#
# print(list(filter(None, paises)))
# print(list(filter(lambda x: len(x) > 0, paises)))


# usuarios = [
#     {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
#     {"username": "carla", "tweets": ["Eu amo meu gato"]},
#     {"username": "jeff", "tweets": []},
#     {"username": "bob123", "tweets": []},
#     {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
#     {"username": "gal", "tweets": []}
# ]
#
# inativos = list(filter(lambda x: not x.get("tweets"), usuarios))
# print(inativos)
#
# nomes = ["Vanessa", "Ana", "Maria"]
# ret = list(map(lambda n: f"Sua instrutora e {n}", filter(lambda x: len(x) < 5, nomes)))
# print(ret)
#
# ret2 = [f"Sua instrutora e {nome}" for nome in nomes if len(nome) < 5]
# print(ret2)
#
# nomes = ['Jariana', 'Jessica', 'Jade']
# print(all(nome[0] == 'J' for nome in nomes))
#
# idades = [["Mariana", 10], ["Jessica", 12]]
# print(all(idade[1] > 18 for idade in idades))
#
# convidados = [["Jade", 18], ["Luca", 18], ["Joao", 22], ["Pedro", 18]]
# todos = all(convidado[1] >= 18 for convidado in convidados)
# if todos:
#     print("A festa comeca")
# else:
#     print(f"Festa barrada por cause do/a {[f'{i[0]}, pois ele/a tem {i[1]} anos' for i in convidados if i[1] < 18]}")

# numeros = [12, 17, 18, 13]
# nomes = {"Luca", "Jade", "Pedro", "Felipe"}
# retu = zip(nomes, numeros)
# retu2 = list(retu)
#
# ganhador = any(p[1] == 17 for p in retu2)
# print(ganhador)
#
# if ganhador:
#     print(f"O ganhador foi {[(p[0], p[1]) for p in retu2 if p[1] == 17]}")


#
def sum_of_arrays(*args):
    """
    Sum of the numbers in a box [], {}, ()
    Ex:
        arr = [2, 1, 5]
        arr2 = [1, 5, 7]
        print(sum_of_array(*arr, *arr2))

    * The arguments must be numeric

    :param args: array, tuple, collect, dict
    :return: return sum(*args)
    """
    return sum(args)

#
# try:
#     geek()
# except:
#     print("Deu ruim")
#
# try:
#     len(17)
# except TypeError:
#     print("Deu ruim")

def geek():
    return "Funfa"

#
# try:
#     print(geek())
#     print(len(geek()))
#     len(78)
# except NameError as err:
#     print(f"Deu erro {err}")
# except TypeError as errb:
#     print(f"deu o erro {errb}")
# except:
#     print(f"Algum erro inesperado")

# entrada = str(input("Digite os numeros: "))
# entrada = entrada.split(' ')
# try:
#     arr = [int(n) for n in entrada]
#     print(sum(arr))
# except ValueError:
#     print("DIgite numeros e nao palavras")
#
# try:
#     entrada = int(input("Digite o numero inteiro: "))
#     print(entrada)
# except ValueError:
#     print("Digite um numero")
#
# try:
#     entrada = float(input("Digite o numero real: "))
#     print(entrada)
# except ValueError:
#     print("Digite um numero real")

#
# try:
#     entrada = str(input("Digite tres valores inteiros: "))
#     entrada = entrada.split(' ')
#     soma = [int(n) for n in entrada]
#     print(sum(soma))
# except ValueError:
#     print("Digite numeros !")
#
# try:
#     entrada = float(input("Digite o numero real: "))
#     print(entrada ** 2)
# except ValueError:
#     print("Digite um numero real !")

#
# try:
#     entrada = int(input("Digite um numero: "))
#     print(entrada ** 5)
# except ValueError:
#     print("Digite um numero")
#
# try:
#     entrada = int(input("Digite a temperatura em C:  "))
#     print(f"A temperatura  em C convertida  para F: {entrada * (9/5) + 32} ")
# except ValueError:
#     print("Digite um numero")

#
# def porcentagemDe(porcent, numero):
#     try:
#         ret = (porcent * numero) / 100
#         return f"{ret}"
#     except TypeError:
#         print("Utilize numeros !")
#
#
# def porcentagemQan(porcent, numero):
#     try:
#         ret = (porcent * 100) / numero
#         return ret
#     except TypeError:
#         print("Digite numeros validos !")
#
#
# print(porcentagemDe(10, 263.46))
# print(porcentagemQan(26.346, 263.46))


from ferramentas import *
#
# valor = 780
# primeiro = porcentagem_de(46, valor)
# segundo = porcentagem_de(32, valor)
# terceiro = valor - (primeiro + segundo)
# print(primeiro)
# print(segundo)
# print(terceiro)

# try:
#     entrada = int(input("Digite o numero de dias trabalhados: "))
#     liquido = porcentagem_de(8, (30 * entrada), valor=True)
#     print(f"A quantia liquida devera ser de R$ {liquido}")
# except ValueError:
#     print("Por favor, insira um dado numerico.")


# print(porcentagem_de(10, 100, valor=True))

#
# try:
#     entrada = float(input("Digite o valor da receita por hora: "))
#     entrada2 = int(input("Digite a carga de horario: "))
#     print(f"O funcionario  trabalhou {entrada2} horas no mes")
#     print(f"Ele recebera uma quantia de {entrada * entrada2} somado com 10% ficara "
#           f"{entrada * entrada2  + porcentagem_de(10, (entrada * entrada2))}")
# except:
#     print("s")
#
# try:
#     entrada = float(input("Digite o valor da receita por hora: "))
#     entrada2 = int(input("Digite a carga de horario: "))
#     receita = int((entrada * entrada2))
#     print(f"O funcionario recebera {receita} + 10% ficara com R$ {receita + porcentagem_de(10, receita)}")
# except ValueError:
#     print("Por favor, insira um dado numerico valido.")


#
#
# def dividir(a, b):
#     try:
#         a = int(a)
#         b = int(b)
#         return a / b
#     except ValueError:
#         print("coloque numeros validos !")


#
# try:
#     entrada = int(input("Digite o primeiro valor: "))
#     entrada2 = int(input("Digite o segundo valor: "))
# except ValueError:
#     print("Informe numeros validos !")
# else:
#     print(dividir(entrada, entrada2))
#
# import pdb
#
# entrada = input("Digite o primeiro valor: ")
# entrada2 = input("Digite o segundo valor: ")
# pdb.set_trace()
# print(dividir(entrada, entrada2))

#
# import random
# import sys
#
#
# print(int((random.random() * 10) + 1))

#
# from random import uniform as u
#
# for i in range(0, 11):
#     print(u(2, 7))
#
# from random import choice
#
# numeros = [2, 4, 7, 17, 18, 19, 16, 35, 99, 7845, 215464, 1111]
# print(choice(numeros))

from ferramentas import (
    sum_of_arrays,
    porcentagem_de,
    porcentagem_qnt,
    key_has_value,
    is_num
)



#
# print(porcentagem_de(10, 7000))
# if not math.isnan(porcentagem_de(10, 100)):
#     print(" e um numero")
# else:
#     print(" n E um numero")
#

# try:
#     if not math.isnan(valor):
#         print("E um numero")
# except:
#     print("N e um numero")

valor = porcentagem_de(10, 470, valor=True)

#
# def isNaN(valor):
#     try:
#         if not isnan(valor):
#             return False
#     except:
#         return True

#
# def is_num(valor):
#     try:
#         if not isnan(valor):
#             return True
#     except:
#         return False
#


if is_num("luca"):
    print("e um numero")
else:
    print("n e um numero")


