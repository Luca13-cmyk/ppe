# -*- coding: UTF-8 -*-
"""

-> Todas minhas ferramentas de Python para otimizar as coisas;

l_. Luca Negrette ._l

"""

from math import isnan

# *** *** *** *** *** *** sum_of_arrays()


def sum_of_arrays(*args):
    """
    Sum of the numbers in a box [], {}, ()
    Ex:
        arr = [2, 1, 5]
        arr2 = [1, 5, 7]
        print(sum_of_array(*arr, *arr2))

    * The arguments must be numeric

    :param args: *array, *tuple, *collect
    :return: return sum(*args)
    """
    return sum(args)


# *** *** *** *** *** *** key_value()


def key_value(**kwargs):
    """
    Show key, value in a dict
    Ex:
        dic = {
            'Name': 'Luca',
            'City': 'Ilhéus-BA'
        }
        print(key_value(**dic))

    :param kwargs: **dict
    :return: return key: value
    """
    for key, value in kwargs.items():
        print(f"{key}: {value},")


# *** *** *** *** *** *** key_has_value()


def key_has_value(key, value, **kwargs):
    """
    Verify if the key has a val == value
    Ex:
        dados = {
            'local': 'Ilhéus',
            'estado': 'BA',
            'nome': 'luca',
            'sobrenome': 'Negrette',
            "ator": 'julie'
        }
        retu = key_has_value('ator', 'julie', **dados)
        if retu:
            print('has')
        else:
            print('Doesn't has')

    :param key: the key of the dict
    :param value: the value of the dict
    :param kwargs: the dict
    :return: if has: return True, if has not: return False
    """
    if key in kwargs:
        val = kwargs.get(key)
        if val == value:
            return True
        return False


def porcentagem_de(porcent, numero, valor=False):
    """
    Calcula a porcentagem do numero especificado
    EX:
        print(porcentagem_de(10, 245))
        10 % de 145 e quanto?

    :param porcent: porcentagem%
    :param numero: numero
    :return: retorna o resultado da porcentagem
    """
    try:
        ret = (porcent * numero) / 100
        if valor:
            return numero - ret
        return ret
    except TypeError:
        print("Digite um numero valido !")


def porcentagem_qnt(valor, numero):
    """
    retorna a porcentagem do valor especificado em relacao ao numero
    EX:
        print(porcentagem_qnt(10, 100))
        10 e quantos % de 100

    :param valor: valor
    :param numero: numero
    :return: ret%
    """
    try:
        ret = (valor * 100) / numero
        return ret
    except TypeError:
        print("Digite um numero valido !")


def is_num(valor):
    try:
        if not isnan(valor):
            return True
    except:
        return False







