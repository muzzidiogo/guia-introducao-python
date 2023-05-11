# Defina a função div que recebe como argumentos dois números naturais  m  e  n  
# e devolve o resultado da divisão inteira de  m  por  n . 

# div(7,2)
# Esperado: 3

def div(m, n):
    return m//n

print('Digite dois números')
x, y = map(int, input().split())

print(f'A divisão inteira entre {x} e {y} é {div(x,y)}')