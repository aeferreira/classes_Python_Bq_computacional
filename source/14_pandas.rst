
Python "científico": biblioteca *pandas*
========================================

.. figure:: images/sci_python_pandas.png
   :alt: 

*web site*: (``pandas.pydata.org``)

.. figure:: images/pandas_web.png
   :alt: 

``Series``
----------

    ``Series`` is a one-dimensional **labeled** array capable of holding
    any data type (integers, strings, floating point numbers, Python
    objects, etc.). The axis labels are collectively referred to as the
    **index**.

.. code:: ipython3

    import pandas as pd

Uma Série (*Series*) é um conjunto (ordenado) de valores, mas cada valor
é associado a uma "etiqueta" (*label*).

Ao conjunto das etiquetas dá-se o nome de "**índice**".

Quando construímos uma Série, usando a função ``Series()``, podemos
indicar o índice.

.. code:: ipython3

    s = pd.Series([1.4, 2.2, 3.2, 6.5, 12],
                  index=['a', 'b', 'c', 'd', 'e'])
    print(s)


.. parsed-literal::

    a     1.4
    b     2.2
    c     3.2
    d     6.5
    e    12.0
    dtype: float64
    

Se não indicarmos um índice, o conjunto dos inteiros sucessivos será o
índice.

.. code:: ipython3

    s = pd.Series([1.4,2.2,3.2,6.5,12])
    print(s)


.. parsed-literal::

    0     1.4
    1     2.2
    2     3.2
    3     6.5
    4    12.0
    dtype: float64
    

As Séries podem ser construídas a partir de um dicionário, em que as
chaves são o índice.

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d)
    print(s)


.. parsed-literal::

    a    0.0
    b    1.0
    c    2.0
    dtype: float64
    

Podemos, mesmo neste caso, indicar um índice. Caso o índice tenha
elementos para além das chaves do dicionário, haverá **valores em
falta**.

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)


.. parsed-literal::

    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64
    

O uso do marcador ``NaN`` para indicar **valores em falta** e a
existência de muitas funções de análise que levam em conta valores em
falta são uma característica muito poderosa do módulo ``pandas``.

Funções descritivas dos valores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As Séries têm algumas funções de estatística descritiva de grande
utilidade.

Note-se que, em geral, **os valores em falta são ignorados nos
cálculos**.

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    print('\nMédia =', s.mean())


.. parsed-literal::

    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64
    
    Média = 1.0
    

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    print('-----')
    print(s.describe())


.. parsed-literal::

    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64
    -----
    count    3.0
    mean     1.0
    std      1.0
    min      0.0
    25%      0.5
    50%      1.0
    75%      1.5
    max      2.0
    dtype: float64
    

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s.cumsum())


.. parsed-literal::

    b    1.0
    c    3.0
    d    NaN
    a    3.0
    dtype: float64
    

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    
    print(s.values)
    print(s.index.values)


.. parsed-literal::

    [  1.   2.  nan   0.]
    ['b' 'c' 'd' 'a']
    

Indexação e operações vetoriais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As Séries podem ser usadas com indexação por números inteiros,
comportando-se como uma lista ou um *array* do ``numpy``.

A função ``len()``\ também funciona com séries.

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(len(s))
    print(s[0])
    print(s[-1])


.. parsed-literal::

    4
    1.0
    0.0
    

As Séries podem ser usadas **como dicionários: as etiquetas comportam-se
como chaves** e são usadas para indexar uma Série. para obter um valor
(e também para modificar um valor).

Tal como nos dicionários, o operador ``in`` **testa a existência de uma
etiqueta**.

.. code:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    print('-----------')
    print(s['b'])
    print(s.c) # notação abreviada
    print('z' in s)
    print('d' in s)


.. parsed-literal::

    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64
    -----------
    1.0
    2.0
    False
    True
    

Mas as Séries são muito mais poderosas: elas comportam-se como *arrays*
do módulo ``numpy``. Podemos usar:

-  *slices*
-  **operações vetoriais**.

.. code:: ipython3

    d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
    s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
    print(s)
    
    print(s[:3])


.. parsed-literal::

    b    1.0
    c    3.0
    d    NaN
    e    1.8
    a    0.5
    dtype: float64
    b    1.0
    c    3.0
    d    NaN
    dtype: float64
    

.. code:: ipython3

    d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
    s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
    print(s)
    
    print(s**2)


.. parsed-literal::

    b    1.0
    c    3.0
    d    NaN
    e    1.8
    a    0.5
    dtype: float64
    b    1.00
    c    9.00
    d     NaN
    e    3.24
    a    0.25
    dtype: float64
    

.. code:: ipython3

    d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
    s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
    print(s)
    
    print(s[s > 1.1])


.. parsed-literal::

    b    1.0
    c    3.0
    d    NaN
    e    1.8
    a    0.5
    dtype: float64
    c    3.0
    e    1.8
    dtype: float64
    

Também muito poderoso é o facto de que, quando aplicamos operações
vetoriais sobre Séries (por exemplo, na soma de duas séries), **os
valores são "alinhados" pelos respetivos *labels*** antes da operação.
Vejamos estas duas séries:

.. code:: ipython3

    s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
    s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})
    
    print('Soma')
    print(s1 + s2)


.. parsed-literal::

    Soma
    a    1.0
    b    2.0
    e    NaN
    f    NaN
    dtype: float64
    

A soma das duas Séries resulta numa Série em que todas as etiquetas
estão presentes (**união de conjuntos**).

As que só existirem numa das Séries ou as que, numa das Séries, têm o
valor ``NaN``, terão o valor ``NaN`` no resultado final.

A função ``.dropna()`` permite eliminar os *valores em falta*.

.. code:: ipython3

    s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
    s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})
    s3 = s1 + s2
    
    print(s3.dropna())


.. parsed-literal::

    a    1.0
    b    2.0
    dtype: float64
    

``DataFrame``
-------------

    ``DataFrame`` is a **2-dimensional labeled data structure** with
    columns of potentially different types. You can think of it like a
    spreadsheet or SQL table, or a **dict of Series objects**. It is
    generally the most commonly used pandas object.

Uma *DataFrame* é um quadro bidimensional, em que cada coluna se
comporta como uma Série, mas em que existe um índice comum a todas as
colunas.

Para ilustar o uso de uma ``DataFrame``, vamos ler e processar a
informação da UniProt sobre a levedura *S. cerevisiae*.

A ``DataFrame`` terá as colunas "**ac**", "**rev**", "**n**" e
"**sequence**"

.. code:: ipython3

    def get_prots(filename):
        with open(filename) as big:
            tudo = big.read()
        return [p for p in tudo.split('//\n') if len(p) != 0]
    
    prots = get_prots('uniprot_s_cerevisiae.txt')
    
    def process_prot(p):
        linhas = p.split('\n')
        partes = linhas[0].split()
        reviewed = partes[2][0:-1]
        naa = int(partes[3])
        ac = linhas[1].split()[1][0:-1]
        for i in range(len(linhas)-1, 0, -1):
            if linhas[i].startswith('SQ'):
                break
        s = ''.join(linhas[i+1:])
        seq = ''.join(s.split())
        return {'ac':ac, 'rev':reviewed, 'n':naa, 'seq':seq}
    
    pinfo = [process_prot(p) for p in prots]
    print('Numero total de proteínas: {}'.format(len(pinfo)))
    print('A primeira proteína tem', pinfo[0]['n'], 'aminoácidos')


::


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-17-2bebe47c11d0> in <module>()
          4     return [p for p in tudo.split('//\n') if len(p) != 0]
          5 
    ----> 6 prots = get_prots('uniprot_s_cerevisiae.txt')
          7 
          8 def process_prot(p):
    

    <ipython-input-17-2bebe47c11d0> in get_prots(filename)
          1 def get_prots(filename):
    ----> 2     with open(filename) as big:
          3         tudo = big.read()
          4     return [p for p in tudo.split('//\n') if len(p) != 0]
          5 
    

    FileNotFoundError: [Errno 2] No such file or directory: 'uniprot_s_cerevisiae.txt'


Podemos construir uma ``DataFrame`` a partir de uma lista de
dicionários. As **chaves dos dicionários serão as colunas**.

.. code:: ipython3

    prots = pd.DataFrame(pinfo)
    print(len(prots))
    prots[:3]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-b95f7c7c35b6> in <module>()
    ----> 1 prots = pd.DataFrame(pinfo)
          2 print(len(prots))
          3 prots[:3]
    

    NameError: name 'pinfo' is not defined


Para inspeção rápida, as funções ``.head()`` e ``.tail()`` apresentam o
início e o fim da ``DataFrame``

.. code:: ipython3

    prots = pd.DataFrame(pinfo)
    #prots.head()
    prots.tail()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-a6febca4a1a1> in <module>()
    ----> 1 prots = pd.DataFrame(pinfo)
          2 #prots.head()
          3 prots.tail()
    

    NameError: name 'pinfo' is not defined


Podemos mudar o índice para uma das colunas.

.. code:: ipython3

    prots = prots.set_index('ac')
    prots.head()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-a06942729c02> in <module>()
    ----> 1 prots = prots.set_index('ac')
          2 prots.head()
    

    NameError: name 'prots' is not defined


A indexação com o nome de uma coluna devolve essa coluna (mas associada
ao índice).

Cada coluna comporta-se como uma Série.

.. code:: ipython3

    prots['n']


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-21-3164baf8fe02> in <module>()
    ----> 1 prots['n']
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    print(prots['n']['P31383'])
    print(prots['n'].max())
    print(prots['n'].min())
    print(prots['n'].mean())


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-ab0a3cfb0aa7> in <module>()
    ----> 1 print(prots['n']['P31383'])
          2 print(prots['n'].max())
          3 print(prots['n'].min())
          4 print(prots['n'].mean())
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    print(prots['n'].describe())


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-d18956a71c5a> in <module>()
    ----> 1 print(prots['n'].describe())
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    desc = prots['n'].describe()
    min_aa = desc['min']
    max_aa = desc['max']
    
    print('Menor proteína:', min_aa)
    print('Maior proteína:', max_aa)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-de754f1e2db9> in <module>()
    ----> 1 desc = prots['n'].describe()
          2 min_aa = desc['min']
          3 max_aa = desc['max']
          4 
          5 print('Menor proteína:', min_aa)
    

    NameError: name 'prots' is not defined


Quais são as proteínas menores e maiores?

.. code:: ipython3

    min_aa = prots['n'].describe()['min']
    
    prots[prots['n'] == min_aa]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-25-0cc7991238d5> in <module>()
    ----> 1 min_aa = prots['n'].describe()['min']
          2 
          3 prots[prots['n'] == min_aa]
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    max_aa = prots['n'].describe()['max']
    
    prots[prots['n'] == max_aa]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-abd9ebf3b827> in <module>()
    ----> 1 max_aa = prots['n'].describe()['max']
          2 
          3 prots[prots['n'] == max_aa]
    

    NameError: name 'prots' is not defined


Para obter uma linha usamos ``.loc`` e indexação por um *label*.

A linha obtida é uma *Series*.

.. code:: ipython3

    prots.loc['P31383']


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-27-06c5a4fa61c3> in <module>()
    ----> 1 prots.loc['P31383']
    

    NameError: name 'prots' is not defined


Quantos triptofanos tem a proteína P31383?

.. code:: ipython3

    prots.loc['P31383']['seq'].count('W')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-28-0f1604ad8dfa> in <module>()
    ----> 1 prots.loc['P31383']['seq'].count('W')
    

    NameError: name 'prots' is not defined


A indexação com condições sobre as colunas é muito poderosa.

Qauntas proteínas têm mais de 2000 aminoácidos?

.. code:: ipython3

    bigs = prots[prots['n'] > 2000]
    print(len(bigs))
    bigs


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-f19a0a283b3d> in <module>()
    ----> 1 bigs = prots[prots['n'] > 2000]
          2 print(len(bigs))
          3 bigs
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    # Média dos comprimentos das proteínas
    # com mais de 2000 aminoácidos
    prots[prots['n'] > 2000]['n'].mean()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-30-93dbf92eb37d> in <module>()
          1 # Média dos comprimentos das proteínas
          2 # com mais de 2000 aminoácidos
    ----> 3 prots[prots['n'] > 2000]['n'].mean()
    

    NameError: name 'prots' is not defined


De novo, qual a proteína maior?

.. code:: ipython3

    prots['n'].idxmax()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-7c6e56a5643c> in <module>()
    ----> 1 prots['n'].idxmax()
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    prots.loc[prots['n'].idxmax()]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-37a2d87ece92> in <module>()
    ----> 1 prots.loc[prots['n'].idxmax()]
    

    NameError: name 'prots' is not defined


Para aplicar funções de *strings* a toda uma coluna de uma só vez,
usamos o atributo ``.str.`` sobre essa coluna (o resultado é uma Série):

.. code:: ipython3

    prots['seq'].str.count('W')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-33-feedb36337c9> in <module>()
    ----> 1 prots['seq'].str.count('W')
    

    NameError: name 'prots' is not defined


Com uma indexação por nome, podemos inserir uma coluna nova na
``DataFrame`` (no fim).

.. code:: ipython3

    prots['W'] = prots['seq'].str.count('W')
    prots.head()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-34-32ebe5364b1f> in <module>()
    ----> 1 prots['W'] = prots['seq'].str.count('W')
          2 prots.head()
    

    NameError: name 'prots' is not defined


As ``DataFrame``\ s também têm funções descritivas, mas o facto de cada
coluna ser uma Série podemos realizar muitas análises de uma forma
simples.

.. code:: ipython3

    prots.info()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-35-747a6e6dff3c> in <module>()
    ----> 1 prots.info()
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    print(prots['rev'].value_counts())


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-36-2023e2a91a58> in <module>()
    ----> 1 print(prots['rev'].value_counts())
    

    NameError: name 'prots' is not defined


.. code:: ipython3

    # só no IPython/Jupyter notebook
    %matplotlib inline

.. code:: ipython3

    import matplotlib.pyplot as pl
    pl.ylabel('Proteins')
    pl.xlabel('Length (aa)')
    p = prots['n'].plot(kind='hist', bins=100)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-38-71f3320dfe60> in <module>()
          2 pl.ylabel('Proteins')
          3 pl.xlabel('Length (aa)')
    ----> 4 p = prots['n'].plot(kind='hist', bins=100)
    

    NameError: name 'prots' is not defined



.. image:: 14_pandas_files/14_pandas_68_1.png

