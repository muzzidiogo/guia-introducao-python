# Faça um programa que receba 5 números e retorne o maior e o menor numero, a soma e a média dos números.

lista = [1,77,87,-5, 10]

def max():
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

def min():
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

def med():
    sum = 0
    n = 0
    for i in lista:
        sum += i
        n += 1
    return sum/n

print(f'Para essa lista, o valor máximo é {max()}, o mínimo é {min()} e a média é {med()}')