
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Printar o Sistema Operacional que voce esta usando:
# YOUR CODE HERE
print(f'Sistema Operacional: {sys.platform}')

# Printar a versão de Python que voce esta usando:
# YOUR CODE HERE
print(f'Versão do python: {sys.version_info}')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Printar a process Id atual
# YOUR CODE HERE
print(f'Process ID Atual: {os.getpid()}')

# Printar o atual diretório:
# YOUR CODE HERE
print(f'Diretório atual: {os.curdir}')

# Printar o nome da maquina
# YOUR CODE HERE
print(f'Nome desta máquina na rede: {os.uname()}')