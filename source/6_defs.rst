
Funções definidas pelo programador
==================================

Introdução ao problema
----------------------

Num problema das TPs, tivemos de separar uma sequência em codões e
"hifenar", várias vezes ao longo de um programa:

.. code-block:: ipython3

    seq = "AGCTGGATCCTGAACGCATAGACTAGCATGGGACTAAAGGTCCATTACTGA"
    btrans = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    comp = ''.join([btrans[b] for b in seq])
    comprev = ''.join(reversed(comp))
    
    codsseq = [seq[i:i+3] for i in range(0, len(seq), 3)]
    cadseq = "5'-"+'-'.join(codsseq)+"-3'"
    print(cadseq)
    
    codscomp = [comp[i:i+3] for i in range(0, len(comp), 3)]
    cadcomp = "3'-"+'-'.join(codscomp)+"-5'"
    print(cadcomp)
    
    codscomprev = [comprev[i:i+3] for i in range(0, len(comprev), 3)]
    cadcomprev = "5'-"+'-'.join(codscomprev)+"-3'"
    print('Complemento reverso')
    print(cadcomprev)


.. code-block:: text

    5'-AGC-TGG-ATC-CTG-AAC-GCA-TAG-ACT-AGC-ATG-GGA-CTA-AAG-GTC-CAT-TAC-TGA-3'
    3'-TCG-ACC-TAG-GAC-TTG-CGT-ATC-TGA-TCG-TAC-CCT-GAT-TTC-CAG-GTA-ATG-ACT-5'
    Complemento reverso
    5'-TCA-GTA-ATG-GAC-CTT-TAG-TCC-CAT-GCT-AGT-CTA-TGC-GTT-CAG-GAT-CCA-GCT-3'
    

A parte do programa

::

    codsseq = [seq[i:i+3] for i in range(0, len(seq), 3)]
    cadseq = "5'-"+'-'.join(codsseq)+"-3'"

repete-se várias vezes, mudando a sequência sobre a qual é aplicada
(``seq``, ``comp``, ``comprev``).

Como podemos não repetir o "texto" desta parte do programa, embora
aplicando a diferentes sequências?

**Solução: funções**

(também conhecidas como *subprogramas*, *subrotinas*, isto é,
mini-programas dentro de programas)

Já vimos várias funções, sempre disponíveis ou disponíveis após
importação de módulos:

.. code-block:: ipython3

    a = 'Uma pequena string'
    n = len(a)
    
    f = int(4.2)
    
    nA = a.count('A')
    
    a = []
    a.append(33)
    
    import math
    l = math.log(2.0)

Definição de funções com ``def``
--------------------------------

**Podemos escrever outras funções para "aumentar" a linguagem.**

Tal como na matemática, as funções transformam objetos noutros objetos:

.. figure:: images/genf.png
   :alt: 

Mas, tal como na matemática, as funções são escritas para atuar sobre
objetos genéricos (``x``):

.. figure:: images/genfx.png
   :alt: 

**Problema**: escrever uma função que, dada uma sequência, devolva a
sequência com os codoes separados por ``-``.

.. code-block:: ipython3

    def seqcods(x):
        cods = [x[i:i+3] for i in range(0,len(x),3)]
        comhifen = '-'.join(cods)
        return comhifen

Anatomia de uma função:
-----------------------

.. figure:: images/anatf.png
   :alt: 

A definição de uma função (``def``) não executa nada imediatamente.

É necessário **chamar** (ou "*invocar*") a função para esta ser usada:

.. code-block:: ipython3

    def seqcods(x):
        cods = [x[i:i+3] for i in range(0,len(x),3)]
        comhifen = '-'.join(cods)
        return comhifen
    
    a = "ATGGTTACCTAGTATTTAGGATTA"
    print(a)
    
    # A função é chamada aqui:
    s = seqcods(a)
    
    print(s)


.. code-block:: text

    ATGGTTACCTAGTATTTAGGATTA
    ATG-GTT-ACC-TAG-TAT-TTA-GGA-TTA
    

**NOTA**: O comando ``return`` pode "devolver" uma expressão complicada
(não só o nome de um objeto):

.. code-block:: ipython3

    def seqcods(x):
        return '-'.join( [x[i:i+3] for i in range(0,len(x),3)])
    
    a = "ATGGTTACCTAGTATTTAGGATTA"
    print(a)
    
    # A função é chamada aqui:
    s = seqcods(a)
    
    print(s)


.. code-block:: text

    ATGGTTACCTAGTATTTAGGATTA
    ATG-GTT-ACC-TAG-TAT-TTA-GGA-TTA
    

**Em resumo:**

A linha

``def seqcods(x):``

"regista" uma nova função, chamada ``seqcods``, que pode ser usada em
qualquer ponto do programa, da forma seguinte:

``s = seqcods(a)``

**Entrada e saída de valores quando uma função é chamada**:

.. figure:: images/fargs_ret.png
   :alt: 

Exemplo: função ``factorial()``:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    def factorial(n):
        res = 1
        for k in range(2,n+1):
            res = res * k
        return res
    
    print(factorial(200))


.. code-block:: text

    788657867364790503552363213932185062295135977687173263294742533244359449963403342920304284011984623904177212138919638830257642790242637105061926624952829931113462857270763317237396988943922445621451664240254033291864131227428294853277524242407573903240321257405579568660226031904170324062351700858796178922222789623703897374720000000000000000000000000000000000000000000000000
    

Vários tipos de funções
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    a = 'Uma pequena string'
    
    #1 argumento, 1 resultado
    print( len(a) )
    
    #1 arg, 1 res, associada a um objeto (string a)
    print( a.count('a') )
    
    #0 arg, 1 res, associada a um objeto (string a)
    print( a.upper() )


.. code-block:: text

    18
    2
    UMA PEQUENA STRING
    

.. code-block:: ipython3

    #1 arg, 0 res, associada a um objeto (lista b)
    # modifica o objeto (a lista b)
    b = [12, 24]
    
    print( b.append(36) )
    print(b)


.. code-block:: text

    None
    [12, 24, 36]
    

Além da função ``.append()``, recordar que **as listas** têm outras duas
funções deste tipo, que modificam a lista sem produzir nenhum resultado
(o resultado é a constante ``None``): ``.reverse()`` e ``.sort()``.

.. code-block:: ipython3

    b = [12, 24, 36]
    print(b)
    
    b.reverse()
    print(b)
    
    b.sort()
    print(b)


.. code-block:: text

    [12, 24, 36]
    [36, 24, 12]
    [12, 24, 36]
    

As funções podem ter mais de um argumento.

O resultado pode não ser apenas um número ou uma *string*: as funções
podem devolver uma lista inteira, um dicionário ou outros objetos mais
complexos.

.. code-block:: ipython3

    import math
    print( math.log(64, 2) )
    
    import time
    x = time.localtime(time.time())
    print(x)


.. code-block:: text

    6.0
    time.struct_time(tm_year=2018, tm_mon=4, tm_mday=8, tm_hour=18, tm_min=39, tm_sec=43, tm_wday=6, tm_yday=98, tm_isdst=1)
    

**Problema**: eliminar valores de uma lista que pertençam a uma "lista
negra"

.. code-block:: ipython3

    def elimin_black(uma_lista, black_list):
        res = [i for i in uma_lista if i not in black_list]
        return res
    
    a = [1, 2, 4, 'um', 'dois', 3, 42, 'quatro']
    print(a)
    
    black = [1, 2, 'um', 'dois']
    print ('\nA eliminar:', black)
    
    clean = elimin_black(a, black)
    print(clean)


.. code-block:: text

    [1, 2, 4, 'um', 'dois', 3, 42, 'quatro']
    
    A eliminar: [1, 2, 'um', 'dois']
    [4, 3, 42, 'quatro']
    

**Problema**: dado um **nome** de um ficheiro de texto, escrever uma
função para **ler o conteúdo do ficheiro para uma lista de linhas sem o
``\n`` no final, excluíndo as linhas vazias**.

.. code-block:: ipython3

    def ler_fich(nome):
        linhas = []
        with open(nome) as a:
            for linha in a:
                linha = linha.strip()
                if len(linha) > 0:
                    linhas.append(linha)
        return linhas
    
    todos = ler_fich('gre3.txt')
    
    for i in todos:
        print(i)


.. code-block:: text

    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIR
    KAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVP
    FEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDL
    LRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTL
    FENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQEL
    KDISALNANIRFNDPWTWLDGKFPTFA
    

**Problema**: eliminar valores repetidos numa lista

.. code-block:: ipython3

    def elimin_reps(uma_lista):
        res = []
        for i in uma_lista:
            if i not in res:
                res.append(i)  
        return res
    
    uma_lista = [1, 2, 4, 7, 7, 5, 8, 8, 9, 10]
    print(uma_lista)
    
    clean = elimin_reps(uma_lista)
    print(clean)


.. code-block:: text

    [1, 2, 4, 7, 7, 5, 8, 8, 9, 10]
    [1, 2, 4, 7, 5, 8, 9, 10]
    

Note-se que na função é criada uma lista nova:

::

    res = []

    ...
          res.append(i)

e é esta lista que é o **resultado** da função.

**Problema**: eliminar valores repetidos numa lista, mas sem ser
devolvida uma lista nova como resultado. Isto é, a função recebe uma
lista e modifica-a, não havendo ``return``.

.. code-block:: ipython3

    def elimin_reps2(uma_lista):
        res = []
        for i in uma_lista:
            if i not in res:
                res.append(i)  
        uma_lista[:] = res
    
    uma_lista = [1, 2, 4, 7, 7, 5, 8, 8, 9, 10]
    print('Antes', uma_lista)
    
    elimin_reps2(uma_lista)
    # não havendo return NÃO se dá um nome
    # ao resultado
    
    print('Depois', uma_lista)


.. code-block:: text

    Antes [1, 2, 4, 7, 7, 5, 8, 8, 9, 10]
    Depois [1, 2, 4, 7, 5, 8, 9, 10]
    

O que significa ``uma_lista[:] = res`` ?

Usa-se um *slice* para toda a lista (``uma_lista[:]`` significa todos os
elementos do princípio o fim)e atribuí-se a esse *slice* uma lista nova.
Assim, toda a lista é modificada.

**Nota**: não é possível usar esta técnica com *strings*. As *strings*
são imutáveis.

Se as funções tiverem resultados é possível usá-las em cadeia:

.. code-block:: ipython3

    def elimin_reps(uma_lista):
        res = []
        for i in uma_lista:
            if i not in res:
                res.append(i)  
        return res
    def elimin_black(uma_lista, black_list):
        return [i for i in uma_lista if i not in black_list]
    
    a = [1, 2, 4, 'um', 'dois', 3, 3, 37, 42, 42, 'quatro']
    black = [1, 2, 'um', 'dois']
    
    clean = elimin_reps(elimin_black(a, black))
    print(clean)


.. code-block:: text

    [4, 3, 37, 42, 'quatro']
    

Âmbito dos nomes dentro de uma função
-------------------------------------

.. code-block:: ipython3

    def recta(m, b, x):
        print('Para x =', x)
        print('com m =', m)
        print('com b =', b)
        r1 = m*x
        r0 = b
        return(r1 + r0)
    
    x, c1, c0 = 2.0, 3.0, 2.0
    
    res = recta(c1, c0, x)
    
    print('Resultado:', res)


.. code-block:: text

    Para x = 2.0
    com m = 3.0
    com b = 2.0
    Resultado: 8.0
    

Este programa corre sem problemas.

Note-se que podemos usar a função ``print()`` dentro de uma função.

.. code-block:: ipython3

    def recta(m, b, x):
        r1, r0 = m*x, b
        return r1 + r0
    
    m, b, x = 2.0, 3.0, 2.0
    res = recta(m, b, x)
    
    print('Para x =', x, 'm =', m, 'b =', b)
    print('m*x =', r1, 'b =', r0)
    print('Resultado:', res)


.. code-block:: text

    Para x = 2.0 m = 2.0 b = 3.0
    

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-f26c93717bbe> in <module>()
          7 
          8 print('Para x =', x, 'm =', m, 'b =', b)
    ----> 9 print('m*x =', r1, 'b =', r0)
         10 print('Resultado:', res)
    

    NameError: name 'r1' is not defined


O que se passou aqui?

Os nomes usados dentro da função ``r1`` e ``r0`` são locais: pertencem
ao **âmbito** da função.

Qualquer parte do programa "exterior" à função não consegue "ver" esses
nomes. Daí o erro durante a execução.

O mesmo acontece aos próprios nomes locais dos **argumentos** da função:

.. code-block:: ipython3

    def recta2(m2, b2, x):
        r1, r0 = m2*x, b2
        return r1 + r0
    
    m, b, x = 2.0, 3.0, 2.0
    res = recta2(m, b, x)
    
    print('Para x =', x, 'm2 =', m2, 'b2 =', b2)
    print('Resultado:', res)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-92c7134da27b> in <module>()
          6 res = recta2(m, b, x)
          7 
    ----> 8 print('Para x =', x, 'm2 =', m2, 'b2 =', b2)
          9 print('Resultado:', res)
    

    NameError: name 'm2' is not defined


.. code-block:: ipython3

    def recta(m, b, x):
        print('Dentro da função --------')
        print('m =', m, 'b =', b, 'x =', x)
        print('-------------------------')
        x = m * x + b
        return x
    
    m = 2
    b = 2
    x = 4
    
    res = recta(m + 3, b + 3, x * x)
    
    print('m =', m, 'b =', b, 'x =', x)
    print('\nResultado:', res)


.. code-block:: text

    Dentro da função --------
    m = 5 b = 5 x = 16
    -------------------------
    m = 2 b = 2 x = 4
    
    Resultado: 85
    

Este programa corre sem problemas!

Mas cada um dos nomes ``m``, ``b``, ``x`` é usado em dois contextos e
tem valores diferentes:

-  O contexto local, quando estão "dentro" da função.
-  O contexto global, quando estão "fora da função".

Fora da função, os valores globais são:

::

    m = 2
    b = 2
    x = 4

Estes valores não são modificados fora da função e são apresentados pela
função ``print()`` no final.

Dentro da função estes nomes são, em primeiro lugar, usados como os
argumentos da função.

Pela **maneira como a função é chamada**, estes valores são:

::

    m = 5
    b = 5
    x = 16

O nome ``x`` é modificado dentro da função (``x = m * x + b``) ficando
com o valor final 85 e é este valor que é o resultado da função
(``return x``).

Quando a função termina e estamos de novo "de fora" da função, o valor
de ``x`` volta a ser 4, uma vez que voltamos a um contexto "global".

Valores *por omissão* em argumentos de funções
----------------------------------------------

.. code-block:: ipython3

    def mix(a=1, b=0):
        c = a + b
        print('a =', a, 'b =', b, '--> return =', c)
        return c
    
    x = mix()
    
    x = mix(b=3)
    
    x = mix(a=2, b=3)
    
    x = mix(2,3)


.. code-block:: text

    a = 1 b = 0 --> return = 1
    a = 1 b = 3 --> return = 4
    a = 2 b = 3 --> return = 5
    a = 2 b = 3 --> return = 5
    

.. code-block:: ipython3

    def factorial(n, trace=False):
        p = 1
        for i in range(2,n+1):
            p = p * i
            if trace:
                print(i, p)
        return p
    
    f20 = factorial(20)
    print('O factorial de 20 é', f20)


.. code-block:: text

    O factorial de 20 é 2432902008176640000
    

.. code-block:: ipython3

    def factorial(n, trace=False):
        p = 1
        for i in range(2,n+1):
            p = p * i
            if trace:
                print(i, p)
        return p
    
    f20 = factorial(20, trace=True)
    print('O factorial de 20 é', f20)


.. code-block:: text

    2 2
    3 6
    4 24
    5 120
    6 720
    7 5040
    8 40320
    9 362880
    10 3628800
    11 39916800
    12 479001600
    13 6227020800
    14 87178291200
    15 1307674368000
    16 20922789888000
    17 355687428096000
    18 6402373705728000
    19 121645100408832000
    20 2432902008176640000
    O factorial de 20 é 2432902008176640000
    
