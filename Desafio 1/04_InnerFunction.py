# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor

def interna(a, b):
    return a+b

def externa(a, b):
    print(f"{interna(a, b) + 5}2")

a = int(input("a = "))
b = int(input("b = "))
externa(a, b)