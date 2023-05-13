#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.
dict_alunos = {}

nome = input('Nome do aluno: ')
media = int(input('Média do aluno: '))
dict_alunos.update({nome:media})

print(dict_alunos)