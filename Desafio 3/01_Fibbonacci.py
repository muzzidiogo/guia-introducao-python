# Os números de Fibonacci são representados pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 
# onde cada valor é calculado pela soma dos dois anteriores. 
# Faça um programa que gere e imprima os primeiros 10 valores desta sequência utilizando for ou while.

def fibo():
    num1 = 0
    num2 = 1
    print(num1)
    print(num2)
    for i in range(8):
        n = num2 + num1
        print(n)
        num1 = num2
        num2 = n

fibo()
        