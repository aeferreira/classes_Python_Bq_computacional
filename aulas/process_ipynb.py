import sys
import subprocess
import shutil
import os

nbfiles = [
           {'nb':'1_basicos.ipynb', 'name':'1_basicos'},
           {'nb':'2_iteracoes.ipynb', 'name':'2_iteracoes'},
           {'nb':'listas.ipynb', 'name':'lista'},
           {'nb':'strings.ipynb', 'name':'strings'},
           {'nb':'defs.ipynb', 'name':'defs'},
           {'nb':'scientific_modules.ipynb', 'name':'scientific_modules'},
           {'nb':'pH.ipynb', 'name':'pH'},
           {'nb':'algoritmos.ipynb', 'name':'algoritmos'},
           {'nb':'leftovers.ipynb', 'name':'leftovers'},
           {'nb':'leftovers2.ipynb', 'name':'leftovers2'},
           {'nb':'pandas.ipynb', 'name':'pandas'}]

def process_list(nbfiles):
    for nbf in nbfiles:
        name = nbf['nb']
        
        print ('--------- converting notebook {0} -----------'.format(name))
        aaa = ('ipython nbconvert --to rst %s'% name).split()
        print (subprocess.check_output(aaa))

        # MS-Windows fix of image links:
        rst_name = name.replace('.ipynb', '.rst')
        print ('--------- fixing img links in {0} ---------'.format(rst_name))

        print ('reading %s'% rst_name)
        with open (rst_name) as f:
            alltext = f.read()

        alltext = alltext.replace('_files%5C', '_files/')

        print ('writing %s' % rst_name)
        with open (rst_name, 'w') as f:
            f.write(alltext)

        print ('--------- Done -----------------------------')

if __name__ == '__main__':
    process_list(nbfiles)