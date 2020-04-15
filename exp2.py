
fellowship = {'Aragorn':'Humano',
              'Frodo':'Hobbit',
              'Sam':'Hobbit',
              'Boromir':'Humano',
              'Merry':'Hobbit',
              'Took':'Hobbit',
              'Gandalf':'Feiticeiro',
              'Gimli':'Anão',
              'Legolas':'Elfo'}

# resultado das contagens num dicionário
# que associa espécie: nº personagens dessa espécie

contagens = {}

for espécie in fellowship.values():
    if espécie in contagens:
        contagens[espécie] = contagens[espécie] + 1
    else:
        contagens[espécie] = 1

for e, c in contagens.items():
    print(e, c)