import sys
import subprocess
import shutil
import os
import glob
from pathlib import Path
from invoke import task, run, collection

_AULAS_DIR = 'aulas/'
_SOURCE_DIR = 'source/'

nbfiles = ['1_basicos.ipynb', '2_iteracoes.ipynb',
           '3_listas_dicts.ipynb', '4_strings.ipynb',
           '5_ficheiros.ipynb', '6_defs.ipynb',
           '7_import.ipynb', '8_requests.ipynb',
           '10_scientific_modules.ipynb', '11_scipy_regression.ipynb',
           '12_scipy_pH.ipynb', '13_algoritmos.ipynb',
##            {'nb':'leftovers.ipynb', 'name':'leftovers'},
##            {'nb':'leftovers2.ipynb', 'name':'leftovers2'},
           '14_pandas.ipynb',
           'data_software.ipynb']

no_exec_nbfiles = ['1_basicos.ipynb', 'data_software.ipynb']


def generate_rsts(nbfiles):
        
    for nbf in nbfiles:
        name = _AULAS_DIR + nbf
        
        print ('=========== notebook {0} ================'.format(name))

        print('-- creating backup')
        backupname = name + '.bak'
        shutil.copy(name, backupname)
        
        if nbf not in no_exec_nbfiles:
            aaa =('jupyter nbconvert --execute --inplace --ExecutePreprocessor.kernel_name=python3 --allow-errors --to notebook %s'% name).split()
            try:
                retcode = subprocess.call(aaa, shell=True)
                if retcode < 0:
                    print("terminated by signal", -retcode, file=sys.stderr)
                elif retcode > 0:
                    print("returned", retcode, file=sys.stderr)
            except OSError as e:
                print("Execution of failed:", e, file=sys.stderr)    
            #print(subprocess.check_output(aaa))

        rst_name = name.replace('.ipynb', '.rst')
        # print ('-- converting to {0}'.format(rst_name))
        aaa = ('jupyter nbconvert --to rst %s'% name).split()
        try:
            retcode = subprocess.call(aaa, shell=True)
            if retcode < 0:
                print("terminated by signal", -retcode, file=sys.stderr)
            elif retcode > 0:
                print("returned", retcode, file=sys.stderr)
        except OSError as e:
            print("Execution of failed:", e, file=sys.stderr)    
        #print(subprocess.check_output(aaa))

        # MS-Windows fix:
        print ('-- fixing img links in {0}'.format(rst_name), end=' ')

        with open(rst_name) as f:
            alltext = f.read()

        alltext = alltext.replace('_files%5C', '_files/')
        alltext = alltext.replace(".. code:: python\n\n    %matplotlib inline\n", '')

        with open (rst_name, 'w') as f:
            f.write(alltext)
        print('done.')

    print('==== Done converting to *.rst ====')
        

def fix_code_blocks(rstfiles):
        
    for rst in rstfiles:
        name = rst
        
        print (f'=========== RST file {name} ================')

        print('-- creating backup')
        backupname = str(name) + '.bak'
        shutil.copy(str(name), backupname)
        
        with open(name) as f:
            alltext = f.read()

        print('-- fixing output blocks')
        alltext = alltext.replace('.. parsed-literal::', '.. code-block:: text')
        print('-- fixing code blocks')
        alltext = alltext.replace('.. code:: ipython3', '.. code-block:: ipython3')

        with open(name, 'w') as f:
            f.write(alltext)
        print('done.')

@task
def fix_blocks(ctx):
    """Change directives of code blocks for sphinx specific directives"""
    print("Fixing code blocks in source")
    source_dir = Path(_SOURCE_DIR)
    files = source_dir.glob('*.rst')
    fix_code_blocks(files)


def generate_slides(nbfiles):
    for nbf in nbfiles:
        name = _AULAS_DIR + nbf
        print ('--------------------'.format(name))
        aaa = ('jupyter nbconvert --to slides %s'% name).split()
        try:
            retcode = subprocess.call(aaa, shell=True)
            if retcode < 0:
                print("terminated by signal", -retcode, file=sys.stderr)
            elif retcode > 0:
                print("returned", retcode, file=sys.stderr)
        except OSError as e:
            print("Execution of failed:", e, file=sys.stderr)    
        #run('jupyter nbconvert --to slides %s'% name)


@task
def build_rst(ctx):
    """Generate .rst support files for e-book"""
    print("Generating .rst support files")
    generate_rsts(nbfiles)

@task
def clean_rst(ctx):
    """Remove .rst support files"""
    print("Removing .rst support files")
    for root, dirs, files in os.walk('aulas', topdown=False):
        for name in files:
            if name.endswith('.rst'):
                print ('removing {}'.format(name))
                os.remove(os.path.join(root, name))
            if name in nbfiles:
                backupname = name + '.bak'
                if os.path.exists(os.path.join(root, backupname)):
                    print ('removing {}'.format(name))
                    os.remove(os.path.join(root, name))
                    print ('restoring {} from backup'.format(name))
                    shutil.move(os.path.join(root, backupname),
                                os.path.join(root, name))

        for name in dirs:
            if name.endswith('_files'):
                print ('removing dir {}'.format(name))
                shutil.rmtree(os.path.join(root, name))

@task
def build_slides(ctx):
    """Generate reveal slides"""
    print("Generating reveal slide files")
    generate_slides(nbfiles)


@task
def clean_slides(ctx):
    """Remove reveal slides"""
    print("Removing reveal slide files")
    for root, dirs, files in os.walk('aulas', topdown=False):
        for name in files:
            if name.endswith('.slides.html'):
                print ('removing {}'.format(name))
                os.remove(os.path.join(root, name))

@task(pre=[clean_rst])
def clean_book(ctx):
    """Clean the _build directory"""
    print("Removing /_build")
    shutil.rmtree('_build', ignore_errors=True)

@task
def make_htmlbook(ctx):
    """Generate the html e-book"""
    print("Building e-book!")
    try:
        retcode = subprocess.call("make" + " html", shell=True)
        if retcode < 0:
            print("make was terminated by signal", -retcode, file=sys.stderr)
        elif retcode > 0:
            print("make returned", retcode, file=sys.stderr)
    except OSError as e:
        print("Execution of make html failed:", e, file=sys.stderr)    

@task(pre=[build_rst])
def build_htmlbook(ctx):
    """Generate *rst files and make the e-book"""
    make_htmlbook(ctx)

## ns = collection.Collection(build_book)
## ns.configure({
##     'run': {
##         'shell': os.environ.get('COMSPEC', os.environ.get('SHELL'))
##     }
## })