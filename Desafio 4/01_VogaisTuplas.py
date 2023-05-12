#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in frutas:
    vogais_palavra = []
    for letra in palavra:
        if letra in vogais:
            vogais_palavra.append(letra)
    print(f'Em {palavra}, há as vogais: {vogais_palavra}')