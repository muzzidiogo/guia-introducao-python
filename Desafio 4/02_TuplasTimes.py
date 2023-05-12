#   Com as tuplas dos 20 primeiros colocados da Liga Juvenil de Futebol Amador,
#   ordenados de acordo com sua colocação, escreva na tela:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avaí')

# a)
print(f'a) {times[:5]}\n')

#b)
print(f'b) {times[15:]}\n')

#c)
times_alfabetico = [times[0]]
for time in times:
    for i in range(0, len(times_alfabetico)):
        if time < times_alfabetico[i]:
            times_alfabetico.insert(i, time)
            break

print(f'c) {times_alfabetico}\n')
        
#d)
for i in range(0, len(times)):
    if times[i] == 'Chapecoense':
        print(f'd) Chapecoense está na posição {i+1}\n')