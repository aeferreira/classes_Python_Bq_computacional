def exotic2fasta(exoticfilename, fastafilename):
    ef = open(exoticfilename)
    ff = open(fastafilename, 'w')
    
    for line in ef:
        line = line.strip() #remover \n
        if line [0:2] == "!!": # o header
            print >>ff, '>'+line[3:-3]  #retirar !!
        elif line[0] in '123456789': #continuar se forem as linhas de nums
            continue
        else:
            #remove spaces
            line = line.replace(' ', '')
            print >>ff, line
    ef.close()
    ff.close()

exotic2fasta('glo3.exotic', 'glo3.fasta')

f = open('glo3.fasta')
fasta = f.read()
f.close()

print fasta
