#   Faça um funcão que leia o nome de uma pessoa
#   e diga se ela tem "Silva" no nome.

def silva_detector():
    nome = input("Digite seu nome: ")
    nome = nome.casefold()
    if "silva" in nome:
        print('Silva!')
    else:
        print('Não Silva :(')
silva_detector()