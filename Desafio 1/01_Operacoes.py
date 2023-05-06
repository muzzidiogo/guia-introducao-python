# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.

a, b, c = map(int, input().split())

soma = a+b+c
prod = a*b*c


print(f"Soma: {soma}\nProduto: {prod}")

# Escreva um programa que leia um número e apresente a raiz quadrada deste número.
x = int(input("Entre  a number: "))
y = x**0.5
print(f"Raíz quadrada de {x} = {y}")


