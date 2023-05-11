# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.
print('Digite os valores do triângulo')
x, y, z= map(int, input().split())

isTriang = False

if x+y > z and x+z > y and y+z > x:
    isTriang = True

if isTriang:
    if x == y == z:
        print('O triângulo é equilátero')
    elif x == y or x == z or y == z:
        print('O triângulo é isóceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é um triângulo :(')