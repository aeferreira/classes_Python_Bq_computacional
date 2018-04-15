
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

.. code-block:: ipython3

    import pandas as pd

Uma Série (*Series*) é um conjunto (ordenado) de valores, mas cada valor
é associado a uma "etiqueta" (*label*).

Ao conjunto das etiquetas dá-se o nome de "**índice**".

Quando construímos uma Série, usando a função ``Series()``, podemos
indicar o índice.

.. code-block:: ipython3

    s = pd.Series([1.4, 2.2, 3.2, 6.5, 12],
                  index=['a', 'b', 'c', 'd', 'e'])
    print(s)


.. code-block:: text

    a     1.4
    b     2.2
    c     3.2
    d     6.5
    e    12.0
    dtype: float64
    

Se não indicarmos um índice, o conjunto dos inteiros sucessivos será o
índice.

.. code-block:: ipython3

    s = pd.Series([1.4,2.2,3.2,6.5,12])
    print(s)


.. code-block:: text

    0     1.4
    1     2.2
    2     3.2
    3     6.5
    4    12.0
    dtype: float64
    

As Séries podem ser construídas a partir de um dicionário, em que as
chaves são o índice.

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d)
    print(s)


.. code-block:: text

    a    0.0
    b    1.0
    c    2.0
    dtype: float64
    

Podemos, mesmo neste caso, indicar um índice. Caso o índice tenha
elementos para além das chaves do dicionário, haverá **valores em
falta**.

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)


.. code-block:: text

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

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    print('\nMédia =', s.mean())


.. code-block:: text

    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64
    
    Média = 1.0
    

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    print('-----')
    print(s.describe())


.. code-block:: text

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
    

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s.cumsum())


.. code-block:: text

    b    1.0
    c    3.0
    d    NaN
    a    3.0
    dtype: float64
    

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    
    print(s.values)
    print(s.index.values)


.. code-block:: text

    [  1.   2.  nan   0.]
    ['b' 'c' 'd' 'a']
    

Indexação e operações vetoriais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As Séries podem ser usadas com indexação por números inteiros,
comportando-se como uma lista ou um *array* do ``numpy``.

A função ``len()``\ também funciona com séries.

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(len(s))
    print(s[0])
    print(s[-1])


.. code-block:: text

    4
    1.0
    0.0
    

As Séries podem ser usadas **como dicionários: as etiquetas comportam-se
como chaves** e são usadas para indexar uma Série. para obter um valor
(e também para modificar um valor).

Tal como nos dicionários, o operador ``in`` **testa a existência de uma
etiqueta**.

.. code-block:: ipython3

    d = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    print('-----------')
    print(s['b'])
    print(s.c) # notação abreviada
    print('z' in s)
    print('d' in s)


.. code-block:: text

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

.. code-block:: ipython3

    d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
    s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
    print(s)
    
    print(s[:3])


.. code-block:: text

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
    

.. code-block:: ipython3

    d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
    s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
    print(s)
    
    print(s**2)


.. code-block:: text

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
    

.. code-block:: ipython3

    d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
    s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
    print(s)
    
    print(s[s > 1.1])


.. code-block:: text

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

.. code-block:: ipython3

    s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
    s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})
    
    print('Soma')
    print(s1 + s2)


.. code-block:: text

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

.. code-block:: ipython3

    s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
    s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})
    s3 = s1 + s2
    
    print(s3.dropna())


.. code-block:: text

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

.. code-block:: ipython3

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


.. code-block:: text

    Numero total de proteínas: 6816
    A primeira proteína tem 316 aminoácidos
    

Podemos construir uma ``DataFrame`` a partir de uma lista de
dicionários. As **chaves dos dicionários serão as colunas**.

.. code-block:: ipython3

    prots = pd.DataFrame(pinfo)
    print(len(prots))
    prots[:3]


.. code-block:: text

    6816
    



.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>ac</th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>P29703</td>
          <td>316</td>
          <td>Reviewed</td>
          <td>MEEYDYSDVKPLPIETDLQDELCRIMYTEDYKRLMGLARALISLNE...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>P36001</td>
          <td>430</td>
          <td>Reviewed</td>
          <td>MDDISGRQTLPRINRLLEHVGNPQDSLSILHIAGTNGKETVSKFLT...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>P08524</td>
          <td>352</td>
          <td>Reviewed</td>
          <td>MASEKEIRRERFLNVFPKLVEELNASLLAYGMPKEACDWYAHSLNY...</td>
        </tr>
      </tbody>
    </table>
    </div>



Para inspeção rápida, as funções ``.head()`` e ``.tail()`` apresentam o
início e o fim da ``DataFrame``

.. code-block:: ipython3

    prots = pd.DataFrame(pinfo)
    #prots.head()
    prots.tail()




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>ac</th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>6811</th>
          <td>A0A1S0T058</td>
          <td>133</td>
          <td>Unreviewed</td>
          <td>MSETCSSSLALLHKILHIHSHTPSVYYNICISVRILTSERLQCFFF...</td>
        </tr>
        <tr>
          <th>6812</th>
          <td>A0A1S0T090</td>
          <td>108</td>
          <td>Unreviewed</td>
          <td>MYKVSACGVRIMSGISEIWIGELRDYKYALRLDREEYPAVLVYEYD...</td>
        </tr>
        <tr>
          <th>6813</th>
          <td>A0A1S0T072</td>
          <td>145</td>
          <td>Unreviewed</td>
          <td>MAILLPLKSILPWCCITFSFLLSSSGSISHSTASSSITLTKSSKPT...</td>
        </tr>
        <tr>
          <th>6814</th>
          <td>A0A1S0T069</td>
          <td>239</td>
          <td>Unreviewed</td>
          <td>MMPTYLGKLTWSYFFTTLGLACAYNVTEQMEFDQFKSDYLACLAPE...</td>
        </tr>
        <tr>
          <th>6815</th>
          <td>A0A1S0T004</td>
          <td>163</td>
          <td>Unreviewed</td>
          <td>MEMHWITLVAFIATFFNLAATSINNSSLPDVDLTNPLRFFTNIPAG...</td>
        </tr>
      </tbody>
    </table>
    </div>



Podemos mudar o índice para uma das colunas.

.. code-block:: ipython3

    prots = prots.set_index('ac')
    prots.head()




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
        </tr>
        <tr>
          <th>ac</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>P29703</th>
          <td>316</td>
          <td>Reviewed</td>
          <td>MEEYDYSDVKPLPIETDLQDELCRIMYTEDYKRLMGLARALISLNE...</td>
        </tr>
        <tr>
          <th>P36001</th>
          <td>430</td>
          <td>Reviewed</td>
          <td>MDDISGRQTLPRINRLLEHVGNPQDSLSILHIAGTNGKETVSKFLT...</td>
        </tr>
        <tr>
          <th>P08524</th>
          <td>352</td>
          <td>Reviewed</td>
          <td>MASEKEIRRERFLNVFPKLVEELNASLLAYGMPKEACDWYAHSLNY...</td>
        </tr>
        <tr>
          <th>P28003</th>
          <td>413</td>
          <td>Reviewed</td>
          <td>MGLYSPESEKSQLNMNYIGKDDSQSIFRRLNQNLKASNNNNDSNKN...</td>
        </tr>
        <tr>
          <th>Q99341</th>
          <td>161</td>
          <td>Reviewed</td>
          <td>MSLYQSIVFIARNVVNSITRILHDHPTNSSLITQTYFITPNHSGKN...</td>
        </tr>
      </tbody>
    </table>
    </div>



A indexação com o nome de uma coluna devolve essa coluna (mas associada
ao índice).

Cada coluna comporta-se como uma Série.

.. code-block:: ipython3

    prots['n']




.. code-block:: text

    ac
    P29703         316
    P36001         430
    P08524         352
    P28003         413
    Q99341         161
    P53913         173
    P38297         855
    P39012         614
    P22146         559
    P38631        1876
    P43557         207
    P53233         369
    Q12676         427
    P32614         470
    P32791         686
    P38310         465
    P18852         110
    P42837         879
    Q08967         793
    P23900         669
    Q05015         223
    P11710         512
    Q08559         129
    P36033         711
    Q12473         712
    Q12209         686
    Q12029         327
    P32805         299
    P36170        1169
    P39712        1322
                  ... 
    A0A1S0T076     103
    A0A1S0T0A7     110
    A0A1S0T0B4     122
    A0A1S0T0A4     124
    A0A1S0T0C1     109
    A0A1S0T0A9     120
    A0A1S0T066     135
    A0A1S0T088     113
    A0A1S0T045     103
    A0A1S0T073     164
    A0A1S0T062     147
    A0A1S0SZZ3     104
    A0A1S0SZN9     130
    A0A1S0T0D1     108
    A0A1S0T0A0     125
    A0A1S0T093     113
    A0A1S0SZW7     133
    A0A1S0T0B3     101
    A0A1S0T034     149
    A0A1S0T0B0     113
    A0A1S0T059     101
    A0A1S0T0A8     108
    A0A1S0T086     136
    A0A1S0T0B6     113
    A0A1S0T065     137
    A0A1S0T058     133
    A0A1S0T090     108
    A0A1S0T072     145
    A0A1S0T069     239
    A0A1S0T004     163
    Name: n, Length: 6816, dtype: int64



.. code-block:: ipython3

    print(prots['n']['P31383'])
    print(prots['n'].max())
    print(prots['n'].min())
    print(prots['n'].mean())


.. code-block:: text

    635
    4910
    16
    445.49838615023475
    

.. code-block:: ipython3

    print(prots['n'].describe())


.. code-block:: text

    count    6816.000000
    mean      445.498386
    std       380.358091
    min        16.000000
    25%       169.000000
    50%       352.000000
    75%       585.000000
    max      4910.000000
    Name: n, dtype: float64
    

.. code-block:: ipython3

    desc = prots['n'].describe()
    min_aa = desc['min']
    max_aa = desc['max']
    
    print('Menor proteína:', min_aa)
    print('Maior proteína:', max_aa)


.. code-block:: text

    Menor proteína: 16.0
    Maior proteína: 4910.0
    

Quais são as proteínas menores e maiores?

.. code-block:: ipython3

    min_aa = prots['n'].describe()['min']
    
    prots[prots['n'] == min_aa]




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
        </tr>
        <tr>
          <th>ac</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Q3E775</th>
          <td>16</td>
          <td>Reviewed</td>
          <td>MLSLIFYLRFPSYIRG</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code-block:: ipython3

    max_aa = prots['n'].describe()['max']
    
    prots[prots['n'] == max_aa]




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
        </tr>
        <tr>
          <th>ac</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Q12019</th>
          <td>4910</td>
          <td>Reviewed</td>
          <td>MSQDRILLDLDVVNQRLILFNSAFPSDAIEAPFHFSNKESTSENLD...</td>
        </tr>
      </tbody>
    </table>
    </div>



Para obter uma linha usamos ``.loc`` e indexação por um *label*.

A linha obtida é uma *Series*.

.. code-block:: ipython3

    prots.loc['P31383']




.. code-block:: text

    n                                                    635
    rev                                             Reviewed
    seq    MSGARSTTAGAVPSAATTSTTSTTSNSKDSDSNESLYPLALLMDEL...
    Name: P31383, dtype: object



Quantos triptofanos tem a proteína P31383?

.. code-block:: ipython3

    prots.loc['P31383']['seq'].count('W')




.. code-block:: text

    7



A indexação com condições sobre as colunas é muito poderosa.

Qauntas proteínas têm mais de 2000 aminoácidos?

.. code-block:: ipython3

    bigs = prots[prots['n'] > 2000]
    print(len(bigs))
    bigs


.. code-block:: text

    37
    



.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
        </tr>
        <tr>
          <th>ac</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Q06179</th>
          <td>2628</td>
          <td>Reviewed</td>
          <td>MMFPINVLLYKWLIFAVTFLWSCKILLRKLLGINITWINLFKLEIC...</td>
        </tr>
        <tr>
          <th>P33892</th>
          <td>2672</td>
          <td>Reviewed</td>
          <td>MTAILNWEDISPVLEKGTRESHVSKRVPFLQDISQLVRQETLEKPQ...</td>
        </tr>
        <tr>
          <th>Q12680</th>
          <td>2145</td>
          <td>Reviewed</td>
          <td>MPVLKSDNFDPLEEAYEGGTIQNYNDEHHLHKSWANVIPDKRGLYD...</td>
        </tr>
        <tr>
          <th>P32874</th>
          <td>2273</td>
          <td>Reviewed</td>
          <td>KGKTITHGQSWGARRIHSHFYITIFTITCIRIGQYKLALYLDPYRF...</td>
        </tr>
        <tr>
          <th>P19158</th>
          <td>3079</td>
          <td>Reviewed</td>
          <td>MSQPTKNKKKEHGTDSKSSRMTRTLVNHILFERILPILPVESNLST...</td>
        </tr>
        <tr>
          <th>P39526</th>
          <td>2014</td>
          <td>Reviewed</td>
          <td>MANRSLKKVIETSSNNGHDLLTWITTNLEKLICLKEVNDNEIQEVK...</td>
        </tr>
        <tr>
          <th>P18963</th>
          <td>3092</td>
          <td>Reviewed</td>
          <td>MNQSDPQDKKNFPMEYSLTKHLFFDRLLLVLPIESNLKTYADVEAD...</td>
        </tr>
        <tr>
          <th>Q12019</th>
          <td>4910</td>
          <td>Reviewed</td>
          <td>MSQDRILLDLDVVNQRLILFNSAFPSDAIEAPFHFSNKESTSENLD...</td>
        </tr>
        <tr>
          <th>P25655</th>
          <td>2108</td>
          <td>Reviewed</td>
          <td>MLSATYRDLNTASNLETSKEKQAAQIVIAQISLLFTTLNNDNFESV...</td>
        </tr>
        <tr>
          <th>P33334</th>
          <td>2413</td>
          <td>Reviewed</td>
          <td>MSGLPPPPPGFEEDSDLALPPPPPPPPGYEIEELDNPMVPSSVNED...</td>
        </tr>
        <tr>
          <th>Q00416</th>
          <td>2231</td>
          <td>Reviewed</td>
          <td>MNSNNPDNNNSNNINNNNKDKDIAPNSDVQLATVYTKAKSYIPQIE...</td>
        </tr>
        <tr>
          <th>P48415</th>
          <td>2195</td>
          <td>Reviewed</td>
          <td>MTPEAKKRKNQKKKLKQKQKKAAEKAASHSEEPLELPESTINSSFN...</td>
        </tr>
        <tr>
          <th>P32600</th>
          <td>2474</td>
          <td>Reviewed</td>
          <td>MNKYINKYTTPPNLLSLRQRAEGKHRTRKKLTHKSHSHDDEMSTTS...</td>
        </tr>
        <tr>
          <th>P38811</th>
          <td>3744</td>
          <td>Reviewed</td>
          <td>MSLTEQIEQFASRFRDDDATLQSRYSTLSELYDIMELLNSPEDYHF...</td>
        </tr>
        <tr>
          <th>Q03280</th>
          <td>3268</td>
          <td>Reviewed</td>
          <td>MVLFTRCEKARKEKLAAGYKPLVDYLIDCDTPTFLERIEAIQEWDR...</td>
        </tr>
        <tr>
          <th>P35169</th>
          <td>2470</td>
          <td>Reviewed</td>
          <td>MEPHEEQIWKSKLLKAANNDMDMDRNVPLAPNLNVNMNMKMNASRN...</td>
        </tr>
        <tr>
          <th>P35194</th>
          <td>2493</td>
          <td>Reviewed</td>
          <td>MAKQRQTTKSSKRYRYSSFKARIDDLKIEPARNLEKRVHDYVESSH...</td>
        </tr>
        <tr>
          <th>Q07878</th>
          <td>3144</td>
          <td>Reviewed</td>
          <td>MLESLAANLLNRLLGSYVENFDPNQLNVGIWSGDVKLKNLKLRKDC...</td>
        </tr>
        <tr>
          <th>Q00955</th>
          <td>2233</td>
          <td>Reviewed</td>
          <td>MSEESLFESSPQKMEYEITNYSERHTELPGHFIGLNTVDKLEESPL...</td>
        </tr>
        <tr>
          <th>P38111</th>
          <td>2368</td>
          <td>Reviewed</td>
          <td>MESHVKYLDELILAIKDLNSGVDSKVQIKKVPTDPSSSQEYAKSLK...</td>
        </tr>
        <tr>
          <th>P38110</th>
          <td>2787</td>
          <td>Reviewed</td>
          <td>MEDHGIVETLNFLSSTKIKERNNALDELTTILKEDPERIPTKALST...</td>
        </tr>
        <tr>
          <th>P39960</th>
          <td>2167</td>
          <td>Reviewed</td>
          <td>MKGLLWSKNRKSSTASASSSSTSTSHKTTTASTASSSSPSSSSQTI...</td>
        </tr>
        <tr>
          <th>P43583</th>
          <td>2143</td>
          <td>Reviewed</td>
          <td>MTANNDDDIKSPIPITNKTLSQLKRFERSPGRPSSSQGEIKRKKSR...</td>
        </tr>
        <tr>
          <th>P25356</th>
          <td>2167</td>
          <td>Reviewed</td>
          <td>MNSIINAASKVLRLQDDVKKATIILGDILILQPINHEVEPDVENLV...</td>
        </tr>
        <tr>
          <th>P32639</th>
          <td>2163</td>
          <td>Reviewed</td>
          <td>MTEHETKDKAKKIREIYRYDEMSNKVLKVDKRFMNTSQNPQRDAEI...</td>
        </tr>
        <tr>
          <th>P50077</th>
          <td>2039</td>
          <td>Reviewed</td>
          <td>MQGRKRTLTEPFEPNTNPFGDNAAVMTENVEDNSETDGNRLESKPQ...</td>
        </tr>
        <tr>
          <th>Q12150</th>
          <td>2958</td>
          <td>Reviewed</td>
          <td>MEAISQLRGVPLTHQKDFSWVFLVDWILTVVVCLTMIFYMGRIYAY...</td>
        </tr>
        <tr>
          <th>P08678</th>
          <td>2026</td>
          <td>Reviewed</td>
          <td>MSSKPDTGSEISGPQRQEEQEQQIEQSSPTEANDRSIHDEVPKVKK...</td>
        </tr>
        <tr>
          <th>P21951</th>
          <td>2222</td>
          <td>Reviewed</td>
          <td>MMFGKKKNNGGSSTARYSAGNKYNTLSNNYALSAQQLLNASKIDDI...</td>
        </tr>
        <tr>
          <th>P36022</th>
          <td>4092</td>
          <td>Reviewed</td>
          <td>MCKNEARLANELIEFVAATVTGIKNSPKENEQAFIDYLHCQYLERF...</td>
        </tr>
        <tr>
          <th>P07149</th>
          <td>2051</td>
          <td>Reviewed</td>
          <td>MDAYSTRPLTLSHGSLEHVLLVPTASFFIASQLQEQFNKILPEPTE...</td>
        </tr>
        <tr>
          <th>P34756</th>
          <td>2278</td>
          <td>Reviewed</td>
          <td>MSSEEPHASISFPDGSHVRSSSTGTSSVNTIDATLSRPNYIKKPSL...</td>
        </tr>
        <tr>
          <th>Q00402</th>
          <td>2748</td>
          <td>Reviewed</td>
          <td>MSHNNRHKKNNDKDSSAGQYANSIDNSLSQESVSTNGVTRMANLKA...</td>
        </tr>
        <tr>
          <th>P07259</th>
          <td>2214</td>
          <td>Reviewed</td>
          <td>MATIAPTAPITPPMESTGDRLVTLELKDGTVLQGYSFGAEKSVAGE...</td>
        </tr>
        <tr>
          <th>P11075</th>
          <td>2009</td>
          <td>Reviewed</td>
          <td>MSEQNSVVNAEKGDGEISSNVETASSVNPSVKPQNAIKEEAKETNG...</td>
        </tr>
        <tr>
          <th>P40468</th>
          <td>2376</td>
          <td>Reviewed</td>
          <td>MASRFTFPPQRDQGIGFTFPPTNKAEGSSNNNQISIDIDPSGQDVL...</td>
        </tr>
        <tr>
          <th>Q06116</th>
          <td>2489</td>
          <td>Reviewed</td>
          <td>MSMLPWSQIRDVSKLLLGFMLFIISIQKIASILMSWILMLRHSTIR...</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code-block:: ipython3

    # Média dos comprimentos das proteínas
    # com mais de 2000 aminoácidos
    prots[prots['n'] > 2000]['n'].mean()




.. code-block:: text

    2564.4054054054054



De novo, qual a proteína maior?

.. code-block:: ipython3

    prots['n'].idxmax()




.. code-block:: text

    'Q12019'



.. code-block:: ipython3

    prots.loc[prots['n'].idxmax()]




.. code-block:: text

    n                                                   4910
    rev                                             Reviewed
    seq    MSQDRILLDLDVVNQRLILFNSAFPSDAIEAPFHFSNKESTSENLD...
    Name: Q12019, dtype: object



Para aplicar funções de *strings* a toda uma coluna de uma só vez,
usamos o atributo ``.str.`` sobre essa coluna (o resultado é uma Série):

.. code-block:: ipython3

    prots['seq'].str.count('W')




.. code-block:: text

    ac
    P29703        11
    P36001         5
    P08524         4
    P28003         5
    Q99341         0
    P53913         0
    P38297         5
    P39012        15
    P22146         5
    P38631        37
    P43557         1
    P53233         7
    Q12676         4
    P32614         2
    P32791        16
    P38310         7
    P18852         1
    P42837        14
    Q08967        14
    P23900        10
    Q05015         2
    P11710         7
    Q08559         1
    P36033        11
    Q12473        15
    Q12209        11
    Q12029         4
    P32805         3
    P36170         9
    P39712        20
                  ..
    A0A1S0T076     1
    A0A1S0T0A7     0
    A0A1S0T0B4     2
    A0A1S0T0A4     0
    A0A1S0T0C1     0
    A0A1S0T0A9     2
    A0A1S0T066     1
    A0A1S0T088     1
    A0A1S0T045     0
    A0A1S0T073     4
    A0A1S0T062     4
    A0A1S0SZZ3     2
    A0A1S0SZN9     0
    A0A1S0T0D1     2
    A0A1S0T0A0     2
    A0A1S0T093     3
    A0A1S0SZW7     1
    A0A1S0T0B3     0
    A0A1S0T034     2
    A0A1S0T0B0     1
    A0A1S0T059     1
    A0A1S0T0A8     0
    A0A1S0T086     6
    A0A1S0T0B6     3
    A0A1S0T065     0
    A0A1S0T058     0
    A0A1S0T090     2
    A0A1S0T072     2
    A0A1S0T069     6
    A0A1S0T004     2
    Name: seq, Length: 6816, dtype: int64



Com uma indexação por nome, podemos inserir uma coluna nova na
``DataFrame`` (no fim).

.. code-block:: ipython3

    prots['W'] = prots['seq'].str.count('W')
    prots.head()




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>n</th>
          <th>rev</th>
          <th>seq</th>
          <th>W</th>
        </tr>
        <tr>
          <th>ac</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>P29703</th>
          <td>316</td>
          <td>Reviewed</td>
          <td>MEEYDYSDVKPLPIETDLQDELCRIMYTEDYKRLMGLARALISLNE...</td>
          <td>11</td>
        </tr>
        <tr>
          <th>P36001</th>
          <td>430</td>
          <td>Reviewed</td>
          <td>MDDISGRQTLPRINRLLEHVGNPQDSLSILHIAGTNGKETVSKFLT...</td>
          <td>5</td>
        </tr>
        <tr>
          <th>P08524</th>
          <td>352</td>
          <td>Reviewed</td>
          <td>MASEKEIRRERFLNVFPKLVEELNASLLAYGMPKEACDWYAHSLNY...</td>
          <td>4</td>
        </tr>
        <tr>
          <th>P28003</th>
          <td>413</td>
          <td>Reviewed</td>
          <td>MGLYSPESEKSQLNMNYIGKDDSQSIFRRLNQNLKASNNNNDSNKN...</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Q99341</th>
          <td>161</td>
          <td>Reviewed</td>
          <td>MSLYQSIVFIARNVVNSITRILHDHPTNSSLITQTYFITPNHSGKN...</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>
    </div>



As ``DataFrame``\ s também têm funções descritivas, mas o facto de cada
coluna ser uma Série podemos realizar muitas análises de uma forma
simples.

.. code-block:: ipython3

    prots.info()


.. code-block:: text

    <class 'pandas.core.frame.DataFrame'>
    Index: 6816 entries, P29703 to A0A1S0T004
    Data columns (total 4 columns):
    n      6816 non-null int64
    rev    6816 non-null object
    seq    6816 non-null object
    W      6816 non-null int64
    dtypes: int64(2), object(2)
    memory usage: 586.2+ KB
    

.. code-block:: ipython3

    print(prots['rev'].value_counts())


.. code-block:: text

    Reviewed      6721
    Unreviewed      95
    Name: rev, dtype: int64
    

.. code-block:: ipython3

    # só no IPython/Jupyter notebook
    %matplotlib inline

.. code-block:: ipython3

    import matplotlib.pyplot as pl
    pl.ylabel('Proteins')
    pl.xlabel('Length (aa)')
    p = prots['n'].plot(kind='hist', bins=100)



.. image:: 14_pandas_files/14_pandas_68_0.png

