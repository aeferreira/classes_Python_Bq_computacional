from __future__ import print_function
from invoke import task, run
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
           {'nb':'13_algoritmos.ipynb', 'name':'algoritmos'},
##            {'nb':'leftovers.ipynb', 'name':'leftovers'},
##            {'nb':'leftovers2.ipynb', 'name':'leftovers2'},
           {'nb':'14_pandas.ipynb', 'name':'pandas'}]


def generate_rsts(nbfiles):
    os.chdir('aulas')
    for nbf in nbfiles:
        
        name = nbf['nb']
        
        print ('--------------------'.format(name))
        run('jupyter nbconvert --to rst %s'% name)

        # MS-Windows fix of image links:
        rst_name = name.replace('.ipynb', '.rst')
        print ('fixing img links in {0}'.format(rst_name))

        #print ('reading %s'% rst_name)
        with open (rst_name) as f:
            alltext = f.read()
        alltext = alltext.replace('_files%5C', '_files/')
        #print ('writing %s' % rst_name)
        with open (rst_name, 'w') as f:
            f.write(alltext)
        
    os.chdir('..')
    #print(os.getcwd())

def generate_slides(nbfiles):
    os.chdir('aulas')
    for nbf in nbfiles:
        name = nbf['nb']
        print ('--------------------'.format(name))
        run('jupyter nbconvert --to slides %s'% name)
        #rst_name = name.replace('.ipynb', '.rst')

    os.chdir('..')


@task
def build_rst():
    """Generate .rst support files for e-book"""
    print("Generating .rst support files")
    generate_rsts(nbfiles)

@task
def clean_rst():
    """Remove .rst support files"""
    print("Removing .rst support files")
    for root, dirs, files in os.walk('aulas', topdown=False):
        for name in files:
            if name.endswith('.rst'):
                print ('removing {}'.format(name))
                os.remove(os.path.join(root, name))
        for name in dirs:
            if name.endswith('_files'):
                print ('removing dir {}'.format(name))
                shutil.rmtree(os.path.join(root, name))

@task
def build_slides():
    """Generate reveal slides"""
    print("Generating reveal slide files")
    generate_slides(nbfiles)


@task
def clean_slides():
    """Remove reveal slides"""
    print("Removing reveal slide files")
    for root, dirs, files in os.walk('aulas', topdown=False):
        for name in files:
            if name.endswith('.slides.html'):
                print ('removing {}'.format(name))
                os.remove(os.path.join(root, name))

@task(pre=[clean_rst])
def clean_book():
    """Clean the _build directory"""
    print("Removing /_build")
    shutil.rmtree('_build', ignore_errors=True)

@task(pre=[build_rst])
def build_book():
    """Generate the html e-book"""
    print("Building e-book!")
    run("make html")