with open('uniprot_scerevisiae_reviewed.fasta') as datafile:
    tudo = datafile.read()

blocks = tudo.split('>')

dictseqs = {}

for b in blocks:
    if b != '':
        lines = b.splitlines()
        header = lines[0]
        seq = ''.join(lines[1:])
        # retirar o Uniprot Id do header
        parts = header.split('|')
        # separando por | um header, o ac está na posição 1
        ac = parts[1]

        # finalmente, por o resultado no dicionário
        dictseqs[ac] = seq


# Ver algumas proteínas...
for ac in ['P28240','P38832','P36084']:
    print(f'{ac}: {dictseqs[ac]}\n')
