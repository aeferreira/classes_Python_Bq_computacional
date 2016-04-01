

def nCbeta(nome):
    f = open(nome)
    count = 0
    for linha in f:
        if linha[:4] == "ATOM":
            if linha[13:15] == "CB":
                count = count +1
    f.close()
    return count

print 'A estrutura 1hew tem', nCbeta('1hew.pdb'), 'carbonos beta'