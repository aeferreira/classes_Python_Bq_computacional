import sys
import subprocess
import shutil
import os

nbfiles = [
           {'nb':'1_basicos.ipynb', 'name':'1_basicos'},
           {'nb':'2_iteracoes.ipynb', 'name':'2_iteracoes'},
           {'nb':'3_listas_dicts.ipynb', 'name':'3_listas_dicts'},
           {'nb':'4_strings.ipynb', 'name':'4_strings'},
           {'nb':'5_ficheiros.ipynb', 'name':'5_ficheiros'},
           {'nb':'6_defs.ipynb', 'name':'6_defs'},
           {'nb':'7_import.ipynb', 'name':'7_import'},
           {'nb':'8_requests.ipynb', 'name':'8_requests'},
           {'nb':'10_scientific_modules.ipynb', 'name':'10_scientific_modules'},
           {'nb':'11_scipy_regression.ipynb', 'name':'11_scipy_regression'},
           {'nb':'12_scipy_pH.ipynb', 'name':'12_scipy_pH'},
           {'nb':'algoritmos.ipynb', 'name':'algoritmos'},
##            {'nb':'leftovers.ipynb', 'name':'leftovers'},
##            {'nb':'leftovers2.ipynb', 'name':'leftovers2'},
           {'nb':'pandas.ipynb', 'name':'pandas'}]
def process_list(nbfiles):
    for nbf in nbfiles:
        name = nbf['nb']
        
        print ('--------- converting notebook {0} -----------'.format(name))
        aaa = ('jupyter nbconvert --to rst %s'% name).split()
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
        
        print ('--------- converting notebook {0} to slides'.format(name))
        aaa = ('jupyter nbconvert --to slides %s'% name).split()
        print (subprocess.check_output(aaa))

        print ('--------- Done -----------------------------')

if __name__ == '__main__':
    process_list(nbfiles)