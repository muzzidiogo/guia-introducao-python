# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 

def prime():
    n = int(input('Digite um número: '))
    i = 2
    isPrime = True
    
    while i <= int(n**0.5):
        if n%i == 0:
            isPrime = False
        i += 1
    
    if isPrime:
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')

prime()