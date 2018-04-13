
Módulos e ``import``
====================

Introdução
----------

Como vimos, muitas funções estão imediatamente disponíveis quando
começamos a escrever um programa.

Estas funções podem ser "livres" (por exemplo a função ``len()``) ou
associadas a objetos (por exemplo, ``s.split()`` que está associada à
*string* ``s``).

A linguagem Python permite a organização dos programas em **módulos**.

Módulos são **ficheiros .py** (ou ficheiros pré-compilados) que contêm
coleções de funções úteis e relacionadas entre si, podendo também conter
alguns outros objetos que não são funções, mas que contêm informação de
suporte.

Os módulos são também essenciais no aumento da funcionalidade da própria
linguagem python: com a distribuição oficial do Python e em algumas
distribuições de "Python científico" são tipicamente disponibilizados
**centenas de módulos**, em que cada módulo reúne a funcionalidade
adicional relacionada com um propósito particular.

Por exemplo, o módulo ``math`` reúne funções associadas a cálculos
matemáticos (e as constantes :math:`\pi` e *e*).

O módulo ``time`` reúne funções e constantes relacionadas com a
utilização da data e hora.

A documentação sobre a coleção de módulos que são são disponibilizados
em qualquer distribuição da linguagem Python (a chamada *Biblioteca
padrão* (em inglês *Standard Library*) pode ser encontrada na
`documentação oficial <https://docs.python.org/3/library/>`__

Por outro lado, quem escreve módulos novos pode submetê-los ao Python
Package Index, conhecido como `PyPi <https://pypi.python.org/pypi>`__.
Trata-se de um imenso depósito de módulos com contribuições de milhares
de autores e em permanente crescimento.

Exemplo de um módulo e ``import``
---------------------------------

.. code:: ipython3

    def readFASTA(filename):
        """This function reads a FASTA format file and
        returns a pair of strings
        with the header and the sequence
        """
        with open(filename) as a:
            lines = [line.strip() for line in a]
        lines = [line for line in lines if len(line) > 0]
        
        if lines[0].startswith('>'):
            return lines[0], ''.join(lines[1:])
        else:
            return '', ''.join(lines)
    
    h, s = readFASTA("gre3.txt")
    
    print('Header:\n{}\n\nSequence:\n{}'.format(h, s))


.. parsed-literal::

    Header:
    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    
    Sequence:
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIRKAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVPFEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDLLRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTLFENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQELKDISALNANIRFNDPWTWLDGKFPTFA
    

Vamos supor que esta seria a primeira de **uma coleção de funções
relacionadas com o processamento de ficheiros de texto contendo
sequências usados em bioinformática** (uma sequência em FASTA é apenas
um exemplo).

Podemos criar um ficheiro **biosequences.py** contendo essa função:

.. figure:: images/biosequences1.png
   :alt: 

Este ficheiro constitui um módulo que pode ser usado num programa.

Para isso, é necessário usar o comando ``import``:

.. code:: ipython3

    import biosequences
    
    h, s = biosequences.readFASTA("gre3.txt")
    
    print('Header:\n{}\n\nSequence:\n{}'.format(h, s))


.. parsed-literal::

    Header:
    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    
    Sequence:
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIRKAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVPFEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDLLRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTLFENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQELKDISALNANIRFNDPWTWLDGKFPTFA
    

Há mais duas maneiras de utilizar o comando ``import``:

.. code:: ipython3

    from biosequences import readFASTA
    
    h, s = readFASTA("gre3.txt")
    
    print('Header:\n{}\n\nSequence:\n{}'.format(h, s))


.. parsed-literal::

    Header:
    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    
    Sequence:
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIRKAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVPFEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDLLRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTLFENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQELKDISALNANIRFNDPWTWLDGKFPTFA
    

.. code:: ipython3

    from biosequences import *
    
    h, s = readFASTA("gre3.txt")
    
    print('Header:\n{}\n\nSequence:\n{}'.format(h, s))


.. parsed-literal::

    Header:
    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    
    Sequence:
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIRKAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVPFEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDLLRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTLFENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQELKDISALNANIRFNDPWTWLDGKFPTFA
    

Esta última maneira é desaconselhada: um módulo pode conter centenas de
funções e, por isso, podem ser importados centenas de novos *nomes* para
um programa, que podem **entrar em conflito** com outros nomes iguais
utilizados no programa.

Um módulo pode conter outros objetos para além de funções.

A pensar em algumas operações que poderiam ser realizadas com sequências
biológicas, o ficheiro **biosequences.py** poderia ser **ampliado** com
as seguintes atribuições:

::

    .....

    basesDNA = 'ATGC'
    basesRNA = 'AUGC'

    aa_residues   = "ACDEFGHIKLMNPQRSTVWY"

    complement = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    complementRNA = { 'A':'U', 'U':'A', 'G':'C', 'C':'G'}

    gencode = {
         'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
         'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
         'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L',
         'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
         'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
         'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
         'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
         'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
         'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
         'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
         'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
         'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
         'GGG': 'G', 'TAA': 'STOP', 'TAG': 'STOP', 'TGA': 'STOP'}

**Problema**: qual a sequência da proteína codificada por
``AGCTGGATCCTGAACGATGCATAAGCATAGCCATAGACTAGCATGGGACTAAAGGTCCATTACTGA``

Sabemos que o módulo ``biosequences`` tem um dicionário chamado
``gencode``.

.. code:: ipython3

    from biosequences import gencode
    
    def translation(seq):
        cods = [seq[i:i+3] for i in range(0, len(seq), 3)]
        prot = []
        for c in cods:
            aa = gencode[c]
            if aa == 'STOP':
                break
            prot.append(aa)
        return ''.join(prot)
    
    seq = 'AGCTGGATCCTGAACGATGCATAAGCATAGCCATAGACTAGCATGGGACTAAAGGTCCATTACTGA'
    
    print(seq)
    print(translation(seq))


.. parsed-literal::

    AGCTGGATCCTGAACGATGCATAAGCATAGCCATAGACTAGCATGGGACTAAAGGTCCATTACTGA
    SWILNDA
    

Claro que a função ``translation()`` seria uma boa adição ao nosso
módulo ``biosequences``...

O projeto `BioPython <http://biopython.org/wiki/Documentation>`__ foi
precisamente criado como uma coleção de funções e objetos que suportam a
representação e transformação de sequências biológicas.

Hoje é muito mais do que isso, mas a parte central deste pacote de
módulos continua a ser a funcionalidade relacionada com sequências
biológicas.

Se usarmos a primeira forma do comando ``import``, é possível mudar o
nome do módulo (para uma forma mais abreviada), um *alias*, da seginte
forma:

.. code:: ipython3

    import biosequences as bs
    
    h, s = bs.readFASTA("gre3.txt")
    
    print('Header:\n{}\n\nSequence:\n{}'.format(h, s))


.. parsed-literal::

    Header:
    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1
    
    Sequence:
    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIRKAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVPFEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDLLRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTLFENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQELKDISALNANIRFNDPWTWLDGKFPTFA
    
