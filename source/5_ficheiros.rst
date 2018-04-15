
Ficheiros de texto
==================

Leitura
-------

O modelo mais simples é ler todo o conteúdo de um ficheiro para uma
*string*:

.. figure:: ./images/fichs.png
   :alt: 

A leitura de um ficheiro segundo este modelo é feito através da função
``.read()``.

Mas o processo é um pouco mais complicado do que o uso simples de uma
função.

O acesso (programático) a um ficheiro existente num computador requer
que num programa se indique que esse acesso vai começar, a *abertura* de
um ficheiro e que o acesso vai terminar, o *fecho* de um ficheiro.

``.read()``, com ``open()`` e ``close()`` explícitos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    a = open('eno1.fasta')
    seq = a.read()
    a.close()
    
    print(type(seq))
    
    print('A sequência, em FASTA é')
    print(seq)


.. code-block:: text

    <class 'str'>
    A sequência, em FASTA é
    >gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]
    MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN
    DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS
    KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG
    DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA
    DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI
    GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL
    GDNAVFAGENFHHGDKL
    
    
    

``.read()``, dentro do bloco de um comando ``with``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Numa versão mais "moderna" podemos abrir e **automaticamente fechar** o
ficheiro é utilizar o comando ``with``:

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        seq = a.read()
    
    print('A sequência, em FASTA é')
    print(seq)


.. code-block:: text

    A sequência, em FASTA é
    >gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]
    MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN
    DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS
    KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG
    DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA
    DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI
    GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL
    GDNAVFAGENFHHGDKL
    
    
    

O comando ``with`` faz o ficheiro permanecer *aberto* até ao fim do
"bloco", (também aqui) indicado pelo alinhamento mais à direita de um ou
mais comandos a seguir à linha em que se encontra o ``with``. Quando
termina o bloco o ficheiro é fechado sem usar a função ``close()``.

Além de ``read()``, em que todo o conteúdo de um ficheiro é lido para
uma *string*, existem outras maneiras de ler um ficheiro.

``.readlines()``
~~~~~~~~~~~~~~~~

A função ``readlines()`` lê e separa **as linhas** de um ficheiro para
uma lista:

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        seq = a.readlines()
    
    print(seq)


.. code-block:: text

    ['>gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]\n', 'MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN\n', 'DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS\n', 'KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG\n', 'DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA\n', 'DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI\n', 'GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL\n', 'GDNAVFAGENFHHGDKL\n', '\n']
    

O que são os ``\n`` no fim das *strings*?

**Numa string,** ``\n`` **indica a mudança de linha**. (Conta como
apenas **1** caractere).

Neste caso eles aparecem porque no ficheiro original há mudanças de
linha.

Muitas vezes, é necessário elimina-los. Para isso podemos usar a função
``.strip()``:

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        seq = a.readlines()
    
    seq = [linha.strip() for linha in seq]
    print(seq)


.. code-block:: text

    ['>gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]', 'MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN', 'DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS', 'KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG', 'DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA', 'DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI', 'GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL', 'GDNAVFAGENFHHGDKL', '']
    

Ou, de uma forma sucinta, usando uma lista em compreensão:

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        seq = [linha.strip() for linha in a.readlines()]
    print(seq)


.. code-block:: text

    ['>gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]', 'MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN', 'DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS', 'KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG', 'DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA', 'DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI', 'GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL', 'GDNAVFAGENFHHGDKL', '']
    

Com ficheiros muito grandes, a leitura pelas funções ``.read()`` e
``.readlines()`` pode esgotar a memória de um computador e "congelar" um
programa.

Existe uma terceira maneira de ler um ficheiro (que não traz problemas
com ficheiros grandes):

Iteração de ficheiros com ``for``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A iteração de um ficheiro "percorre" as linhas do ficheiro**

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        for linha in a:
            linha = linha.strip()
            print('Linha:', linha)


.. code-block:: text

    Linha: >gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]
    Linha: MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN
    Linha: DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS
    Linha: KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG
    Linha: DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA
    Linha: DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI
    Linha: GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL
    Linha: GDNAVFAGENFHHGDKL
    Linha: 
    

Podemos até usar a função ``enumerate()`` com um ficheiro. São gerados
os pares de valores

``(num linha, linha)``.

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        for i, linha in enumerate(a):
            linha = linha.strip()
            print('linha', i, ':', linha)


.. code-block:: text

    linha 0 : >gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]
    linha 1 : MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVN
    linha 2 : DVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKS
    linha 3 : KTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVG
    linha 4 : DEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLA
    linha 5 : DLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQI
    linha 6 : GTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL
    linha 7 : GDNAVFAGENFHHGDKL
    linha 8 : 
    

**Problema: ler uma ficheiro FASTA e separar o cabeçalho da sequência em
duas strings (juntando toda a sequência numa só string)**

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        linhas = [k.strip() for k in a.readlines()]
    
    header = linhas[0]
    # usamos um slice de uma lista de 1 até ao fim
    outras = linhas[1:]
    # e a funçao .join() com separador vazio para
    # juntá-las
    seq = ''.join(outras)
    
    print("cabeçalho:", header)
    print('sequência, com', len(seq), 'aminoácidos:')
    print(seq)


.. code-block:: text

    cabeçalho: >gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]
    sequência, com 437 aminoácidos:
    MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVNDVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKSKTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVGDEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLADLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQIGTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEELGDNAVFAGENFHHGDKL
    

Às vezes os ficheiros não têm cabeçalho! É melhor testar se a primeira
linha começa por ">" !

.. code-block:: ipython3

    with open('eno1.fasta') as a:
        linhas = [k.strip() for k in a]
    
    if linhas[0].startswith('>'):
        header = linhas[0]
        seq = ''.join(linhas[1:])
    else:
        header = ""
        seq = ''.join(linhas)
    
    print("cabeçalho:", header)
    print('sequência, com', len(seq), 'aminoácidos:')
    print(seq)


.. code-block:: text

    cabeçalho: >gi|398366315|ref|NP_011770.3| Eno1p [Saccharomyces cerevisiae S288c]
    sequência, com 437 aminoácidos:
    MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVNDVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKSKTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVGDEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLADLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQIGTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEELGDNAVFAGENFHHGDKL
    

As linhas em branco podem por vezes causar alguns problemas. Mas é fácil
"ignora-las".

Vamos supor que o ficheiro **gre3.txt** tem o seguinte conteúdo:

--------------

::


    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1

    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIR
    KAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVP
    FEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDL
    LRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTL
    FENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQEL
    KDISALNANIRFNDPWTWLDGKFPTFA

--------------

Como separar o cabeçalho da sequência?

.. code-block:: ipython3

    with open('gre3.txt') as a:
        linhas = [k.strip() for k in a]
    
    linhas = [k for k in linhas if len(k) > 0]
        
    if linhas[0].startswith('>'):
        header = linhas[0]
        seq = ''.join(linhas[1:])
    else:
        header = ""
        seq = ''.join(linhas)
    
    print("cabeçalho:")
    print(header)
    print('sequência, com', len(seq), 'aminoácidos:')
    print(seq)


.. code-block:: text

    cabeçalho:
    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    sequência, com 327 aminoácidos:
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIRKAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVPFEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDLLRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTLFENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQELKDISALNANIRFNDPWTWLDGKFPTFA
    

Exemplo: Extração de informação de um ficheiro FASTA múltiplo.
--------------------------------------------------------------

**Problema: extraír os cabeçalhos e as sequências de um ficheiro FASTA
múltiplo. Mostrar o comprimento das proteínas e o número de triptofanos
(W)**

.. code-block:: ipython3

    with open('proteins.fasta') as a:
        tudo = a.read()
    prots = tudo.split('>')
    
    for p in prots:
        print(len(p))


.. code-block:: text

    0
    1121
    1151
    374
    551
    549
    551
    351
    556
    

.. code-block:: ipython3

    with open('proteins.fasta') as a:
        tudo = a.read()
    prots = tudo.split('>')
    prots = [p for p in prots if len(p) > 0]
    
    for p in prots:
        print(len(p))
        print(p[:30])


.. code-block:: text

    1121
    sp|P16862|PFKA2_YEAST ATP-depe
    1151
    sp|P16861|PFKA1_YEAST ATP-depe
    374
    sp|P00950|PMG1_YEAST Phosphogl
    551
    sp|P00924|ENO1_YEAST Enolase 1
    549
    sp|P30575|ENO1_CANAL Enolase 1
    551
    sp|P00925|ENO2_YEAST Enolase 2
    351
    sp|P32626|ENOPH_YEAST Enolase-
    556
    sp|P40370|ENO11_SCHPO Enolase 
    

.. code-block:: ipython3

    with open('proteins.fasta') as a:
        tudo = a.read()
    prots = tudo.split('>')
    prots = [p for p in prots if len(p) > 0]
    
    headers = []
    seqs = []
    for p in prots:
        linhas = [k.strip() for k in p.split('\n')]
        headers.append(linhas[0])
        seqs.append(''.join(linhas[1:]))
    
    for h in headers:
        print(h)


.. code-block:: text

    sp|P16862|PFKA2_YEAST ATP-dependent 6-phosphofructokinase subunit beta OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=PFK2 PE=1 SV=4
    sp|P16861|PFKA1_YEAST ATP-dependent 6-phosphofructokinase subunit alpha OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=PFK1 PE=1 SV=1
    sp|P00950|PMG1_YEAST Phosphoglycerate mutase 1 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GPM1 PE=1 SV=3
    sp|P00924|ENO1_YEAST Enolase 1 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=ENO1 PE=1 SV=3
    sp|P30575|ENO1_CANAL Enolase 1 OS=Candida albicans (strain SC5314 / ATCC MYA-2876) GN=ENO1 PE=2 SV=1
    sp|P00925|ENO2_YEAST Enolase 2 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=ENO2 PE=1 SV=2
    sp|P32626|ENOPH_YEAST Enolase-phosphatase E1 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=UTR4 PE=1 SV=2
    sp|P40370|ENO11_SCHPO Enolase 1-1 OS=Schizosaccharomyces pombe (strain 972 / ATCC 24843) GN=eno101 PE=1 SV=2
    

.. code-block:: ipython3

    with open('proteins.fasta') as a:
        tudo = a.read()
    prots = tudo.split('>')
    prots = [p for p in prots if len(p) > 0]
    
    headers = []
    seqs = []
    for p in prots:
        linhas = [k.strip() for k in p.split('\n')]
        headers.append(linhas[0])
        seqs.append(''.join(linhas[1:]))
    
    ids = []
    for h in headers:
        separados = h.split('|')
        ids.append(separados[1])
    
    for i, s  in zip(ids, seqs):
        print(i, 'tem', len(s), 'aminoácidos,', s.count('W'), 'são triptofanos')


.. code-block:: text

    P16862 tem 959 aminoácidos, 10 são triptofanos
    P16861 tem 987 aminoácidos, 12 são triptofanos
    P00950 tem 247 aminoácidos, 5 são triptofanos
    P00924 tem 437 aminoácidos, 5 são triptofanos
    P30575 tem 440 aminoácidos, 5 são triptofanos
    P00925 tem 437 aminoácidos, 5 são triptofanos
    P32626 tem 227 aminoácidos, 1 são triptofanos
    P40370 tem 439 aminoácidos, 7 são triptofanos
    

Escrita
-------

Função ``print()`` para ficheiros
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basta abrir o ficheiro em *modo de escrita* usando o argumento ``w`` na
função ``open()``. Depois, modificar a função ``print()``, com o
argumento ``file``, indicando que o resultado da escrita deve ser
*enviado* para o ficheiro.

.. code-block:: ipython3

    with open('exp.txt', 'w') as a:
        print('1, 2, 3, experiência, som, som', file=a)
        for i in range(30):
            print(i, i**0.5, file=a)

Aparentemente não aconteceu nada, mas um ficheiro novo foi criado

Vamos ler o ficheiro:

.. code-block:: ipython3

    with open('exp.txt') as a:
        print(a.read())


.. code-block:: text

    1, 2, 3, experiência, som, som
    0 0.0
    1 1.0
    2 1.4142135623730951
    3 1.7320508075688772
    4 2.0
    5 2.23606797749979
    6 2.449489742783178
    7 2.6457513110645907
    8 2.8284271247461903
    9 3.0
    10 3.1622776601683795
    11 3.3166247903554
    12 3.4641016151377544
    13 3.605551275463989
    14 3.7416573867739413
    15 3.872983346207417
    16 4.0
    17 4.123105625617661
    18 4.242640687119285
    19 4.358898943540674
    20 4.47213595499958
    21 4.58257569495584
    22 4.69041575982343
    23 4.795831523312719
    24 4.898979485566356
    25 5.0
    26 5.0990195135927845
    27 5.196152422706632
    28 5.291502622129181
    29 5.385164807134504
    
    

Função ``.write()``
~~~~~~~~~~~~~~~~~~~

Também existe a função ``.write()`` que funciona como o contrário de
``.read()``:

.. code-block:: ipython3

    tudo = """
    Um texto que ocupa
    1 linha
    2 linhas
    3 linhas
    """
    
    with open('exp2.txt', 'w') as a:
        a.write(tudo)
    with open('exp2.txt') as a:
        print(a.read())


.. code-block:: text

    
    Um texto que ocupa
    1 linha
    2 linhas
    3 linhas
    
    

**Problema: ler uma ficheiro com dados numéricos e converter o ponto
decimal em vírgula decimal**

No ficheiro ``exp.txt``, recentemente criado, podemos, de uma form
sucinta, passar os ``.`` a ``,`` ?

.. code-block:: ipython3

    with open('exp.txt') as a:
        tudo = a.read().replace('.', ',')
    
    with open('exp.txt', 'w') as a:
        a.write(tudo)
    
    with open('exp.txt') as a:
        print(a.read())


.. code-block:: text

    1, 2, 3, experiência, som, som
    0 0,0
    1 1,0
    2 1,4142135623730951
    3 1,7320508075688772
    4 2,0
    5 2,23606797749979
    6 2,449489742783178
    7 2,6457513110645907
    8 2,8284271247461903
    9 3,0
    10 3,1622776601683795
    11 3,3166247903554
    12 3,4641016151377544
    13 3,605551275463989
    14 3,7416573867739413
    15 3,872983346207417
    16 4,0
    17 4,123105625617661
    18 4,242640687119285
    19 4,358898943540674
    20 4,47213595499958
    21 4,58257569495584
    22 4,69041575982343
    23 4,795831523312719
    24 4,898979485566356
    25 5,0
    26 5,0990195135927845
    27 5,196152422706632
    28 5,291502622129181
    29 5,385164807134504
    
    

Exemplo: Extração de informação de ficheiros de resultados de metabolómica.
---------------------------------------------------------------------------

`MassTRIX <http://www.masstrix.org>`__, (*Mass TRanslator into
Pathways*) [1] é um serviço online de tratamento de dados de
metabolómica.

A funcionalidade primária é a identificação de compostos a partir de
listas de massas e intensidades obtidas por análise de amostras
biológics por Espectrometria de Massa.

O resultado da identificação é disponibilizado em vários ficheiros de
texto. Num dos formatos, cada linha do ficheiro diz respeito a um pico
de massa e apresenta, de entre outros, os compostos identificados com
aquela massa, bem como as anotações das vias celulares em que esses
compostos podem estar envolvidos.

Pretende-se ilustrar o uso programático da leitura de ficheiros e as
operações com *strings* com um exemplo da **extração da informação
contida num desses ficheiros**.

[1] K. Suhre and P. Schmitt-Kopplin (2008) MassTRIX: Mass TRanslator
Into Pathways, *Nucleic Acids Research*, **36**, Web Server issue,
W481-W484.

Exploração do formato
~~~~~~~~~~~~~~~~~~~~~

Vamos ler o ficheiro ``masses.annotated.reformat.tsv``, separar todas as
linhas para uma lista e mostrar a primeira e a última:

.. code-block:: ipython3

    name = 'masses.annotated.reformat.tsv'
    with open(name) as a:
        all_lines = [line.strip() for line in a]
    
    print('FIRST line ----------------------------')
    print(all_lines[0])
    print('LAST line -----------------------------')
    print(all_lines[-1])


.. code-block:: text

    FIRST line ----------------------------
    154.97517	7.25775e+06	120.005768420091	4	154.975098039829#154.975098039829#154.975274805989	0.464333550973771#0.464333550973771#-0.676276005999922	C00988#HMDB00816#C02287	C2H5O6P#C2H5O6P#C3H4O5	2-Phosphoglycolate;Phosphoglycolic acid ([M-H]-)#Phosphoglycolic acid (see KEGG C00988); 2-phosphonooxyacetic acid [carboxylic acid] ([M-H]-)#Hydroxymalonate;Tartronic acid;Hydroxymalonic acid;2-Hydroxymalonate;2-Hydroxymalonic acid;2-Tartronic acid ([M+Cl35]-)													ko00630;ko01100#null#null	;Glyoxylate and dicarboxylate metabolism;Metabolic pathways#null#null	null#null#null
    LAST line -----------------------------
    raw_mass	peak_height	corrected_mass	npossible	KEGG_mass	ppm	KEGG_cid	KEGG_formula	KEGG_name	uniqueID	C13	O18	N15	S34	Mg25	Mg26	Fe54	Fe57	Ca44	Cl37	K41	KEGG Pathways	KEGG Pathways descriptions	Compound in Organism(X)
    

Nas linhas deste ficheiro, os vários campos com informação estão
separados por **tabs** (o caractere ``\t``).

A última linha tem como informação os nomes de cada um destes campos
(``raw_mass peak_height`` etc)

Vamos dividir a linha 0 em várias partes, pelo separador ``\t``. As
partes obtidas são os vários campos de informação reltiva a um pico de
MS.

Já agora, vamos obter os nomes de cada campo, fazendo o mesmo à última
linha:

.. code-block:: ipython3

    name = 'masses.annotated.reformat.tsv'
    with open(name) as a:
        all_lines = [line.strip() for line in a]
    
    headers = all_lines[-1].split('\t')
    for h in headers:
        print(h)


.. code-block:: text

    raw_mass
    peak_height
    corrected_mass
    npossible
    KEGG_mass
    ppm
    KEGG_cid
    KEGG_formula
    KEGG_name
    uniqueID
    C13
    O18
    N15
    S34
    Mg25
    Mg26
    Fe54
    Fe57
    Ca44
    Cl37
    K41
    KEGG Pathways
    KEGG Pathways descriptions
    Compound in Organism(X)
    

.. code-block:: ipython3

    name = 'masses.annotated.reformat.tsv'
    with open(name) as a:
        all_lines = [line.strip() for line in a]
    
    headers = all_lines[-1].split('\t')
    line0 = all_lines[0].split('\t')
    
    info = dict(zip(headers, line0))
    
    for h in headers:
        print(h, ':', info[h])


.. code-block:: text

    raw_mass : 154.97517
    peak_height : 7.25775e+06
    corrected_mass : 120.005768420091
    npossible : 4
    KEGG_mass : 154.975098039829#154.975098039829#154.975274805989
    ppm : 0.464333550973771#0.464333550973771#-0.676276005999922
    KEGG_cid : C00988#HMDB00816#C02287
    KEGG_formula : C2H5O6P#C2H5O6P#C3H4O5
    KEGG_name : 2-Phosphoglycolate;Phosphoglycolic acid ([M-H]-)#Phosphoglycolic acid (see KEGG C00988); 2-phosphonooxyacetic acid [carboxylic acid] ([M-H]-)#Hydroxymalonate;Tartronic acid;Hydroxymalonic acid;2-Hydroxymalonate;2-Hydroxymalonic acid;2-Tartronic acid ([M+Cl35]-)
    uniqueID : 
    C13 : 
    O18 : 
    N15 : 
    S34 : 
    Mg25 : 
    Mg26 : 
    Fe54 : 
    Fe57 : 
    Ca44 : 
    Cl37 : 
    K41 : 
    KEGG Pathways : ko00630;ko01100#null#null
    KEGG Pathways descriptions : ;Glyoxylate and dicarboxylate metabolism;Metabolic pathways#null#null
    Compound in Organism(X) : null#null#null
    

Vamos extraír da linha 0

-  a massa do pico "*raw mass*", (campo 0)
-  a intensidade do pico, (campo 1)
-  os IDs dos compostos, (campo 6)
-  os nomes dos compostos (campo 8)
-  os IDs das vias (campo 21)
-  as descrições das vias (campo 22)

Havendo vários compostos possíveis em cada pico, é usado como separador
o caractere ``#``.

Podemos já separar a informação por composto.

.. code-block:: ipython3

    name = 'masses.annotated.reformat.tsv'
    use_only = ['raw_mass', 'peak_height', 'KEGG_cid', 'KEGG_name', 'KEGG Pathways', 'KEGG Pathways descriptions']
    needs_split = ['KEGG_cid', 'KEGG_name', 'KEGG Pathways', 'KEGG Pathways descriptions']
    
    with open(name) as a:
        all_lines = [line.strip() for line in a]
    
    headers = all_lines[-1].split('\t')
    line0 = all_lines[0].split('\t')
    info = {}
    for h, i in zip(headers, line0):
        if h in use_only:
            info[h] = i
    
    for n in needs_split:
        info[n] = info[n].split('#')
    
    for h in use_only:
        print(h, ':', info[h])


.. code-block:: text

    raw_mass : 154.97517
    peak_height : 7.25775e+06
    KEGG_cid : ['C00988', 'HMDB00816', 'C02287']
    KEGG_name : ['2-Phosphoglycolate;Phosphoglycolic acid ([M-H]-)', 'Phosphoglycolic acid (see KEGG C00988); 2-phosphonooxyacetic acid [carboxylic acid] ([M-H]-)', 'Hydroxymalonate;Tartronic acid;Hydroxymalonic acid;2-Hydroxymalonate;2-Hydroxymalonic acid;2-Tartronic acid ([M+Cl35]-)']
    KEGG Pathways : ['ko00630;ko01100', 'null', 'null']
    KEGG Pathways descriptions : [';Glyoxylate and dicarboxylate metabolism;Metabolic pathways', 'null', 'null']
    

Quanto à informação relativa às vias em que cada composto pode estar
envolvido, podemos reparar que:

1. Um composto pde ter várias vias, separadas por ``;``.

2. Um composto pode não ter nenhuma via. neste caso, aparece a anotação
   "null".

Finalmente, vamos transformar a informação relativa às vias (quer os IDs
quer as descrições) em **listas**.

Repare-se que ainda são *strings* e que usam como separador o ``;`` para
delimitar várias vias.

.. code-block:: ipython3

    name = 'masses.annotated.reformat.tsv'
    use_only = ['raw_mass', 'peak_height', 'KEGG_cid', 'KEGG_name', 'KEGG Pathways', 'KEGG Pathways descriptions']
    needs_split = ['KEGG_cid', 'KEGG_name', 'KEGG Pathways', 'KEGG Pathways descriptions']
    needs_more_split = ['KEGG Pathways', 'KEGG Pathways descriptions']
    
    with open(name) as a:
        all_lines = [line.strip() for line in a]
    
    headers = all_lines[-1].split('\t')
    line0 = all_lines[0].split('\t')
    info = {}
    for h, i in zip(headers, line0):
        if h in use_only:
            info[h] = i
    
    for n in needs_split:
        info[n] = info[n].split('#')
    
    for n in needs_more_split:
        info[n] = [p.split(';') for p in info[n]]
    
    for h in use_only:
        print(h, ':', info[h])


.. code-block:: text

    raw_mass : 154.97517
    peak_height : 7.25775e+06
    KEGG_cid : ['C00988', 'HMDB00816', 'C02287']
    KEGG_name : ['2-Phosphoglycolate;Phosphoglycolic acid ([M-H]-)', 'Phosphoglycolic acid (see KEGG C00988); 2-phosphonooxyacetic acid [carboxylic acid] ([M-H]-)', 'Hydroxymalonate;Tartronic acid;Hydroxymalonic acid;2-Hydroxymalonate;2-Hydroxymalonic acid;2-Tartronic acid ([M+Cl35]-)']
    KEGG Pathways : [['ko00630', 'ko01100'], ['null'], ['null']]
    KEGG Pathways descriptions : [['', 'Glyoxylate and dicarboxylate metabolism', 'Metabolic pathways'], ['null'], ['null']]
    

Agora **tudo junto, aplicando ao ficheiro inteiro**. Para controlo,
podemos contar os compostos obtidos.

.. code-block:: ipython3

    name = 'masses.annotated.reformat.tsv'
    use_only = ['raw_mass', 'peak_height', 'KEGG_cid', 'KEGG_name', 'KEGG Pathways', 'KEGG Pathways descriptions']
    needs_split = ['KEGG_cid', 'KEGG_name', 'KEGG Pathways', 'KEGG Pathways descriptions']
    needs_more_split = ['KEGG Pathways', 'KEGG Pathways descriptions']
    
    with open(name) as a:
        all_lines = [line.strip() for line in a]
    
    headers = all_lines[-1].split('\t')
    
    peaks = []
    for line in all_lines[:-1]:
        info = {}
        line_parts = line.split('\t')
    
        for h, i in zip(headers, line_parts):
            if h in use_only:
                info[h] = i
    
        for n in needs_split:
            info[n] = info[n].split('#')
    
        for n in needs_more_split:
            info[n] = [p.strip(';').split(';') for p in info[n]]
        
        peaks.append(info)
    
    print('São', len(peaks), 'massas')
    print('\n---- Massa 0 -----')
    for h in use_only:
        print(h, ':', peaks[0][h])


.. code-block:: text

    São 482 massas
    
    ---- Massa 0 -----
    raw_mass : 154.97517
    peak_height : 7.25775e+06
    KEGG_cid : ['C00988', 'HMDB00816', 'C02287']
    KEGG_name : ['2-Phosphoglycolate;Phosphoglycolic acid ([M-H]-)', 'Phosphoglycolic acid (see KEGG C00988); 2-phosphonooxyacetic acid [carboxylic acid] ([M-H]-)', 'Hydroxymalonate;Tartronic acid;Hydroxymalonic acid;2-Hydroxymalonate;2-Hydroxymalonic acid;2-Tartronic acid ([M+Cl35]-)']
    KEGG Pathways : [['ko00630', 'ko01100'], ['null'], ['null']]
    KEGG Pathways descriptions : [['Glyoxylate and dicarboxylate metabolism', 'Metabolic pathways'], ['null'], ['null']]
    

Correspondência compostos - vias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Agora com esta **lista de dicionários** chamada ``peaks`` disponível
podemos centrar a informação em torrno dos compostos associados a vias.

Para isso vamos criar dois dicionários:

-  um chamado ``pathways`` que associa cada **Id de um composto** a uma
   **lista de Ids de vias** e
-  outro chamado ``descriptions``, que associa cada Id de via à sua
   descrição.

.. code-block:: ipython3

    paths = {}
    descriptions = {}
    
    for k in peaks:
        for c, p, d in zip(k['KEGG_cid'], k['KEGG Pathways'], k['KEGG Pathways descriptions']):
            if p[0] == 'null':
                continue
            paths[c] = p
            for pId, desc in zip(p, d):
                descriptions[pId] = desc
    
    print('São', len(paths), 'compostos com anotações de vias')
    
    print('\n---------Alguns compostos:\n')
    
    for (i, c) in enumerate(paths):
        if i > 10:
            break
        print(c, '-->', paths[c])
    
    print('\n---------Alguns compostos:\n')
    
    for (i, c) in enumerate(paths):
        if i > 10:
            break
        p_desc = [descriptions[p] for p in paths[c]]
        print(c, '-->', ' AND '.join(p_desc))


.. code-block:: text

    São 327 compostos com anotações de vias
    
    ---------Alguns compostos:
    
    C00988 --> ['ko00630', 'ko01100']
    C16652 --> ['ko00982']
    C16655 --> ['ko00982']
    C01088 --> ['ko00770']
    C01989 --> ['ko00630']
    C02488 --> ['ko00620']
    C02991 --> ['ko00051']
    C03652 --> ['ko00760']
    C03979 --> ['ko00051']
    C06159 --> ['ko00051']
    C16390 --> ['ko00760']
    
    ---------Alguns compostos:
    
    C00988 --> Glyoxylate and dicarboxylate metabolism AND Metabolic pathways
    C16652 --> Drug metabolism - cytochrome P450
    C16655 --> Drug metabolism - cytochrome P450
    C01088 --> Pantothenate and CoA biosynthesis
    C01989 --> Glyoxylate and dicarboxylate metabolism
    C02488 --> Pyruvate metabolism
    C02991 --> Fructose and mannose metabolism
    C03652 --> Nicotinate and nicotinamide metabolism
    C03979 --> Fructose and mannose metabolism
    C06159 --> Fructose and mannose metabolism
    C16390 --> Nicotinate and nicotinamide metabolism
    

Utilização da informação
~~~~~~~~~~~~~~~~~~~~~~~~

Agora com estes dois dicionários podemos responder a várias questões:

Exemplo: Como obter uma **lista** com nomes das vias, mas sem
repetições?

.. code-block:: ipython3

    names = []
    
    for c in paths:
        for pId in paths[c]:
            name = descriptions[pId]
            if name not in names:
                names.append(name)
    
    # AS primeiras 20 vias:
    for name in names[:21]:
        print(name)


.. code-block:: text

    Glyoxylate and dicarboxylate metabolism
    Metabolic pathways
    Drug metabolism - cytochrome P450
    Pantothenate and CoA biosynthesis
    Pyruvate metabolism
    Fructose and mannose metabolism
    Nicotinate and nicotinamide metabolism
    Phenylalanine metabolism
    Phenylalanine, tyrosine and tryptophan biosynthesis
    Phenylpropanoid biosynthesis
    Tropane, piperidine and pyridine alkaloid biosynthesis
    Glucosinolate biosynthesis
    Aminoacyl-tRNA biosynthesis
    Biosynthesis of phenylpropanoids
    Biosynthesis of alkaloids derived from shikimate pathway
    Biosynthesis of alkaloids derived from ornithine, lysine and nicotinic acid
    Biosynthesis of plant hormones
    ABC transporters
    Biosynthesis of plant secondary metabolites
    Alanine, aspartate and glutamate metabolism
    Tetracycline biosynthesis
    

Exemplo: Como obter um **dicionário** com os **Ids das vias como
chaves** e o **número de vezes que aparecem como valores**?

.. code-block:: ipython3

    counts = {}
    
    for c in paths:
        for pId in paths[c]:
            if pId in counts:
                counts[pId] = counts[pId] + 1
            else:
                counts[pId] = 1
    
    print('São', len(counts), 'vias')
    
    print('\n---------Algumas contagens:\n')
    
    for i, pId in zip(range(10), counts):
        print(counts[pId], '\t', pId, '\t', descriptions[pId])


.. code-block:: text

    São 150 vias
    
    ---------Algumas contagens:
    
    8 	 ko00630 	 Glyoxylate and dicarboxylate metabolism
    113 	 ko01100 	 Metabolic pathways
    5 	 ko00982 	 Drug metabolism - cytochrome P450
    4 	 ko00770 	 Pantothenate and CoA biosynthesis
    4 	 ko00620 	 Pyruvate metabolism
    17 	 ko00051 	 Fructose and mannose metabolism
    6 	 ko00760 	 Nicotinate and nicotinamide metabolism
    4 	 ko00360 	 Phenylalanine metabolism
    6 	 ko00400 	 Phenylalanine, tyrosine and tryptophan biosynthesis
    2 	 ko00940 	 Phenylpropanoid biosynthesis
    

Uma vez que ``counts`` é um dicionário, não se aplica a noção de ordem e
é evidente que as vias não estão ordenadas segundo as contagens de
compostos.

Podemos obter as vias por ordem decrescente de compostos?

Para, por exemplo, obter **as 20 vias mais abundantes** em compostos?

Uma vez que os dicionários não estão associados a uma "ordenação", temos
de trabalhar com listas.

Estratégia:

-  Criar uma lista com os pares (contagens, Id da via)
-  Ordenar a lista

.. code-block:: ipython3

    counts_list = [(counts[k], k) for k in counts]
    
    #Controlo: 5 primeiros elementos, lista desordenada:
    for i in counts_list[:5]:
        print(i)


.. code-block:: text

    (8, 'ko00630')
    (113, 'ko01100')
    (5, 'ko00982')
    (4, 'ko00770')
    (4, 'ko00620')
    

.. code-block:: ipython3

    counts_list.sort(reverse=True)
    # reverse=True indica que a ordenação é por ordem decrescente
    
    print('As 20 vias com mais compostos associados:\n')
    for c, pId in counts_list[:20]:
        print(c, ':', descriptions[pId])


.. code-block:: text

    As 20 vias com mais compostos associados:
    
    113 : Metabolic pathways
    24 : Biosynthesis of plant secondary metabolites
    21 : Galactose metabolism
    20 : alpha-Linolenic acid metabolism
    18 : Biosynthesis of unsaturated fatty acids
    17 : Biosynthesis of terpenoids and steroids
    17 : Linoleic acid metabolism
    17 : Starch and sucrose metabolism
    17 : Ascorbate and aldarate metabolism
    17 : Fructose and mannose metabolism
    16 : Phosphotransferase system (PTS)
    15 : Diterpenoid biosynthesis
    15 : Steroid biosynthesis
    14 : Biosynthesis of plant hormones
    14 : Glycolysis / Gluconeogenesis
    13 : ABC transporters
    13 : Biosynthesis of alkaloids derived from shikimate pathway
    13 : Biosynthesis of phenylpropanoids
    13 : Amino sugar and nucleotide sugar metabolism
    13 : Pentose and glucuronate interconversions
    

Como exemplo final, escrever um ficheiro que sumariza esta informação.

Problema: Escrever um ficheiro, chamado ``pathways.txt`` com vários
campos, separados por ``\t`` e **uma via por linha**.

As vias devem estar por ordem decrescente de ocorrência

Os campos são:

-  O ID da via
-  A descrição da via
-  O número de ocorrências
-  Os Ids dos compostos associados à via, separados por ``;``

.. code-block:: ipython3

    file_name = 'pathways.txt'
    
    # associação entre ids de vias e lista de compostos
    compounds = {}
    
    for c in paths:
        for pId in paths[c]:
            if pId in compounds:
                compounds[pId].append(c)
            else:
                compounds[pId] = [c]
    
    # contagens de coorrências (número de compostos)
    counts = {}
    for Id in compounds:
        counts[Id] = len(compounds[Id])
    
    # ordenar as contagens
    counts_list = [(counts[k], k) for k in counts]
    counts_list.sort(reverse=True)
    
    # escrever o ficheiro com a informação
    with open(file_name, 'w') as f:
        for c, Id in counts_list:
            print(Id, descriptions[Id], c, compounds[Id], file=f, sep='\t')

.. code-block:: ipython3

    # verificar se correu bem...
    file_name = 'pathways.txt'
    
    with open(file_name) as a:
        linhas = a.readlines()
        print(linhas[14])


.. code-block:: text

    ko00010	Glycolysis / Gluconeogenesis	14	['C00111', 'C00118', 'C00031', 'C00221', 'C00267', 'C00631', 'C00197', 'C00103', 'C00668', 'C01172', 'C05345', 'C00236', 'C01159', 'C16255']
    
    
