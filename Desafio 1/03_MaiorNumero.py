# Escreva uma função para encontrar o maior entre 3 numeros
def max(a,b,c):
    m = a
    if(b > m):
        m = b
    if(c > m):
        m = c
    print(f"O maior número é {m}")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
max(a,b,c)