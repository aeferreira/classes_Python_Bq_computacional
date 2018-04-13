
Listas e dicionários
====================

No capítulo anterior, definiu-se o conceito de coleção e mostrou-se 3 dos tipos
fundamentais de coleções na linguagem Python: as listas, as *strings* e os
dicionários.

Uma das mais poderosas técnicas associadas às coleções é a sua iteração, usando
o comando ``for``.

Neste capítulo mostra-se algumas **funções** que são específicas de cada coleção,
começando pelas **listas** e **dicionários**.

Listas
------

Recordemos: em comum com as outras coleções,

-  as listas podem ser iteradas num comando ``for``.
-  a função ``len()`` pode ser usada para determinar o numero de
   elementos de uma lista.
-  podemos testar se um elemento pertence a uma lista usando ``in``.

Vejamos algumas funções que são **específicas das listas**:

``.append()``, ``.insert()``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    a = [1, 2, 3, 4]
    print(a)
    
    a.append(10)
    
    print('\ndepois de append(10):', a)
    
    a.insert(1, 20)
    
    print('\ndepois de insert(1, 20):', a)


.. parsed-literal::

    [1, 2, 3, 4]
    
    depois de append(10): [1, 2, 3, 4, 10]
    
    depois de insert(1, 20): [1, 20, 2, 3, 4, 10]
    

``.extend()``.
~~~~~~~~~~~~~~

.. code:: ipython3

    a = [1, 2, 3, 4]
    print(a)
    
    novos = [11, 12, 13, 14]
    a.extend(novos)
    
    print('\ndepois de extend([11, 12, 13, 14]):')
    print(a)


.. code-block:: text

    [1, 2, 3, 4]
    
    depois de extend([11, 12, 13, 14]):
    [1, 2, 3, 4, 11, 12, 13, 14]
    

``.remove()``
~~~~~~~~~~~~~

.. code:: ipython3

    a = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    print(a)
    
    a.remove(3)
    
    print('\ndepois de remove(3):', a)


.. parsed-literal::

    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    
    depois de remove(3): [1, 2, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    

``.count()``.
~~~~~~~~~~~~~

.. code:: ipython3

    a = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    print(a)
    
    print('\nresultado de count(1:)')
    print(a.count(1))


.. parsed-literal::

    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    
    resultado de count(1:)
    3
    

``.append()`` como geradora de listas novas
-------------------------------------------

Recordar que as listas podem ser iteradas com o comando ``for``.

A combinação da iteração de listas com a função ``.append()`` começando
numa **lista vazia** é uma das combinações mais poderosas para gerar
novas listas.

**Problema: gerar os 40 primeiros quadrados perfeitos**
:math:`\{i^2: i=0, 1, 2,...,39\}` **pondo o resultado numa lista**

Podemos combinar ``.append()`` com ``for``:

.. code:: ipython3

    a = []
    for i in range(40):
        a.append(i**2)
    
    print(a)


.. parsed-literal::

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521]
    

**Problema: gerar os 40 primeiros quadrados perfeitos**
:math:`\{i^2: i=0, 1, 2,...,39\}`\ **, que estejam entre 400 e 800,
pondo o resultado numa lista**

Podemos combinar ``.append()`` com ``for`` e ``if``:

.. code:: ipython3

    a = []
    for i in range(40):
        q = i**2
        if q >= 400 and q <= 800:
            a.append(q)
    
    print(a)


.. parsed-literal::

    [400, 441, 484, 529, 576, 625, 676, 729, 784]
    

**Problema: somar os 10 primeiros números ímpares**
:math:`\sum\limits_{i=0}^9 2i+1`

.. code:: ipython3

    impares = []
    for i in range(10):
        impares.append(2*i + 1)
    print(impares)
    
    soma = 0
    for i in impares:
        soma = soma + i
    
    print('soma dos 10 primeiros ímpares:', soma)
    print('Pela soma de prog. aritm.',(1+19)/2*10)


.. parsed-literal::

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    soma dos 10 primeiros ímpares: 100
    Pela soma de prog. aritm. 100.0
    

Indexação
---------

As listas têm uma **numeração implícita, (a contar do zero)**, e podemos
**indexar** uma lista usando ``lista[posição]``

.. code:: ipython3

    enzimas = ['HK', 'G6PDH', 'TPI', 'Ald', 'PFK', 'PK']
    #           0       1       2      3      4      5   len()
    
    print(enzimas[0])
    print(enzimas[3])
    print(enzimas[len(enzimas) -1])


.. parsed-literal::

    HK
    Ald
    PK
    

As listas têm também uma **numeração implícita com números negativos**:
o último elemento é -1, o penúltimo -2 e assim sucessivamente.

.. code:: ipython3

    enzimas = ['HK', 'G6PDH', 'TPI', 'Ald', 'PFK', 'PK']
    #                          -4     -3     -2     -1
    
    print(enzimas[-4])
    print(enzimas[-6])
    print(enzimas[-1])


.. parsed-literal::

    TPI
    HK
    PK
    

A indexação permite usar elementos de uma lista pela sua posição

.. code:: ipython3

    a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    
    print( 2*a[1] + a[2] + 2*a[-1] )


.. parsed-literal::

    11
    

A indexação permite também **modificar** um elemento que está numa
posição

.. code:: ipython3

    a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    print(a)
    
    a[2] = 4 * 2**10 + a[-1]
    print(a)


.. parsed-literal::

    [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    [1, 1, 4100, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    

Podemos também indexar a partir da iteração de numeros inteiros

.. code:: ipython3

    a = [1, 2, 3, 2, 1]
    
    for e in a:
        print(e)
    
    print('-------- dá o mesmo resultado que -----------')
    
    for i in range(len(a)):
        print(a[i])


.. parsed-literal::

    1
    2
    3
    2
    1
    -------- dá o mesmo resultado que -----------
    1
    2
    3
    2
    1
    

**Problema: calcular as diferenças sucessivas entre os elementos de uma
lista, pondo o resultado numa lista**

.. code:: ipython3

    a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 7]
    
    difs = []
    for i in range(1, len(a)):
        d = a[i] - a[i-1]
        difs.append(d)
    
    print(a)
    print(difs)


.. parsed-literal::

    [1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 7]
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 2]
    

**Problema: mostrar que as diferenças sucessivas entre os quadrados
perfeitos, são os números ímpares (usar os 20 primeiros)**

.. code:: ipython3

    #calcular os quadrados perfeitos
    quads = []
    for i in range(20):
        quads.append(i**2)
    
    #calcular as diferenças sucessivas
    difs = []
    for i in range(1, len(quads)):
        d = quads[i] - quads[i-1]
        difs.append(d)
    
    print('quadrados perfeitos', quads)
    print('diferenças sucessivas', difs)


.. parsed-literal::

    quadrados perfeitos [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
    diferenças sucessivas [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
    

A propriedade matemática anterior foi usada por Galileu no estudo da
queda livre dos corpos.

.. figure:: images/galileu.jpg
   :alt: 

As distâncias sucessivas percorridas durante a queda para a mesma
unidade de tempo estão entre si como a sucessão dos números ímpares, o
que implica que a distância acumulada cresce segundo o quadrado do tempo
decorrido: o movimento de queda livre é uniformemente acelerado.

Listas em compreensão
---------------------

O padrão

.. code:: python

    nova_lista = []
    for i in uma_lista:
        "<geração de um novo elemento p a partir de i>"
        nova_lista.append(p)

é tão frequente, que existe uma forma mais sucinta de gerar a nova
lista:

**listas em compreensão**

Numa lista em compreensão constrói-se uma lista a partir de outra,
indicando a operação a efectuar a cada elemento da lista original.
Usa-se um comando ``for`` para percorrer a lista original.

É uma forma muito compacta de construir listas.

Como obter uma lista com numeros ímpares:

.. code:: ipython3

    impares = [2*i+1 for i in range(10)]
    
    print(impares)


.. parsed-literal::

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    

Em resumo, entre\ ``[]`` indica-se um "termo geral" e um comando ``for``
para percorrer a lista original

Um outro exemplo: obter os quadrados perfeitos entre 400 e 800

.. code:: ipython3

    quads = [i**2 for i in range(30)]
    
    quads_filtrados = [q for q in quads if q > 400 and q < 800]
    
    print(quads_filtrados)


.. parsed-literal::

    [441, 484, 529, 576, 625, 676, 729, 784]
    

Este exemplo mostra que podemos impor condições (com o comando ``if``)
aos valores da lista original.

Num outro exemplo, pretendemos obter uma lista com as diferenças
sucessivas entre quadrados perfeitos, para mostrar que são os números
ímpares:

.. code:: ipython3

    # Diferenças entre quadrados perfeitos sucessivos
    # são os numeros ímpares
    q = [i**2 for i in range(20)]
    difs = [q[i] - q[i-1] for i in range(1, len(q))]
    
    print('Quadrados: ', q)
    print('\nDiferenças:', difs)


.. parsed-literal::

    Quadrados:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
    
    Diferenças: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
    

**Problema: retirar todas as ocorrências de um elemento de uma lista**

.. code:: ipython3

    kill = 'Bad'
    a = ['Good','Nice','OK','Bad','Cool','Bad','OK']
    a_clean = [x for x in a if x != kill]
    
    print(a)
    print(a_clean)


.. parsed-literal::

    ['Good', 'Nice', 'OK', 'Bad', 'Cool', 'Bad', 'OK']
    ['Good', 'Nice', 'OK', 'Cool', 'OK']
    

**Problema: retirar todas as ocorrências dos elemento de uma "lista
negra"**

.. code:: ipython3

    black_list = ['Bad', 'So so']
    a = ['Good','So so','OK','Bad','Cool','Bad','OK']
    a_clean = [x for x in a if x not in black_list]
    
    print(a)
    print(a_clean)


.. parsed-literal::

    ['Good', 'So so', 'OK', 'Bad', 'Cool', 'Bad', 'OK']
    ['Good', 'OK', 'Cool', 'OK']
    

**Problema: obter uma lista de numeros até 300 que sejam múltiplos de 3
e de 7**

.. code:: ipython3

    mult_3_7 = [x for x in range(301) if x%7==0 and x%3==0]
    
    print(mult_3_7)


.. parsed-literal::

    [0, 21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294]
    

Leitura interessante:

`Comprehensions in Python the Jedi
way <https://gist.github.com/bearfrieze/a746c6f12d8bada03589>`__

Mais algumas funções de listas
------------------------------

``.pop()``, ``.reverse()``, ``.sort()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Todas estas funções **modificam** uma lista, tal como ``.append()``.

.. code:: ipython3

    a = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    print('lista original')
    print(a)
    
    a.reverse()
    print('\nDepois de a.reverse()')
    print(a)
    
    a.sort()
    print('\nDepois de a.sort()')
    print(a)


.. parsed-literal::

    lista original
    ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    
    Depois de a.reverse()
    ['dom', 'sab', 'sex', 'qui', 'qua', 'ter', 'seg']
    
    Depois de a.sort()
    ['dom', 'qua', 'qui', 'sab', 'seg', 'sex', 'ter']
    

.. code:: ipython3

    a = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    print('lista original')
    print(a)
    
    a.pop()
    print('Depois de a.pop()')
    print(a)
    x = a.pop(2)
    print('\nDepois de a.pop(2)   ')
    print(a)
    print('O valor retirado foi', x)


.. parsed-literal::

    lista original
    ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    Depois de a.pop()
    ['seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    
    Depois de a.pop(2)   
    ['seg', 'ter', 'qui', 'sex', 'sab']
    O valor retirado foi qua
    

Dicionários
-----------

Os dicionários são associações não ordenadas entre **chaves** e
**valores**. Cada chave é única.

Indexação e iteração
~~~~~~~~~~~~~~~~~~~~

A maneira de ler, inserir e modificar valores num dicionário é através
das suas chaves. O operador ``in`` testa a existência de uma chave num
dicionário.

.. code:: ipython3

    d = {'H':1, 'Li':3, 'Na':11, 'K':19}
    
    print('K: ', d['K'])
    print('Li:', d['Li'])
    
    d['O'] = 16
    print('O: ', d['O'])
    
    d['O'] = 18
    print('O: ', d['O'])


.. parsed-literal::

    K:  19
    Li: 3
    O:  16
    O:  18
    

.. code:: ipython3

    d = {'H':1, 'Li':3, 'Na':11, 'K':19}
    
    if 'N' in d:
        print('Existe info sobre o azoto')
    else:
        print('Não existe info sobre o azoto')


.. parsed-literal::

    Não existe info sobre o azoto
    

A **iteração** percorre as **chaves** de um dicionário:

.. code:: ipython3

    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    for k in d:
        if d[k] > 10:
            print(k, '--->', d[k])


.. parsed-literal::

    Na ---> 11
    K ---> 19
    O ---> 18
    

``.update()``
~~~~~~~~~~~~~

.. code:: ipython3

    d = {'a': 1, 'c': 3, 'b': 2}
    print(d)
    
    e = {'p': 10, 'q': 15}
    d.update(e)
    print(d)


.. parsed-literal::

    {'a': 1, 'c': 3, 'b': 2}
    {'a': 1, 'c': 3, 'b': 2, 'p': 10, 'q': 15}
    

``.clear()``
~~~~~~~~~~~~

.. code:: ipython3

    d = {'a': 1, 'c': 3, 'b': 2}
    print(d)
    
    d.clear()
    print(d)


.. parsed-literal::

    {'a': 1, 'c': 3, 'b': 2}
    {}
    

``.values()``,\ ``.items()``, ``.keys()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    for i in d.values():
        print(i)


.. parsed-literal::

    1
    3
    11
    19
    18
    

.. code:: ipython3

    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    for i in d.items():
        print(i)


.. parsed-literal::

    ('H', 1)
    ('Li', 3)
    ('Na', 11)
    ('K', 19)
    ('O', 18)
    

.. code:: ipython3

    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    for i in d.keys():
        print(i)


.. parsed-literal::

    H
    Li
    Na
    K
    O
    

``.items()`` é útil para simplificar um ciclo ``for``: podemos desdobrar
o par de valores e dar dois nomes diferentes:

.. code:: ipython3

    # compare-se com o exemplo acima...
    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    for e, n in d.items():
        if n > 10:
            print (e, '--->', n)


.. parsed-literal::

    Na ---> 11
    K ---> 19
    O ---> 18
    

.. code:: ipython3

    # Virar um dicionário "do avesso"
    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    d2 = {}
    
    for k in d:
        d2[d[k]] = k
    print(d)
    print(d2)


.. parsed-literal::

    {'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
    {1: 'H', 3: 'Li', 11: 'Na', 19: 'K', 18: 'O'}
    

.. code:: ipython3

    # Virar um dicionário "do avesso"
    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    d2 = {}
    
    for elem, na in d.items():
        d2[na] = elem
    print(d)
    print(d2)


.. parsed-literal::

    {'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
    {1: 'H', 3: 'Li', 11: 'Na', 19: 'K', 18: 'O'}
    

**Problema: Contar os diferentes valores de um dicionário**

.. code:: ipython3

    a = {'Aragorn':'Humano', 'Frodo':'Hobbit',
         'Sam':'Hobbit', 'Boromir':'Humano',
         'Merry':'Hobbit', 'Took':'Hobbit',
         'Gandalf':'Feiticeiro',
         'Gimli':'Anão','Legolas':'Elfo'}
    
    contagens = {}
    for especie in a.values():
        if especie in contagens:
            contagens[especie] = contagens[especie] + 1
        else:
            contagens[especie] = 1
    
    for e, c in contagens.items():
        print(e,c )


.. parsed-literal::

    Humano 2
    Hobbit 4
    Feiticeiro 1
    Anão 1
    Elfo 1
    

Dicionários em compreensão
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    d = {i:i**2 for i in range(10)}
    for k, v in d.items():
        print(k, '---->', v)


.. parsed-literal::

    0 ----> 0
    1 ----> 1
    2 ----> 4
    3 ----> 9
    4 ----> 16
    5 ----> 25
    6 ----> 36
    7 ----> 49
    8 ----> 64
    9 ----> 81
    

.. code:: ipython3

    # Virar um dicionário "do avesso"
    # usando um dicionário em compreensão
    d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}
    
    d2 = {na: elem for elem, na in d.items()}
    
    print(d)
    print(d2)


.. parsed-literal::

    {'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
    {1: 'H', 3: 'Li', 11: 'Na', 19: 'K', 18: 'O'}
    

``dict()``
~~~~~~~~~~

A função ``dict()`` que tenta transformar o seu argumento num
dicionário. Em particular, pode aceitar pares de valores,
interpretando-os como associações de chaves a valores.

.. code:: ipython3

    pares = [('Li', 3), ('K', 19), ('O',18)]
    
    d = dict(pares)
    print(d)


.. parsed-literal::

    {'Li': 3, 'K': 19, 'O': 18}
    

Função ``zip()``
----------------

.. code:: ipython3

    nomes = ['Enolase (S.cerevisiae)',
             'Enolase (S.pombe)',
             'Enolase (K.lactis)']
    ids = ['P00924', 'P40370', 'Q70CP7']
    
    for x in zip(ids, nomes):
        print(x)


.. parsed-literal::

    ('P00924', 'Enolase (S.cerevisiae)')
    ('P40370', 'Enolase (S.pombe)')
    ('Q70CP7', 'Enolase (K.lactis)')
    

.. code:: ipython3

    nomes = ['Enolase (S.cerevisiae)',
             'Enolase (S.pombe)',
             'Enolase (K.lactis)']
    ids = ['P00924', 'P40370', 'Q70CP7']
    
    for n, i in zip(nomes, ids):
        print(i, ':', n)


.. parsed-literal::

    P00924 : Enolase (S.cerevisiae)
    P40370 : Enolase (S.pombe)
    Q70CP7 : Enolase (K.lactis)
    

.. code:: ipython3

    nomes = ['Enolase (S.cerevisiae)',
             'Enolase (S.pombe)',
             'Enolase (K.lactis)']
    ids = ['P00924', 'P40370', 'Q70CP7']
    
    d = {n: i for i, n in zip(nomes, ids)}
    
    print(d)


.. parsed-literal::

    {'P00924': 'Enolase (S.cerevisiae)', 'P40370': 'Enolase (S.pombe)', 'Q70CP7': 'Enolase (K.lactis)'}
    

Combinando a função ``zip()`` com a função ``dict()``, a criação do
dicionário fica ainda mais sucinta:

.. code:: ipython3

    nomes = ['Enolase (S.cerevisiae)',
             'Enolase (S.pombe)',
             'Enolase (K.lactis)']
    ids = ['P00924', 'P40370', 'Q70CP7']
    
    d = dict(zip(nomes, ids))
    
    print(d)


.. parsed-literal::

    {'Enolase (S.cerevisiae)': 'P00924', 'Enolase (S.pombe)': 'P40370', 'Enolase (K.lactis)': 'Q70CP7'}
    
