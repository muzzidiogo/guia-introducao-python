#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

def a_reader():
    phrase = input('Digite sua frase: ')
    count = 0
    i = 0
    pos = []
    
    for word in phrase:
        if word == 'a':
            count += 1
            pos.append(i)
        i+=1
    
    print(f'A letra "A" apareceu {count} vezes, primeiro na posição {pos[0]} e por último na posição {pos[len(pos)-1]}')

a_reader()