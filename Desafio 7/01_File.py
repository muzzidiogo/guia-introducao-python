"""
referencia: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# 1-Abra o arquivo do diretorio atual "foo.txt"
# Printe todo o conteudo do arquivo , então feche o arquivo
with open('my_workspace/guia-introducao-python/Desafio 7/foo.txt', 'r') as foo:
    print(f'#1: {foo.read()}\n')

# 2- Crie um arquivo chamado "bar.txt" 
# Abra o arquivo e conte quanta vezes a palavra "sir" aparece 
# Escreva no arquivo que voce criou quantas palavras foram encontradas
# Feche o arquivo
with open('my_workspace/guia-introducao-python/Desafio 7/foo.txt', 'r') as foo:
    texto = foo.read()
    num_sir = texto.count('sir')
    with open('my_workspace/guia-introducao-python/Desafio 7/bar.txt', 'w') as bar:
        bar.write(f'A palavra "sir" foi escrita {num_sir} vezes no arquivo "foo.txt"')