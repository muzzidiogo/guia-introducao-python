"""
Para este exercicio, voce tem uma lista de dicionarios. Cada dicionario
tem as seguintes chaves:
 - lat: inteiro representando o valor de latitude
 - lon: inteiro representando o valor de longitude
 - name: nome do local
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Adicione um novo local a lista
# YOUR CODE HERE
waypoints.append({"lat":50, "lon":100, "name":"an island in the sky"})

# Modifique o dicionario com nome "a place" para uma longitude
# de valor -130 e mude seu nome para "not a real place"
# YOUR CODE HERE
for dict in waypoints:
    if dict["name"] == "a place":
        dict.update({"lon":-130, "name":"not a real place"})

# Crie um loop que escreva na tela todos os valores dos dicionarios da lista
# YOUR CODE HERE
for dict in waypoints:
    print(dict["lat"], dict["lon"], dict["name"])