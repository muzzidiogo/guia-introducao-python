import numpy as np

#1- Crie uma matriz 1D com números de 0 a 9
matrix = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'#1: {matrix}\n')

#2- Crie uma matriz booleana numpy 3×3 com ‘True’
matrix = np.array([[True, True, True],
                   [True, True, True],
                   [True, True, True]])
print(f'#2: \n{matrix}\n')

#3- Extraia todos os números ímpares de ‘arr’
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

index = 0
indices = []

for i in np.nditer(arr):
    if i % 2 != 0:
        indices.append(index)
    index+=1

print(f'#3: ìmpares nas posições de indice {indices}\n')

#4- Substitua todos os números ímpares arr por -1
arr[indices] = -1
print(f'#4: {arr}\n')

#5- Substitua todos os números ímpares em arr com -1 sem alterar arr
arr = np.arange(10)

arr2 = np.where(arr % 2 != 0)
print(f'#5: {arr2}\n')
#6 - Converta uma matriz 1D para uma matriz 2D com 2 linhas:
arr = np.arange(10)

arr2D = arr[np.newaxis, :]
print(f'#6: \n{arr2D}\n')

#7- Empilhe matrizes verticalmente:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

m_vertical = np.vstack((a, b))
print(f'#7: \n{m_vertical}\n')

#8- Empilhe as matrizes horizontalmente:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

m_horizontal = np.hstack((a, b))
print(f'#8: \n{m_horizontal}\n')