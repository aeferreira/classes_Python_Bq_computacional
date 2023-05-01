---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Exemplo: ficheiros UniProt txt

## Introdução

Este e o próximo capítulo são dedicados a aplicar as ferramentas mostradas
na primeira parte a pequenos projetos já com alguma elaboração.

Os dois exemplos consistem em extraír informação relevante de ficheiros disponibilizados por portais e ferramentas de Bioinformática.

O primeiro exemplo consiste em extraír a informação sobre *modificações pós-traducionais* (em inglês: Post Translational Modifications, ou **PTM**) de um
ficheiro contendo a informação da UniProt sobre todas as proteínas de um determinado organismo, um dos *proteomas de referência* existentes neste portal.

O que são PTMs? São modificações que ocorrem nas proteínas após a sua síntese. Uma das mais conhecidas é a fosforição de grupos laterais contendo -OH, que são muitas vezes são relacionadas com a regulação da função de uma proteína. Mas existem muitas outras modificações possíveis.

O objetivo é extraír a informação sobre PTMs e fazer uma contagem  (e visualizar num gráfico) de modo a ter uma ideia da sua abundância relativa nas notações da UniProt.

O proteoma usado vai ser o do organismo *Saccharomyces cerevisiae* (a levedura de padeiro, um dos organismos modelo em biociências moleculares)

Este exemplo irá ilustrar muitas dos conceitos introduzidos nos capítulos anteriores, especialmente sobre a transformação de *strings*

Mas antes é necessário obter e preparar a informação *total* sobre as proteínas da levedura da UniProt.

## Obtenção do ficheiro UniProt txt

A UniProt disponibiliza vários tipos de ficheiros após a realização de uma busca.

Um dos mais completos são os ficheiros do tipo *UniProt txt* que contêm praticamente toda a informação que podemos visualizar quando consultamos as páginas web dedicadas a uma determinada proteína, mas num formato de texto e podendo juntar a informação de várias proteínas no mesmo ficheiro.

A UniProt tem [documentação](http://web.expasy.org/docs/userman.html) com indicações detalhadas sobre o formato dos seus ficheiros, em particular o *UniProt txt*:

Instruções para obter o ficheiro de trabalho:

- Na UniProt procurar pelo ["proteoma de referência" da levedura S. cerevisiae](http://www.uniprot.org/proteomes/UP000002311) (http://www.uniprot.org/proteomes/UP000002311)
- Passar para resultados UniProtKB: em "Map To" escolher UniPortKB
- Escolher *Download -> Text , compressed* (NOTA: o ficheiro é grande, o download pode demorar um pouco)
- Se o download tiver sido em modo "compressed", extraír o (único) ficheiro do zip.
- Alterar o nome do ficheiro para `uniprot_scerevisiae.txt`
- Criar uma pasta de trabalho, onde irá ser desenvolvido o programa e mover o ficheiro `uniprot_scerevisiae.txt` para essa pasta.

## Programa completo

Comecemos por mostrar o programa completo e o respetivo output:

```{code-cell} ipython3

# Counts of the several types of PTMs in proteins of S. cerevisiae

from matplotlib import pyplot as plt
import seaborn as sns

data_filename = 'uniprot_scerevisiae.txt'

def read_Uniprot_text(filename):
    """Reads a UniProt text file and splits into a list of protein records."""
    
    with open(filename) as uniprot_file:
        whole_file = uniprot_file.read()

    records = whole_file.split('//\n')
    
    # remove empty records
    records = [p for p in records if len(p) != 0]
    # since we know that it is the last one only...
    # records.pop(-1)
    return records

prots = read_Uniprot_text(data_filename)

def extract_info(record):
    """Reads a UniProt text record and returns a dict with extrated information.
    
    The returned dict has the following fields:
    
    'ac': the UniProt Access Id,
    'n': the sequence length, 
    'PTMs': a dictionary that associates the location of PTMs (int, as keys)
               with the name of the PTM.
    """
    
    IDline, ACline, *otherlines = record.splitlines()
    
    # Extract UniProt AC and number of amino acids
    # Example (first two lines):
    # ID   AB140_YEAST             Reviewed;         628 AA.
    # AC   Q08641; D6W2U2; Q08644;
    
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
    
    # Extract FT lines and process PTM information
    #
    # Example of phosphorylation lines
    # FT   MOD_RES         342
    # FT                   /note="Phosphoserine"
    # FT                   /evidence="ECO:0000244|PubMed:18407956,
    # FT                   ECO:0000244|PubMed:19779198"
    
    PTMs = {}
    
    for i, line in enumerate(otherlines):

        if line.startswith('FT   MOD_RES'):
            FTcode, MOD_RES, loc, *rest = line.split()
            
            nextline = otherlines[i+1]
            PTMtype = nextline.split('/note=')[1]
            PTMtype = PTMtype.strip('"')
            PTMtype = PTMtype.split(';')[0]
            
            PTMs[loc] = PTMtype
        
    # Return dictionary of extracted information
    return {'ac': ac, 'n': n, 'PTMs': PTMs}

all_prots = [extract_info(p) for p in prots]

PTM_counts = {}
for p in all_prots:
    PTMs = p['PTMs']
    
    # just skip if no PTMs
    if len(PTMs) == 0:
        continue
        
    for ptmtype in PTMs.values():
        if ptmtype in PTM_counts:
            PTM_counts[ptmtype] = PTM_counts[ptmtype] + 1
        else:
            PTM_counts[ptmtype] = 1

# sort function returning the second element of a pair of values
def second(pair):
    return pair[1]

# sort items, using second element (the counts) as key, decreasing order

sorted_items = sorted(PTM_counts.items(), key=second, reverse=True)

# the result of sorted is not actually a list,
# but we can transform it into a list

ordered_PTM_counts = list(sorted_items)

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

# let's look at the results
for PTMtype, count in ordered_PTM_counts:
    print(PTMtype, count)

# make a barplot, only for PTMs with count > 10
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6,9))

types = [t for t,c in ordered_PTM_counts if c > 10]
counts = [c for t,c in ordered_PTM_counts if c > 10]

bp = sns.barplot(y=types, x=counts, orient='h', log=True, palette='tab10')
plt.show()

```

De uma forma sumária, o programa realiza as seguintes *tarefas*:

- leitura do ficheiro `uniprot_scerevisiae.txt` para uma *string* e separação da informação por proteína, criando a
lista `prots`
- Extração da informação, criando uma lista de dicionários, `all_prots`, em que cada dicionário tem o número de acesso, comprimento da proteína e tabela de PTMs
- Contagem dos diferentes tipos de PTM, ordenando as contagens por ordem decrescente
- Apresentação dos resultados, incluíndo um gráfico de barras

As duas primeiras tarefas são implementadas em funções.

Para o gráfico, são usados dois módulos de criação de gráficos da linguagem Python: `matplotlib` e `seaborn`. Eles são importados no início do programa. É prática comum que os `import`s sejam feitos no início do programa.

Vejamos agora as várias partes:

## Leitura do ficheiro e separação da informação por proteína

Para o programa funcionar, o ficheiro `uniprot_scerevisiae.txt` deve estar na mesma pasta que o programa.

Podemos começar por ler todo o seu conteúdo para uma *string*:

```{code-cell} ipython3
data_filename = 'uniprot_scerevisiae.txt'

with open(data_filename) as uniprot_file:
    whole_file = uniprot_file.read()
```


O passo seguinte será, na *string* `whole_file`, que contem toda a informação sobre todas as proteínas de levedura, separarmos a informação por proteína, pondo o resultado numa lista de *strings*, blocos de texto em que cada bloco diz respeito a uma proteína diferente.

Para isso precisamos de saber o que "divide", o que separa no texto as proteínas umas das outras. Isto na perspetiva de usarmos a função `.split()` para separarmos a informação a partir de um separador, criando uma lista.

Qual é o separador?

Podemos abrir o ficheiro num editor de texto e reparamos
nos pormenores da sua estrutura.

Depressa nos apercebemos que existe uma marca para separar a informação de diferentes proteínas:

    ...
    ...
    FT   CARBOHYD    103    103       N-linked (GlcNAc...) asparagine.
    FT                                {ECO:0000255}.
    SQ   SEQUENCE   411 AA;  48455 MW;  91676D56AC053F3C CRC64;
        MTSATDKSID RLVVNAKTRR RNSSVGKIDL GDTVPGFAAM PESAASKNEA KKRMKALTGD
        SKKDSDLLWK VWFSYREMNY RHSWLTPFFI LVCVYSAYFL SGNRTESNPL HMFVAISYQV
        DGTDSYAKGI KDLSFVFFYM IFFTFLREFL MDVVIRPFTV YLNVTSEHRQ KRMLEQMYAI
        FYCGVSGPFG LYIMYHSDLW LFKTKPMYRT YPVITNPFLF KIFYLGQAAF WAQQACVLVL
        QLEKPRKDYK ELVFHHIVTL LLIWSSYVFH FTKMGLAIYI TMDVSDFFLS LSKTLNYLNS
        VFTPFVFGLF VFFWIYLRHV VNIRILWSVL TEFRHEGNYV LNFATQQYKC WISLPIVFVL
        IAALQLVNLY WLFLILRILY RLIWQGIQKD ERSDSDSDES AENEESKEKC E
    //
    ID   MUD2_YEAST              Reviewed;         527 AA.
    AC   P36084; D6VXL2;
    DT   01-JUN-1994, integrated into UniProtKB/Swiss-Prot.
    DT   16-AUG-2004, sequence version 3.
    DT   13-FEB-2019, entry version 153.
    DE   RecName: Full=Splicing factor MUD2;
    ...
    ...


```{admonition} Informação
:class: info
No formato *Uniprot txt* o separador que aparece entre a informação sobre proteínas distintas é `//` numa
linha.

Não deve existir mais nada nessa linha, o que significa que o separador é, na realidade, `//` seguido de mudança de linha, isto é, `//\n`

```

Portanto, podemos dividir todo o ficheiro em blocos,
indicando `//\n` na função `.split()`:

```{code-cell} ipython3
data_filename = 'uniprot_scerevisiae.txt'

with open(data_filename) as uniprot_file:
    whole_file = uniprot_file.read()

records = whole_file.split('//\n')
```

Podemos ver se resultou.

Como `records`, o nome dado ao resultado de `split('//\n')` é uma lista, podemos ver o elemento 0, por exemplo:

```{code-cell} ipython3
:tags: [output_scroll]
data_filename = 'uniprot_scerevisiae.txt'

with open(data_filename) as uniprot_file:
    whole_file = uniprot_file.read()

records = whole_file.split('//\n')

print(records[0])
```


Parece ter resultado.

Ainda para confirmar podemos ver o último elemento da lista (posição -1):

```{code-cell} ipython3
data_filename = 'uniprot_scerevisiae.txt'

with open(data_filename) as uniprot_file:
    whole_file = uniprot_file.read()

records = whole_file.split('//\n')

print(records[-1])
```


Desta vez nada apareceu como resultado da função `print()`.

Porquê?

É apenas um pequeno problema que resulta do facto do ficheiro acabar com uma linha contendo `//`. (Por favor confirmar)

Isto faz com que o resultado da função `split()` tenha, no final da lista, uma *string* vazia.

Esta *string* vazia deve ser retirada do fim da lista.

Podemos usar uma lista em compreensão para a retirar:

    records = [p for p in records if len(p) != 0]

isto é, mantemos todos os records, desde que o seu comprimento seja maior do que 0, isto é, não seja uma lista vazia.

Outra possibilidade é usar a função `pop()` de listas que
retira o elemento que está numa posição:

    records.pop(-1)

Esta "tarefa" pode ser posta numa função, uma vez que é uma parte lógica do programa (ler o ficheiro e dividir em blocos respeitantes a diferentes proteínas).

Podemos definir a função aplicar a função logo de seguida.

Como curiosidade, podemos saber qual a dimensão deste proteoma anotado da levedura:

```{code-cell} ipython3
def read_Uniprot_text(filename):
    """Reads a UniProt text file and splits into a list of protein records."""
    
    with open(filename) as uniprot_file:
        whole_file = uniprot_file.read()

    records = whole_file.split('//\n')
    
    # remove empty records
    records = [p for p in records if len(p) != 0]
    # since we know that it is the last one only...
    # records.pop(-1)
    return records

prots = read_Uniprot_text(data_filename)

print(f'The number of protein records in "{data_filename}" is {len(prots)}')
```


## Extração da informação

O interesse agora é extrair a informação pertinente de cada proteína.

Estamos interessados em informações sobre as PTMs. Já vamos ver onde essa informação se encontra e em que formato está. Mas para treinar a extração da informação, podemos começar por tentar obter, para cada proteína, o seu número de acesso Uniprot, umm identificador único para cada proteína e o número de aminoácidos da proteína.

A ideia é conseguir criar um dicionário com estes dois "pedaços" de informação.

Vejamos melhor a primeira proteína da lista, `prots[0]`:

```{code-cell} ipython3
:tags: [output_scroll]
# NOTA: continuação do programa anterior!
print(prots[0])
```

Um primeiro lugar devemos reparar que as linhas começam com um conjunto de duas letras que identifica o tipo de informação que está no resto da linha. Por exemplo, `GN` é a linha com *Gene name*, `AC` é uma linha contendo números de acesso, etc.

O documentação da UniProt contem uma descrição detalhada com estes códigos.

No final de cada bloco de uma proteína encontra-se a sua sequência de amino-ácidos. São as únicas linhas sem código de duas letras (embora a linha introdutória da sequência contenha o código `SQ`):

```{code-block}
...
...
SQ   SEQUENCE   440 AA;  49072 MW;  DCE9E5C434D51201 CRC64;
     MESQQLSQHS PISHGSACAS VTSKEVHTNQ DPLDVSASKT EECEKASTKA NSQQTTTPAS
     SAVPENPHHA SPQTAQSHSP QNGPYPQQCM MTQNQANPSG WSFYGHPSMI PYTPYQMSPM
     YFPPGPQSQF PQYPSSVGTP LSTPSPESGN TFTDSSSADS DMTSTKKYVR PPPMLTSPND
     FPNWVKTYIK FLQNSNLGGI IPTVNGKPVR QITDDELTFL YNTFQIFAPS QFLPTWVKDI
     LSVDYTDIMK ILSKSIEKMQ SDTQEANDIV TLANLQYNGS TPADAFETKV TNIIDRLNNN
     GIHINNKVAC QLIMRGLSGE YKFLRYTRHR HLNMTVAELF LDIHAIYEEQ QGSRNSKPNY
     RRNPSDEKND SRSYTNTTKP KVIARNPQKT NNSKSKTARA HNVSTSNNSP STDNDSISKS
     TTEPIQLNNK HDLHLRPETY
```

Voltando ao exemplo do princípio de cada bloco, as duas primeiras linhas têm a informação que precisamos: o número de acesso e o comprimento da proteína:

```{code-block}
ID   AGP2_YEAST              Reviewed;         596 AA.
AC   P38090; D6VQC9;
...
...
```

Vamos tentar extraír para um dicionário o número de aminoácidos e o número de acesso da primeira proteína da lista obtida anteriormente.

Uma vez que a informação está claramente organizada linha a linha, então podemos para a primeira proteína, começar por separar o bloco de texto por linhas e obter a primeira e a segunda linhas:

```{code-cell} ipython3
# NOTA: continuação do programa anterior!

record = prots[0] # mais tarde aplicaremos a todos os blocos

lines = record.splitlines()

lineID = lines[0]
lineAC = lines[1]
print(lineID)
print(lineAC)

```

Funciona. Vamos agora extraír o que interessa a partir destas linhas.

Se separarmos os elementos da primeira linha pelos espaços o número de aminoácidos está na posição 3! 

O número de acesso está na linha `AC`. O primeiro identificador é o mais atual, os outros são identificadores antigos. A estratégia será aqui separar pelos `;` e pelos espaços.

```{code-cell} ipython3
# NOTA: continuação do programa anterior!

record = prots[0] # mais tarde aplicaremos a todos os blocos

lines = record.splitlines()

lineID = lines[0]
lineAC = lines[1]

partsID = lineID.split()
n = partsID[3]
n = int(n) # para forçar que seja um número inteiro

partsAC = lineAC.split(';')
ac = partsAC[0] # isto é  AC   P38090, é preciso tirar a parte AC
ac = ac.split()
ac = ac[1]

resultado = {'n': n, 'ac':ac}

print(resultado)
```

Resultou. Criámos um dicionário com as duas partes que nos interessavam extraídas.

Desde já um melhoramento: Poddemos aplicar muitas funções de *string* do Python em cadeia e ainda combinar com a indexação. isto pode-nos poupar o uso de nomes intermédios.

Vejamos uma alternativa:


```{code-cell} ipython3
# NOTA: continuação do programa anterior!

record = prots[0] # mais tarde aplicaremos a todos os blocos

lines = record.splitlines()

lineID = lines[0]
lineAC = lines[1]

ac = lineAC.split(';')[0].split()[1]
n = int(lineID.split()[3])

resultado = {'n': n, 'ac':ac}

print(resultado)
```


Vamos dissecar o processo de obter o `ac`.

    ac = lineAC.split(';')[0].split()[1]

Isto significa:

- *Dividir a linha `lineAC` por `;`*
- *aproveitar o fragmento 0*
- *dividir este por espaços*
- *aproveitar o fragmento 1*

Podemos agora criar uma função que possa ser aplicada a qualquer bloco de texto com a informação sobre uma proteína (e não apenas à proteína 0).

Vejamos todo o programa até agora, já testando a nova função com a proteína 0 da lista `prots` resultantes da primeira função:

```{code-cell} ipython3
data_filename = 'uniprot_scerevisiae.txt'

def read_Uniprot_text(filename):
    """Reads a UniProt text file and splits into a list of protein records."""
    
    with open(filename) as uniprot_file:
        whole_file = uniprot_file.read()

    records = whole_file.split('//\n')
    
    # remove empty records
    records = [p for p in records if len(p) != 0]
    # since we know that it is the last one only...
    # records.pop(-1)
    return records

prots = read_Uniprot_text(data_filename)

def extract_info(record):
    
    lines = record.splitlines()

    IDline = lines[0]
    ACline = lines[1]
    
    # Extract UniProt AC and number of amino acids
    # Example (first two lines):
    # ID   AB140_YEAST             Reviewed;         628 AA.
    # AC   Q08641; D6W2U2; Q08644;
    
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
    
    # Return dictionary of extracted information
    return {'ac': ac, 'n': n}

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

print('First protein:')
print(extract_info(prots[0]))
```

Podemos agora aplicar a função a todas os blocos, com uma lista em compreensão.

Vamos chamar ao resultado `all_prots`. Será uma **lista de dicionários**.

O programa, até este ponto será:

```{code-cell} ipython3
data_filename = 'uniprot_scerevisiae.txt'

def read_Uniprot_text(filename):
    """Reads a UniProt text file and splits into a list of protein records."""
    
    with open(filename) as uniprot_file:
        whole_file = uniprot_file.read()

    records = whole_file.split('//\n')
    
    # remove empty records
    records = [p for p in records if len(p) != 0]
    # since we know that it is the last one only...
    # records.pop(-1)
    return records

prots = read_Uniprot_text(data_filename)

def extract_info(record):
    
    lines = record.splitlines()

    IDline = lines[0]
    ACline = lines[1]
    
    # Extract UniProt AC and number of amino acids
    # Example (first two lines):
    # ID   AB140_YEAST             Reviewed;         628 AA.
    # AC   Q08641; D6W2U2; Q08644;
    
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
    
    # Return dictionary of extracted information
    return {'ac': ac, 'n': n}

all_prots = [extract_info(p) for p in prots]

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

# see the first 3, as a test
for p in all_prots[:4]:
    print('------------------------------------------')
    print(p)
```

## Extração da informação: PTMs

Vamos agora modificar a função `extract_info()` com a informação que possa existir no ficheiro da Uniprot sobre PTM.

Aqui está uma pequena parte do meio do ficheiro:

```
FT   MOD_RES         223
FT                   /note="Phosphoserine"
FT                   /evidence="ECO:0000244|PubMed:17330950,
FT                   ECO:0000244|PubMed:18407956, ECO:0000244|PubMed:19779198"
FT   MOD_RES         228
FT                   /note="Phosphoserine"
FT                   /evidence="ECO:0000244|PubMed:19779198"
FT   MOD_RES         232
FT                   /note="Phosphothreonine"
FT                   /evidence="ECO:0000244|PubMed:19779198"
FT   MOD_RES         244
FT                   /note="Phosphothreonine"
FT                   /evidence="ECO:0000244|PubMed:19779198"
FT   MOD_RES         570
FT                   /note="Phosphothreonine; by PKH1 or PKH2"
```

Podemos consultar a [documentação da UniProt sobre as linhas FT](http://web.expasy.org/docs/userman.html#FT_keys).

Parece evidente que a informação sobre resíduos modificados está em linhas começadas por `FT   MOD_RES` e nas linhas seguintes.

Na linha `FT   MOD_RES` está a posição do aminoácido modificado.

Na linha imediatamente a seguir está `/note=` e o nome da PTM entre `"`. E ainda, por vezes está o nome da PTM e, a seguir a `;` alguma informação adicional.

Para cada proteína (na função `extract_info()`) queremos

- passar por todas as linhas começadas por `FT   MOD_RES`, extraír daí a posição da PTM
- na linha seguinte, obter o que está a seguir a `/note=`
- tirar as `"`
- separar por `;`
- aproveitar a primeira parte. Isto será o nome da PTM.
- finalmente, criar um dicionário com associação entre a posição e o nome da PTM, para todas as PTMs
- e incluír este dicionário no return da função `extract_info()`

Como fazer isto por programação?

Temos vários problemas para resolver:

- Como passar por todas as linhas respeitantes a uma proteína e procurar as que contêm informação sobre PTM? (fácil, `for` e ver se começam por `FT   MOD_RES`)
- Como extraír a posição? (fácil: separar por espaços e usar o elemento na posição 2)
- Como ir para a linha seguinte? (menos fácil, mas `enumerate()` permite ter acesso à posição da linha que estamos a tratar, logo também a posição da linha seguinte)
- Como obter o nome da PTM? (fácil, mais uns `split()`s)

Vamos então modificar a função `extract_info()` e incluír estas ideias:

```{code-cell} ipython3
# ... NOTA: continuação do programa a partir
# da função read_Uniprot_text(filename)

prots = read_Uniprot_text(data_filename)

def extract_info(record):
    """Reads a UniProt text record and returns a dict with extrated information.
    
    The returned dict has the following fields:
    
    'ac': the UniProt Access Id,
    'n': the sequence length, 
    'PTMs': a dictionary that associates the location of PTMs (int, as keys)
               with the name of the PTM.
    """
    
    lines = record.splitlines()

    IDline = lines[0]
    ACline = lines[1]
    
    # Extract UniProt AC and number of amino acids
    # Example (first two lines):
    # ID   AB140_YEAST             Reviewed;         628 AA.
    # AC   Q08641; D6W2U2; Q08644;
    
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
    
    # Extract FT lines and process PTM information
    #
    # Example of phosphorylation lines
    # FT   MOD_RES         342
    # FT                   /note="Phosphoserine"
    # FT                   /evidence="ECO:0000244|PubMed:18407956,
    # FT                   ECO:0000244|PubMed:19779198"

    # NOTE: there are 3 spaces between FT and MOD_RES
    
    PTMs = {}
    
    for i, line in enumerate(lines):

        if not line.startswith('FT   MOD_RES'):
            # skip line if does not start with FT   MOD_RES
            continue

        loc = line.split()[2]

        nextline = lines[i+1] # here enumerate() is very usefull

        PTMtype = nextline.split('/note=')[1]
        PTMtype = PTMtype.strip('"') # strip() takes out the ""
        PTMtype = PTMtype.split(';')[0] # the name of the PTM is before the ;
            
        # add to dicionary PTMs
        PTMs[loc] = PTMtype
        
    # Return dictionary of extracted information
    # including the PTMs dicionary
    return {'ac': ac, 'n': n, 'PTMs': PTMs}

all_prots = [extract_info(p) for p in prots]

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

# see the first 4, as a test
for p in all_prots[:5]:
    print('------------------------------------------')
    print(p)
```

Aparentemente nem todas as proteínas têm anotações sobre PTMs.

Note-se a utilidade da função `enumerate()`: podemos ao mesmo tempo passar com o comando `for` pelas linhas usando o nome `line` e pelas **posições** das linhas, usando `i` (não esquecer que `lines` é uma lista de linhas).

    for i, line in enumerate(lines):

isto foi útil para obter facilmente a "linha seguinte":

    nextline = lines[i+1]

Já se conseguiu muito: agora temos uma lista de 6049 dicionários em que cada um deles tem o número de acesso, o comprimento da proteína e um dicionário com as localizações e o nome de cada PTM da proteína.

O próximo passo é contar as PTM de cada tipo, listar e fazer um gráfico de barras.

## Interlúdio: atribuições múltiplas com *

Antes de passarmos à fase seguinte, existe um pormenor da atribuição de nomes que pode ser útil. Trata-se da atribuição
múltipla de nomes com a opção de utilizar `*` para captar o "restante" de uma coleção.

Vejamos um pequeno exemplo de atribuições múltiplas, uma técnica já usada em problemas anteriores:


```{code-cell} ipython3
# atribuição múltipla

m, a = 12, 365

print(m, a)

# atribuição múltipla a partir dos
# elementos de uma lista

s, m, a = [7, 12, 365]

print(s, m, a)
```


Aqui mostra-se o facto de uma atribuição poder ser feita à custa dos elementos
de uma lista.

Para todos os efeitos, conseguimos assim atribuír nomes a todos
os elementos de uma lista:

```{code-cell} ipython3
s, m, a = [7, 12, 365]

# é equivalente a

nums = [7, 12, 365]

s = nums[0]
m = nums[1]
a = nums[2]
```

Nesta situação, é possível usar, do lado esquerdo do sinal de igual, um `*`
como prefixo de um dos nomes para **captar** um conjunto de elementos restantes nas atribuições, na forma de
uma lista mais pequena.

O melhor é ver um exemplo:

```{code-cell} ipython3
s, m, a, *tudo_o_resto = [7, 12, 365, 1, 3, 5, 7, 9, 11]

print(s)
print(m)
print(a)
print(tudo_o_resto)
```


Neste exemplo, pelo facto de termos usado um `*` antes do nome `tudo_o_resto`
fez com este nome fosse atribuído à *parte restante* da lista que serviu de atribuição.

```{admonition} Dica
:class: tip
Esta atribuição múltipla com `*` é muito útil quando não sabemos
exatamente qual o comprimento da lista que fornece os valores e estamos
interessados apenas em alguns dos primeiros valores.

O nome que é usado com `*` como prefixo é sempre atribuído a uma lista.

Esta pode ter apenas um elemento ou até uma lista vazia.

```

Mas este mecanismo pode até ser usado sem ser no nome final:


```{code-cell} ipython3
s, m, a, *o_meio, ultimo = [7, 12, 365, 1, 3, 5, 7, 9, 11]

print(s)
print(m)
print(a)
print(o_meio)
print(ultimo)
```


Um outro exemplo:

```{code-cell} ipython3
*lixo, antepenúltimo, penúltimo, último = [7, 12, 365, 1, 3, 5, 7, 9, 11]

print(antepenúltimo)
print(penúltimo)
print(último)
```


E ainda outro...

```{code-cell} ipython3
primeiro, *lixo, antepenúltimo, penúltimo, último = [7, 12, 365, 1, 3, 5, 7, 9, 11]

print(primeiro)
print(antepenúltimo)
print(penúltimo)
print(último)

print(lixo)
```


Este mecanismo pode-nos ajudar a simplificar um pouco alguns passos da função
`extract_info()`:

Em vez de 

```{code-block} python3
lines = record.splitlines()

IDline = lines[0]
ACline = lines[1]
```

Podemos escrever apenas

```{code-block} python3
IDline, ACline, *otherlines = record.splitlines()
```

A função `.splitlines()` gera uma lista, logo podemos imediatamente usar
uma atribuição múltipla para atribuír nomes a várias linhas que estejamos interessados.

Note-se que `otherlines` seria um nome de uma lista contendo todas as linhas
menos as duas primeiras. O que significa que, mais à frente, quando procuramos
linhas começadas por `FT`, devemos fazer

    for line in otherlines:
     

````{admonition} Problema
:class: question
Como poderíamos substituír a obtenção de `n` nesta parte do program

```{code-block} python3
n = int(IDline.split()[3])
```

por uma atribuição múltipla para *isolar* o `n` no meio dos outros
elementos na mesma linha?

Repare que a linha `ID` tem o seguinte aspeto:

```{code-block}
ID   AB140_YEAST             Reviewed;         628 AA.
```
````

````{admonition} Solução
:class: tip, dropdown
```{code-block} ipython3
*useless, n, final = IDline.split()
n = int(n)
```

Não sendo mais compacto, é mais simples de entender
````

## Contagem dos tipos de PTM

Vamos agora continuar o programa de forma contar os vários tipos de PTM que existem, já
"extraídos" na lista de dicionários `all_prots`.

```{admonition} Atenção
:class: warning
Nos passos seguintes vamos ampliar o programa que já existe, até
ao cálculo da lista `all_prots`. Esta lista já tem de existir para o resto
funcionar.

```

Recorde-se que a lista `all_prots` contem dicionários.

Cada dicionário contem
uma chave `PTMs`, a qual tem como valor um outro dicionário que associa a posição
de cada *PTM* ao seu nome.

    {'ac': 'P40467', 'n': 964, 'PTMs': {'166': 'Phosphoserine', '186': 'Phosphoserine', '963': 'Phosphoserine'}}


Como contar as *PTM* em todas as proteínas pelo seu nome?

Podemos criar, mais uma vez, um novo dicionário que associa o nome de cada *PTM* à sua contagem. Vamos chamar
`PTM_counts`.

A ideia será passar por toda a lista `all_prots` (com `for p in all_prots`),
obter os nomes das *PTM* de cada proteína (com `p['PTMs'].values()`) e depois
ir adicionando +1 à contagem existente no dicionário de contagens.

Se ainda não existir o nome de uma PTM no dicionário, na primeira vez que é colocado
deve ter o valor 1, a primeira contagem.

Vejamos como fica:


```{code-cell} ipython3
:tags: [output_scroll]
PTM_counts = {}
for p in all_prots:
    PTMs = p['PTMs']
    
    # just skip if no PTMs
    if len(PTMs) == 0:
        continue
        
    for ptmtype in PTMs.values():
        if ptmtype in PTM_counts:
            PTM_counts[ptmtype] = PTM_counts[ptmtype] + 1
        else:
            PTM_counts[ptmtype] = 1
            
print(PTM_counts) 
```

Funcionou, embora não seja a maneira mais elegante de apresentar as contagens.

Na realidade o ideal seria ordenar por ordem decrescente, de forma a apresentar
na forma de uma tabela em que saberíamos facilemnte quais as *PTM* mais abundantes e menos
abundantes.

O problema é que os dicionários não têm uma **ordem** dos seus elementos implícita.

As listas têm e é fácil transformar um dicionário numa lista de pares (chave:valor):


```{code-cell} ipython3
:tags: [output_scroll]
PTM_counts = {}
for p in all_prots:
    PTMs = p['PTMs']
    
    # just skip if no PTMs
    if len(PTMs) == 0:
        continue
        
    for ptmtype in PTMs.values():
        if ptmtype in PTM_counts:
            PTM_counts[ptmtype] = PTM_counts[ptmtype] + 1
        else:
            PTM_counts[ptmtype] = 1

# print(PTM_counts) 

list_PTM_counts = list(PTM_counts.items())

print(list_PTM_counts) 
```


Agora temos uma lista, mas não está ordenada por contagens.

Como ordenar esta lista?

Repare-se que os elementos da lista são pares de objetos e queremos ordenar a lista pelo
**segundo elemento do par de objetos**.

Existe uma função para gerar uma sequência de valores ordenados a partir de uma lista: a função
`sorted()`

Mas esta função pode receber como argumento `key` uma **outra função** que indique
qual exatamente o valor que deve ser ordenado, calculado a partir de cada elemento.

Isto é útil, neste caso. Precisamos de uma função que "aponte" para o segundo elemento
de cada par para que a função `sorted()` saiba o que fazer.

Mas temos de escrever essa função.

É uma função muito simples que recebe um par de valores
e devolve o segundo elemento do par.

```{code-cell} ipython3
# sort function returning the second element of a pair of values
def second(pair):
    return pair[1]
```

Vejamos como aplicar esta função:

```{code-cell} ipython3
# sort function returning the second element of a pair of values
def second(pair):
    return pair[1]

ordered_PTM_counts = sorted(list_PTM_counts, key=second, reverse=True)
print(ordered_PTM_counts)

```


Agora sim, temos uma lista ordenada.

Mas é muito mais elegante apresentar em linhas separadas:

```{code-cell} ipython3
:tags: [output_scroll]
# sort function returning the second element of a pair of values
def second(pair):
    return pair[1]

ordered_PTM_counts = sorted(list_PTM_counts, key=second, reverse=True)

# let's look at the results
for PTMtype, count in ordered_PTM_counts:
    print(PTMtype, count)

```


Agora sim, vemos que as fosforilações são as *PTM* mais prevalentes, pelo
menos levando em conta as anotações na UniProtKB relativamente às proteínas 
de levedura *S. cerevisiae*.

Conseguimos extraír a informação em que estávamos interessados a partir de um
ficheiro de texto que segue um formato rígido particular a um portal de Bioinformática.

Note-se, no desenvolvimento deste programa, o papel essencial das coleções da linguagem Python,
listas e dicionários, para armazenar a informação obtida e também o papel das funções
associadas a *strings*

O programa todo até este ponto é o seguinte:

```{code-cell} ipython3
:tags: [output_scroll]

data_filename = 'uniprot_scerevisiae.txt'

def read_Uniprot_text(filename):
    """Reads a UniProt text file and splits into a list of protein records."""
    
    with open(filename) as uniprot_file:
        whole_file = uniprot_file.read()

    records = whole_file.split('//\n')
    
    # remove empty records
    records = [p for p in records if len(p) != 0]
    # since we know that it is the last one only...
    # records.pop(-1)
    return records

prots = read_Uniprot_text(data_filename)

def extract_info(record):
    """Reads a UniProt text record and returns a dict with extrated information.
    
    The returned dict has the following fields:
    
    'ac': the UniProt Access Id,
    'n': the sequence length, 
    'PTMs': a dictionary that associates the location of PTMs (int, as keys)
                with the name of the PTM.
    """
    
    IDline, ACline, *otherlines = record.splitlines()
    
    # Extract UniProt AC and number of amino acids
    # Example (first two lines):
    # ID   AB140_YEAST             Reviewed;         628 AA.
    # AC   Q08641; D6W2U2; Q08644;
    
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
    
    # Extract FT lines and process PTM information
    #
    # Example of phosphorylation lines
    # FT   MOD_RES         342
    # FT                   /note="Phosphoserine"
    # FT                   /evidence="ECO:0000244|PubMed:18407956,
    # FT                   ECO:0000244|PubMed:19779198"
    
    PTMs = {}
    
    for i, line in enumerate(otherlines):

        if line.startswith('FT   MOD_RES'):
            FTcode, MOD_RES, loc, *rest = line.split()
            
            nextline = otherlines[i+1]
            PTMtype = nextline.split('/note=')[1]
            PTMtype = PTMtype.strip('"')
            PTMtype = PTMtype.split(';')[0]
            
            PTMs[loc] = PTMtype
        
    # Return dictionary of extracted information
    return {'ac': ac, 'n': n, 'PTMs': PTMs}

all_prots = [extract_info(p) for p in prots]

PTM_counts = {}
for p in all_prots:
    PTMs = p['PTMs']
    
    # just skip if no PTMs
    if len(PTMs) == 0:
        continue
        
    for ptmtype in PTMs.values():
        if ptmtype in PTM_counts:
            PTM_counts[ptmtype] = PTM_counts[ptmtype] + 1
        else:
            PTM_counts[ptmtype] = 1


list_PTM_counts = list(PTM_counts.items())

# sort function returning the second element of a pair of values
def second(pair):
    return pair[1]

ordered_PTM_counts = sorted(list_PTM_counts, key=second, reverse=True)

# Output of PTM information

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

for PTMtype, count in ordered_PTM_counts:
    print(PTMtype, count)

```

## Gráficos

A tabela que conseguimos obter na secção anterior já é muito interessante.

Ficámos a saber que a fosforilação de serinas tem 6049 anotações, enquanto que a
*PTM* exótica S-metilcisteína tem uma única anotação (ela e outras 13).

Mas um gráfico causaria muito mais impressão. Vamos fazer um gráfico de barras com as
contagens de *PTM*.

Para a linguagem Python existem vários módulos destinados a obter gráficos num
program. Um dos mais conhecidos é o `matplotlib`, uma da "bibliotecas" gráficas
mais versáteis e populares (e também um pouco intimidante) da linguagem Python.

O [*site* oficial da matplotlib](https://matplotlib.org/) dá uma ideia da versatilidade da
biblioteca, tendo uma galeria extensa de exemplos.

Uma outra biblioteca digna de nota é o projeto [seaborn](https://seaborn.pydata.org/) que é
baseado na `matplotlib` e inclui "melhoramentos" estéticos e novos tipos de gráficos, especialemnte da área da estatística.

Ampliando o programa, vamos combinar os dois módulos, criando um gráfico de barras com as contagens
da PTM, embora restringindo àquelas que têm pelo menos 10 contagens:

```{code-cell} ipython3
from matplotlib import pyplot as plt
import seaborn as sns


sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6,9))

types = [t for t,c in ordered_PTM_counts if c > 10]
counts = [c for t,c in ordered_PTM_counts if c > 10]

bp = sns.barplot(y=types, x=counts, orient='h', log=True, palette='tab10')
plt.show()
```

Embora seja uma pequena ampliação do programa, é preciso explicar um pouco a utilização destas duas bibliotecas,
de uma forma muitíssimo sumária, uma vez que a sua funcionalidade é muito vasta.

Após os dois `imports` necessários para se utilizar as bibliotecas, a função
`seaborn.set()` introduz um **estilo** de gráficos particular, o "darkgrid" (existem vários).

É uma questão estética (e de gosto pessoal).

A função `subplots()` é uma função importante que prepara uma figura se tiver vários painéis, o que não é
o caso e, de entre outras opções, permite controlar o tamanho total da figura, com `figsize` (unidades em polegadas).

Depois disto é apenas necessário preparar duas listas, uma com os nomes das barras e
outra com as alturas da barras e usar a função `seaborn.barplot()` usando estas duas
listas como argumentos.

As listas foram criadas como listas em compreensão a partir da lista `ordered_PTM_counts`,
filtrando as *PTM* com mais de 10 contagens.

Mais 3 pormenores finais na função `barplot()`:

- `orient='h'` desenha barras horizontais e não (as mais habituais) barras verticais
- `palette='tab10'` escolhe um mapa de cores a usar nas barras. Há inúmeras possibilidades. Ver
por exemplo [esta página](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)
- finalmente, *last but not least*, `log=True`, faz a escala de contagens ser logarítmica. Isto é necessário, caso
contrário as fosforilações dominariam completamente o gráfico e não conseguiríamos ver as *PTM* menos
abundantes que teríam barras perto de 0.

## Programa completo

```{code-cell} ipython3
:tags: [output_scroll]
data_filename = 'uniprot_scerevisiae.txt'

def read_Uniprot_text(filename):
    """Reads a UniProt text file and splits into a list of protein records."""
    
    with open(filename) as uniprot_file:
        whole_file = uniprot_file.read()

    records = whole_file.split('//\n')
    
    # remove empty records
    records = [p for p in records if len(p) != 0]
    # since we know that it is the last one only...
    # records.pop(-1)
    return records

prots = read_Uniprot_text(data_filename)

def extract_info(record):
    """Reads a UniProt text record and returns a dict with extrated information.
    
    The returned dict has the following fields:
    
    'ac': the UniProt Access Id,
    'n': the sequence length, 
    'PTMs': a dictionary that associates the location of PTMs (int, as keys)
                with the name of the PTM.
    """
    
    IDline, ACline, *otherlines = record.splitlines()
    
    # Extract UniProt AC and number of amino acids
    # Example (first two lines):
    # ID   AB140_YEAST             Reviewed;         628 AA.
    # AC   Q08641; D6W2U2; Q08644;
    
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
    
    # Extract FT lines and process PTM information
    #
    # Example of phosphorylation lines
    # FT   MOD_RES         342
    # FT                   /note="Phosphoserine"
    # FT                   /evidence="ECO:0000244|PubMed:18407956,
    # FT                   ECO:0000244|PubMed:19779198"
    
    PTMs = {}
    
    for i, line in enumerate(otherlines):

        if line.startswith('FT   MOD_RES'):
            FTcode, MOD_RES, loc, *rest = line.split()
            
            nextline = otherlines[i+1]
            PTMtype = nextline.split('/note=')[1]
            PTMtype = PTMtype.strip('"')
            PTMtype = PTMtype.split(';')[0]
            
            PTMs[loc] = PTMtype
        
    # Return dictionary of extracted information
    return {'ac': ac, 'n': n, 'PTMs': PTMs}

all_prots = [extract_info(p) for p in prots]

PTM_counts = {}
for p in all_prots:
    PTMs = p['PTMs']
    
    # just skip if no PTMs
    if len(PTMs) == 0:
        continue
        
    for ptmtype in PTMs.values():
        if ptmtype in PTM_counts:
            PTM_counts[ptmtype] = PTM_counts[ptmtype] + 1
        else:
            PTM_counts[ptmtype] = 1


list_PTM_counts = list(PTM_counts.items())

# sort function returning the second element of a pair of values
def second(pair):
    return pair[1]

ordered_PTM_counts = sorted(list_PTM_counts, key=second, reverse=True)

# Output of PTM information

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

for PTMtype, count in ordered_PTM_counts:
    print(PTMtype, count)


# Bar plot of PTM counts

from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6,9))

types = [t for t,c in ordered_PTM_counts if c > 10]
counts = [c for t,c in ordered_PTM_counts if c > 10]

bp = sns.barplot(y=types, x=counts, orient='h', log=True, palette='tab10')
plt.show()

```



