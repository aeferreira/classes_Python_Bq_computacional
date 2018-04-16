
*Strings*
=========

Definição literal, iteração e indexação
---------------------------------------

As *strings* são um dos tipos de objetos mais usados na linguagem
Python. É comum um programa lidar com texto, seja porque o objetivo do
programa é precisamente o processamento de informação na forma textual,
seja simplesmente para que os resultados de um programa sejam
apresentados com pequenos textos destinados a descrever esses
resultados.

Como vimos anteriormente, uma *string* é uma coleção de caracteres.

Uma maneira de criarmos *strings* num programa é defini-las
literalmente, como um **texto entre aspas**.

Na definição literal de *strings* **podemos usar 3 tipos diferentes de
aspas**: ``"``, ``'`` ou ``"""``.

As *aspas triplas* permitem definir literalmente uma *string* com várias
linhas.

.. code-block:: ipython3

    a = "O Neo tomou o comprimido vermelho"
    
    b ='What is the matrix?'
    
    c ="There's no spoon"
    
    d = """ Um pequeno texto que até
    ocupa várias linhas
    
    algumas das linhas estão em branco"""

"Concatenação" de strings com o operador ``+``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O operador ``+`` serve para "juntar" várias *strings*, uma operação
designada por *concatenação*.

.. code-block:: ipython3

    c = "There's no spoon"
    print('c = ', c)
    
    c = c + ', really, ' + 'none' + '.'
    
    print('c = ', c)


.. code-block:: text

    c =  There's no spoon
    c =  There's no spoon, really, none.
    

As strings têm muitas funções em comum com as listas:

-  ``len()``, ``count()``, ``in``, ``not in``
-  Indexação: ``a[i]``
-  Iteração: ``for i in a:``

Isto acontece porque as *strings* se comportam como uma **sequência de
caracteres**, tal como uma lista é uma sequência de quaisquer objetos.

Funções ``len()``, ``.count()``, operador ``in``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    c = "There's no spoon"
    print('c = ', c)
    print('len(c) =', len(c))
    
    print('c.count("s") = ', c.count('s'))
    
    print('z' in c)
    print('r' in c)
    print('ere' in c)


.. code-block:: text

    c =  There's no spoon
    len(c) = 16
    c.count("s") =  2
    False
    True
    True
    

Iteração e indexação.
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    frase = "There's no spoon"
    
    for i, c in enumerate(frase):
        print(i, c)


.. code-block:: text

    0 T
    1 h
    2 e
    3 r
    4 e
    5 '
    6 s
    7  
    8 n
    9 o
    10  
    11 s
    12 p
    13 o
    14 o
    15 n
    

.. code-block:: ipython3

    frase = "There's no spoon"
    
    for i in range(-1, -len(frase)-1, -1):
        print(i, frase[i])


.. code-block:: text

    -1 n
    -2 o
    -3 o
    -4 p
    -5 s
    -6  
    -7 o
    -8 n
    -9  
    -10 s
    -11 '
    -12 e
    -13 r
    -14 e
    -15 h
    -16 T
    

Funções associadas a *strings*
------------------------------

Existem muitas funções associadas a *strings*

Consultar a documentação oficial em
`docs.python.org <https://docs.python.org/3/library/stdtypes.html#string-methods>`__

.. figure:: images/docspython_strmethods.png
   :alt: 

**São cerca de 40!**

Imutabilidade
-------------

As *strings* são **imutáveis**.

Isto significa que (ao contrário das listas e dicionários) **não existem
funções para modificar uma** *string*.

**Não existe**, por exemplo, ``s.append('a')``.

**Todas as operações com** *strings* **resultam numa** *string*
**nova**, à qual é, geralmente, atribuído um nome (mesmo que seja o
mesmo nome da *string* original)

Podemos, por isso, usar ``s = s + 'a'``

Algumas funções úteis
---------------------

Funções ``.strip()``, ``.startswith()``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    c = "    There's no spoon      "
    print('c:')
    print(c)
    
    s = c.strip()
    print('c.strip():')
    print(s)


.. code-block:: text

    c:
        There's no spoon      
    c.strip():
    There's no spoon
    

.. code-block:: ipython3

    c = "    There's no spoon      "
    
    if s.strip().startswith('Th'):
        print('Começa por Th')


.. code-block:: text

    Começa por Th
    

Funções ``.upper()``, ``.lower()``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    c = "    There's no spoon      "
    
    c_upper = c.upper()
    print('c.upper():',c_upper)
    
    c_lower = c.lower()
    print('c.lower():',c_lower)


.. code-block:: text

    c.upper():     THERE'S NO SPOON      
    c.lower():     there's no spoon      
    

Função ``.replace()``.
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    palavra = 'pois'
    print(palavra)
    
    palavra = palavra.replace('p', 'd')
    print(palavra)


.. code-block:: text

    pois
    dois
    

Funções ``.split()`` e ``.join()``
----------------------------------

.. code-block:: ipython3

    a = "There's no spoon"
    
    b = a.split()
    c = a.split('e')
    d = a.split("'")
    
    print(b)
    print(c)
    print(d)


.. code-block:: text

    ["There's", 'no', 'spoon']
    ['Th', 'r', "'s no spoon"]
    ['There', 's no spoon']
    

A função ``.split()`` **gera uma lista de partes**, encontrando um
separador numa *string*.

O separador a encontrar é o argumento da função.

Se não se usar um argumento, considera-se que as partes são separadas
por espaços, tabs ou mudanças de linha (no inglês genericamente
designados por *white space*)

A função ``.join()`` é uma espécie de inversa de ``.split()``:
transforma **uma lista** de *strings* **numa única** *string*,
interpondo um separador:

.. code-block:: ipython3

    aas = ['Arg', 'Tyr', 'Gly', 'Asp']
    
    print(" ".join(aas))
    print("-".join(aas))
    print("".join(aas))
    print("+".join(aas))
    print("-CONH-".join(aas))


.. code-block:: text

    Arg Tyr Gly Asp
    Arg-Tyr-Gly-Asp
    ArgTyrGlyAsp
    Arg+Tyr+Gly+Asp
    Arg-CONH-Tyr-CONH-Gly-CONH-Asp
    

**Problema: transformar** ``AUGUUCAAGGAGUAAUGCCCCCGACUA`` **em**
``AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA``

.. code-block:: ipython3

    s = "AUGUUCAAGGAGUAAUGCCCCCGACUA"
    print(s)
    
    codoes = []
    for i in range(0, len(s), 3):
        # i é o início de cada codão (c)
        c = s[i] + s[i+1] + s[i+2]
        codoes.append(c)
    
    print(codoes)
    
    final = "-".join(codoes)
    print(final)


.. code-block:: text

    AUGUUCAAGGAGUAAUGCCCCCGACUA
    ['AUG', 'UUC', 'AAG', 'GAG', 'UAA', 'UGC', 'CCC', 'CGA', 'CUA']
    AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA
    

Tem de haver uma maneira mais sucinta de de juntar vários caracteres
consecutivos!

Função ``.splitlines()``
------------------------

.. code-block:: ipython3

    d = """ Um pequeno texto que até
    ocupa várias linhas
    
    algumas das linhas estão em branco"""
    
    print(d.splitlines())


.. code-block:: text

    [' Um pequeno texto que até', 'ocupa várias linhas', '', 'algumas das linhas estão em branco']
    

A função ``.splitlines()`` é praticamente equivalente a
``.split('\n')``.

É muito interessante o facto de podermos usar funções de *strings* em
conjunção com listas em compreensão:

**Problema: num texto com várias linhas, obter numa lista as linhas que
começam por uma vogal e têm menos de 20 caracteres**

.. code-block:: ipython3

    txt = """ 
     Um pequeno texto que até
    ocupa várias
    linhas
    
    mas haverá
    Algumas em branco"""
    
    a = [s.strip() for s in txt.splitlines()]
    print(a)
    a = [s for s in a if 0 < len(s) < 20]
    print(a)
    a = [s for s in a if s[0].lower() in 'aeiou']
    print(a)


.. code-block:: text

    ['', 'Um pequeno texto que até', 'ocupa várias', 'linhas', '', 'mas haverá', 'Algumas em branco']
    ['ocupa várias', 'linhas', 'mas haverá', 'Algumas em branco']
    ['ocupa várias', 'Algumas em branco']
    

"Slices" (em português: "fatias")
---------------------------------

Já vimos que podemos indexar listas e *strings*, usando [] e a posição
do elemento.

Os ``[]`` podem ser usados para um outro tipo de indexação de listas ou
*strings*: os **slices**.

Os *slices* extraem uma parte de uma lista ou *string* que podem ter
mais de um elemento.

A forma geral é ``[início : fim(exclusivé) : passo]``. O ``passo`` é
opcional.

.. code-block:: ipython3

    a = "O Neo tomou o comprimido vermelho"
    #    012345678901234567890123456789012
    
    print(a[2:5])
    print(a[0:5])
    print(a[6:-1])


.. code-block:: text

    Neo
    O Neo
    tomou o comprimido vermelh
    

.. code-block:: ipython3

    a = "O Neo tomou o comprimido vermelho"
    #    012345678901234567890123456789012
    
    print(a[ :5])
    print(a[6: ])
    print(a[ : ])
    print(a[0:12:2])


.. code-block:: text

    O Neo
    tomou o comprimido vermelho
    O Neo tomou o comprimido vermelho
    ONotmu
    

**Problema: transformar** ``AUGUUCAAGGAGUAAUGCCCCCGACUA`` **em**
``AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA``

.. code-block:: ipython3

    s = "AUGUUCAAGGAGUAAUGCCCCCGACUA"
    print(s)
    
    codoes = []
    for i in range(0, len(s), 3):
        # i é o início de cada codão
        # aqui usamos um slice
        # em vez da soma de 3 posições consecutivas.
        c = s[i:i+3]
        codoes.append(c)
    
    final = "-".join(codoes)
    print(final)


.. code-block:: text

    AUGUUCAAGGAGUAAUGCCCCCGACUA
    AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA
    

Usando uma lista em compreensão como argumento da função ``.join()`` o
programa pode ficar mais compacto:

.. code-block:: ipython3

    s = "AUGTTCAAGGAGUAAUGCCCCCGACUA"
    sf = "-".join([s[i:i+3] for i in range(0,len(s),3)])
    
    print(s)
    print(sf)


.. code-block:: text

    AUGTTCAAGGAGUAAUGCCCCCGACUA
    AUG-TTC-AAG-GAG-UAA-UGC-CCC-CGA-CUA
    

**Os** *slices* **também funcionam com listas**

.. code-block:: ipython3

    aas = ['Arg', 'Tyr', 'Gly', 'Asp']
    
    s1 = aas[ :2]
    s2 = aas[-2: ]
    s3 = aas[ : :2]
    
    print(s1)
    print(s2)
    print(s3)


.. code-block:: text

    ['Arg', 'Tyr']
    ['Gly', 'Asp']
    ['Arg', 'Gly']
    

**Os** *slices* **produzem sempre novos objetos**

**No caso de uma lista**, podemos **atribuír valores a um** *slice* **da
lista**, mudando alguns elementos de uma só vez:

.. code-block:: ipython3

    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(nums)
    nums[3:5] = [8, 9]
    print(nums)


.. code-block:: text

    [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    [1, 2, 2, 8, 9, 3, 4, 4, 4, 4]
    

**Problema: Converter uma sequência com códigos de uma letra de
aminoácidos para códigos de 3 letras, usando um dicionário para a
conversão.**

Numa secção anterior, este problema foi resolvido anteriormente da
seguinte forma:

.. code-block:: ipython3

    trans = {'A': 'Ala', 'C': 'Cys', 'E': 'Glu', 'D': 'Asp', 'G': 'Gly', 'F': 'Phe', 'I': 'Ile', 'H': 'His', 'K': 'Lys', 'M': 'Met', 'L': 'Leu', 'N': 'Asn', 'Q': 'Gln', 'P': 'Pro', 'S': 'Ser', 'R': 'Arg', 'T': 'Thr', 'W': 'Trp', 'V': 'Val', 'Y': 'Tyr'}
    
    # Problema: transformar s1 numa string
    # com os códigos de 3 letras dos aa
    s1 = 'ADKLITCWFHHWE'
    
    s3 = ''
    for aa in s1:
        s3 = s3 + trans[aa] + '-'
    
    print(s1, 'é o mesmo que ', s3)


.. code-block:: text

    ADKLITCWFHHWE é o mesmo que  Ala-Asp-Lys-Leu-Ile-Thr-Cys-Trp-Phe-His-His-Trp-Glu-
    

Podemos compactar o programa e melhorar o aspeto do resultado.

Por um lado, podemos usar uma lista em compreensão para gerar os códigos
de 3 letras (em vez de uma *string*), por outro podemos usar a função
``.join()`` para apresenta-los separados por ``-``.

.. code-block:: ipython3

    trans = {'A': 'Ala', 'C': 'Cys', 'E': 'Glu', 'D': 'Asp', 'G': 'Gly', 'F': 'Phe', 'I': 'Ile', 'H': 'His', 'K': 'Lys', 'M': 'Met', 'L': 'Leu', 'N': 'Asn', 'Q': 'Gln', 'P': 'Pro', 'S': 'Ser', 'R': 'Arg', 'T': 'Thr', 'W': 'Trp', 'V': 'Val', 'Y': 'Tyr'}
    
    s1 = 'ADKLITCWFHHWE'
    
    s3 = '-'.join([trans[aa] for aa in s1])
    
    print(s1, 'é o mesmo que', s3)


.. code-block:: text

    ADKLITCWFHHWE é o mesmo que Ala-Asp-Lys-Leu-Ile-Thr-Cys-Trp-Phe-His-His-Trp-Glu
    

**Problema: calcular o complemento reverso de uma sequência, mas
separando os codões por "-".**

.. code-block:: ipython3

    bcompl = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    a = "ATGGTTACCTAGTATTTAGGATTA"
    c = ''.join([bcompl[b] for b in a[ : :-1]])
    
    print("Seq:")
    print('-'.join([a[i:i+3] for i in range(0,len(a),3)]))
    
    print("\nComplemento reverso:")
    print('-'.join([c[i:i+3] for i in range(0,len(c),3)]))


.. code-block:: text

    Seq:
    ATG-GTT-ACC-TAG-TAT-TTA-GGA-TTA
    
    Complemento reverso:
    TAA-TCC-TAA-ATA-CTA-GGT-AAC-CAT
    
