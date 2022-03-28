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

# pandas

[![](images/pandas.svg)](https://pandas.pydata.org/)

O módulo `pandas` é um dos mais populares módulos da linguagem Python para
o tratamento de dados que não sejam de natureza exclusivamente numérica (como acontece com o módulo `numpy`).

É também considerado também um dos módulos principais do chamado **"ecossistema" de módulos científicos** que, não estando disponíveis na distribuição base da linguagem Python, são geralmente incluídos nas distribuições mais "científicas" da linguagem, por exemplo a distribuição Anaconda.

Tal como o módulo `numpy` introduz um tipo novo de objetos, os *arrays* com propriedades que as listas não têm (operações vetoriais e muitas funções associadas), o módulo `pandas` define outros dois tipos principais de objetos com novas propriedades (embora sejam grandes as semelhanças com os *arrays* do `numpy`):

- as *Series*
- as *DataFrames*

A documentação do módulo apresenta as seguintes definições:


> `Series` is a one-dimensional **labeled** array capable of holding any
> data type (integers, strings, floating point numbers, Python objects,
> etc.). The axis labels are collectively referred to as the **index**.


> `DataFrame` is a **2-dimensional labeled data structure** with columns
> of potentially different types. You can think of it like a spreadsheet
> or SQL table, or a **dict of Series objects**. It is generally the
> most commonly used pandas object.

Além das dimensões (uma *Series* é unidimensional e uma *DataFrame* é bidimensional, isto é, na forma de uma tabela), o que é de sublinhar nestes dois tipos novos de objetos é o facto dos dados serem acompanhados de *labels* (etiquetas)

Estes *labels* servem vários propósitos. Podendo ser basicamente entendidos como dados adicionais, eles são muito importantes na **indexação** da informação, tendo um papel análogo à chaves dos dicionários, mas com outras funcionalidades muito interessantes.

Estes conjuntos de *labels* constituem um **índice**.

Uma *Series* tem um único índice, chamado `index`.

Uma *DataFrame*, tem dois índices, um para as linhas, chamado `index` e outro para as colunas, chamado `columns`.

Comecemos pelas *Series*

## Series

### Construção e indexação

O módulo *pandas* tem de ser importado.

A convenção é importar comm a seguinte "abreviatura":


```{code-cell} ipython3
import pandas as pd
```

Uma Série (*Series*) é um conjunto (ordenado) de valores, mas cada valor
é associado a um *label*.

Ao conjunto dos *labels* é o `index` da *Series*

Uma *Series* pode ser construída, por exemplo, a partir de uma lista, usando a função `pd.Series()`:

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

meses = pd.Series(ndias)

print(meses)
```


Os números de 0 a 11 são o `index` da *Series*.

Se não indicarmos um índice, o conjunto dos inteiros sucessivos será o
índice.

Mas quando construímos uma Série, usando a função `pd.Series()`, podemos indicar o índice, explicitamente:

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind = 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez'.split()

meses = pd.Series(ndias, index=ind)

print(meses)
```


Uma das principais razões de utilizarmos uma *Series* é que podemos
indexar de diferentes maneiras:

- usando um *label* para obter um elemento (como um dicionário)
- usando *slices* de posições
- usando **listas** de *labels*

```{code-cell} ipython3

# ...
# usando a Series meses criada acima...

só_out = meses['Out']
trimestre1 = meses[:3]
férias = meses[['Jul', 'Ago', 'Set']]

print(só_out)
print('--------------')
print(trimestre1)
print('--------------')
print(férias)
```


Ou ainda, tal como os *arrays* do `numpy`, usar **condições lógicas** para indexar (no fundo usando *arrays booleanos*):

```{code-cell} ipython3

# ...
# usando a Series meses criada acima...

m31 = meses[meses==31]

print(m31)
```


Também existe a função `Series.reindex()` que transforma uma *Series*
noutra apenas com os elementos indicados e respeitando a ordem do "novo índice":

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind = 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez'.split()
meses = pd.Series(ndias, index=ind)

alguns_meses = meses.reindex(['Dez', 'Set', 'Abr'])

print(alguns_meses)
```


As Séries podem também ser construídas a partir de um dicionário,
usando `pd.Series()`. As chaves do dicionário passam a ser o `index`:

```{code-cell} ipython3
d = {'a' : 0, 'b' : 1, 'c' : 2}

s = pd.Series(d)
print(s)
```


### Valores em falta

Quando contruímos uma *Series* a partie de um dicionário podemos indicar explicitamente os valores do índice.

Mas, neste caso, se índice tiver elementos que nãoo estejam nas chaves do dicionário, haverá **valores em falta** (em inglês *missing values*).

```{code-cell} ipython3
d = {'a' : 0, 'b' : 1, 'c' : 2}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)
```


O `pandas` uso o marcador `NaN` para indicar **valores em falta**.

Esta representação do conceito de *valores em falta* (que também existe no `numpy`) é muito útil: frequentemente lidamos com tabelas de dados em que não existem valores atribuídos em certas linhas e será conveniente assinalar esses valores.

Mais importante ainda, muitas funções de análise disponíveis no `pandas` levam em conta a existência de *valores em falta* que são pura e simplesmente ignorados. Por exemplo, o cálculo do desvio padrão de uma série ignora as entradas com *valores em falta*.

Usando a função `Series.reindex()` podem aparecer valores *valores em falta*:

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind = 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez'.split()

meses = pd.Series(ndias, index=ind)

alguns_meses = meses.reindex(['Dez', 'Set', 'não vai dar', 'Abr'])

print(alguns_meses)
```


### Funções descritivas

As Séries têm muitas [funções descritivas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) de grande utilidade.

Por exemplo, `sum()`, `mean()`, `std()` e `var()` calculam a soma, média, desvio padrão e variância dos valores da *Series*, respetivamente.

Note-se que, em geral, **os valores em falta são ignorados nos
cálculos**.

```{code-cell} ipython3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])

print(s)

print('\nMédia =', s.mean())
```


`Series.value_counts()` é outra função particularmente útil. O resultado é uma contagem dos valores diferentes da *Series*:

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind = 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez'.split()
meses = pd.Series(ndias, index=ind)

cont_dias = meses.value_counts()

print(cont_dias)
```


Outra função interessante é a função `Series.describe()`:

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind = 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez'.split()
meses = pd.Series(ndias, index=ind)

stats = meses.describe()

print(stats)
```


Outra função útil é a `Series.cumsum()`, a soma acumulada ao longo da *Series*:

```{code-cell} ipython3
ndias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ind = 'Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez'.split()
meses = pd.Series(ndias, index=ind)

totais = meses.cumsum()

print(totais)
```


Repare-se num pormenor interessante: o resultado destas 3 últimas funções é
também uma *Series*.

Se quiser saber quantos dias do ano passaram no final de outubro podemos  simplesmente indexar a soma acumulada com `'Out'`

    meses.cumsum()['Out']

Finalmente, tal como se fossem dicionários, a função `len()`e o operador `in` também funcionam com *Series*.

### Operações vetoriais

As Séries comportam-se como *arrays* do módulo `numpy`: podemos executar operações vetoriais:

```{code-cell} ipython3
d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 

print(s)
print('-----------------')
print(s**2)
```


Neste exemplo, elevámos a *Series* ao quadrado.

O *valor em falta* foi ignorado.

Também muito poderoso é o facto de que, quando aplicamos operações
vetoriais sobre *Series* (por exemplo, na soma de duas séries), os
valores são **alinhados** pelos respetivos *labels* antes da operação.

Vejamos esta soma de duas séries:

```{code-cell} ipython3
s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})

print('Soma')
print(s1 + s2)
```


A soma das duas Séries resulta numa Série em que todas os *labels*
estão presentes (**união de conjuntos**).

As que só existirem numa das Séries ou as que, numa das Séries, têm o
valor `NaN`, terão o valor `NaN` no resultado final.

A função `.dropna()` permite eliminar os *valores em falta*.

```{code-cell} ipython3
s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})
s3 = s1 + s2

print(s3.dropna())
```


## DataFrames

Numa definição muito simplificada:

Uma *DataFrame* é um quadro bidimensional, em que cada coluna se
comporta como uma Série, mas em que existe um índice comum a todas as
colunas.

Há muitas formas diferentes de criar uma *DataFrame*:

- a partir de listas de dicionários
- a partir de dicionários de listas
- a partir de *arrays*

Mas para ilustrar as possibilidades de criação de *DataFrames*, o primeiro exemplo mostra a criação
de uma *DataFrame* a partir de dados organizados em tabela num ficheiro de texto do tipo CSV:

```{code-cell} ipython3
import pandas as pd

pdata = pd.read_csv('planetdata.txt', sep='\t')

print(pdata)
```


Esta *DataFrame* tem 3 colunas, cada uma delas funciona como uma *Series*. Mas, todas as *Series* partilham o mesmo `index`, neste caso os números de 0 a 8.

Muitas vezes faz muito sentido que uma das colunas seja o `index`. Podemos passar uma coluna para funcionar como `index` com a função `DataFrame.set_index()`:

```{code-cell} ipython3
pdata = pd.read_csv('planetdata.txt', sep='\t')

pdata = pdata.set_index('Planet')

print(pdata)
```


Para obter uma das colunas, podemos indexar a *DataFrame* com
o nome da coluna:

```{code-cell} ipython3
pdata = pd.read_csv('planetdata.txt', sep='\t')
pdata = pdata.set_index('Planet')

rot_days = pdata['rotation_days']

print(rot_days)
```


ou, se o nome da coluna não tiver espaços, podemos simplesmente
usar o nome na forma `.nome`:

```{code-cell} ipython3
pdata = pd.read_csv('planetdata.txt', sep='\t')
pdata = pdata.set_index('Planet')

rot_days = pdata.rotation_days

print(rot_days)
```


Sendo as colunas *Series*, podemos usar toda a funcionalidade das *Series*:

```{code-cell} ipython3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


pdata = pd.read_csv('planetdata.txt', sep='\t').set_index('Planet')

print('Rotation:')
rot_days = pdata.rotation_days

print(rot_days.describe())

logrev = np.log10(pdata.revolution_years)

logrev.plot(marker='o', grid=True)
plt.show()
```

Interessante que o log do período de revolução seja quase linear.

Podemos fazer indexação por condições de toda a *DataFrame*

Em que planetas o dia é maior do que um dia na Terra?

```{code-cell} ipython3
pdata = pd.read_csv('planetdata.txt', sep='\t').set_index('Planet')

rot_days = pdata.rotation_days

longer_than1 = rot_days[rot_days > 1]

print(longer_than1)
```



## Exemplo: Tabela com informação Uniprot txt

Para ilustar o uso de uma `DataFrame` na organização e análise de dados, vamos ler a informação da UniProt sobre a levedura *S. cerevisiae* e realizar algumas análises sobre os comprimentos das proteínas, a abundância de aminoácidos e a contagem de *modificações pós-traducionais*.

### Preparação

O ficheiro de partida é o mesmo usado num capítulo anterior, o ficheiro _Unitprot text_ com a informação sobre as proteínas da levedura _S. cerevisiae_.

Recorde-se que para obter este ficheiro, deve-se proceder aos seguintes passos

- na UniProt procurar pelo "proteoma" da levedura _S. cerevisiae_ [www.uniprot.org/proteomes/UP000002311](https://www.uniprot.org/proteomes/UP000002311)
- Passar para resultados UniProtKB em "Map to Reviewed"
- Download -> Text
- Se o download tiver sido em modo "compressed", extraír o ficheiro do zip.
- Alterar o nome do ficheiro para `uniprot_scerevisiae.txt`

O ficheiro obtido deve estar na mesma pasta que os programas exibidos até ao final deste capítulo.


### Extração dos dados

Vamos criar uma *DataFrame* a partir de uma lista com dicionários. De toda a informação disponível no ficheiro UniProt txt, vamos extraír, para acada proteína,
o seu *número de acesso Uniprot*, com a chave `ac`, o comprimento da proteína, com a chave `n`, uma lista de modificações pós-traducionais, com a chave `PTMs` e a sequência da proteína, com a chave `seq`.

Desde que as chaves não mudem, podemos transformar uma lista de dicionários numa *DataFrame*, quase sem esforço.

Mas primeiro temos de criar essa lista de dicionários.

O programa seguinte cria justamente essa lista de dicionários. Grande parte deste programa repete o que foi já abordado num capítulo anterior, sobre a [extração de informação](uniprot_txt.md) a partir de ficheiros Uniprot txt.

Duas diferenças em relação a esse capítulo são de sublinhar:

- A sequência da proteína é agora também extraída. Num ficheiro de texto Uniprot txt, a sequência encontra-se na parte final do bloco de texto para cada proteína e é marcado por linhas que começam por, pelo menos, dois espaços em branco. Estas linhas são todas juntas numa única *string*, depois de eliminar os espaços.
- As modificações pós-traducionais são extraídas e representadas na forma de uma **lista de pares** em que cada par é constituído pela posição da PTM e nome da PTM.



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

data_filename = 'uniprot_scerevisiae.txt'
prots = read_Uniprot_text(data_filename)

def extract_info(record):
    """Reads a UniProt text record and returns a dict with extrated information.
    
    The returned dict has the following fields:
    
    'ac': the UniProt Access Id,
    'n': the sequence length, 
    'PTMs': a dictionary that associates the location of PTMs (int, as keys)
               with the name of the PTM.
    'seq': a string with the protein sequence
    """
    
    IDline, ACline, *otherlines = record.splitlines()
      
    ac = ACline.split(';',1)[0].split()[1]
    n = int(IDline.split()[3])
       
    PTMs = []
    seqlines = []
    for i, line in enumerate(otherlines):

        if line.startswith('FT   MOD_RES'):
            FTcode, MOD_RES, loc, *rest = line.split()
            
            nextline = otherlines[i+1]
            PTMtype = nextline.split('/note=')[1]
            PTMtype = PTMtype.strip('"')
            PTMtype = PTMtype.split(';')[0]
            
            PTMs.append((loc, PTMtype))
        if line.startswith('  '): # two spaces
            seqlines.append(line)
    # build seq string from seqlines
    seq = ''.join([line.replace(' ', '') for line in seqlines])
        
    # Return dictionary of extracted information
    return {'ac': ac, 'n': n, 'PTMs': PTMs, 'seq': seq}

all_prots = [extract_info(p) for p in prots]


print(f'The number of protein records in "{data_filename}" is {len(prots)}')

for p in all_prots[:4]:
    print('-----------------------------------')
    print(p)
```

```{admonition} Nota
:class: warning
Até ao final do capítulo considera-se que a lista de dicionários `all_prots` já foi construída pelas funções acima e não será repetida a sua construção.
```

### Transformação numa *DataFrame*

A lista de dicionários criada pode ser transformada numa *DataFrame* através da função `pandas.DataFrame()`:

```{code-cell} ipython3
prot_table = pd.DataFrame(all_prots)
prot_table
```

```{admonition} Nota
:class: note
Em certas plataformas de execução de código Python como, por exemplo, os *Jupyter notebooks*, existe um mecanismo de apresentação de objetos de uma forma mais flexível do que a função `print()`.

Se em qualquer célula de um *notebook* a última linha fôr apenas um objeto, geralmente o nome de um objeto, a palatforma Jupyter apresenta esse objeto num formato que pode ser visualmente muito apelativo.

É o caso das *DataFrames* que, se estiverem no final de uma célula, elas não só não necessitam da função `print()` como também são apresentadas como uma tabela do *browser* podendo ser "estilizadas" de diferentes formas.

No resto deste capítulo, as *DataFrames* (não as Series) serão apresentadas desta maneira e será evitado o uso da função `print()` para as apresentar, como no exemplo acima.
```

Na *DataFrame* que acabámos de obter faz todo o sentido que o `index` seja a coluna com o número de acesso Uniprot.

Para "promover" a coluna `ac` ao `index`, usamos a função `.set_index()`:

```{code-cell} ipython3
prot_table = prot_table.set_index('ac')
prot_table
```

### Uso da DataFrame

Agora que a informação está contida na *DataFrame* podemos ilustrar o uso da funcionalidade das *DataFrames* para de uma forma compacta rspondermos a certas perguntas interessantes.

#### Qual a proteína mais pequena. Qual a maior?

A coluna `n` da *DataFrame* tem a informação sobre os comprimentos da proteínas.

Poderíamos saber qual o máximo e o mínimo desses valores, mas, ainda melhor, as *Series* têm as funções `idxmin()` e `idxmax()` que nos dão os valores do `index` correspondentes ao mínimo e máximo de uma coluna. Neste caso obtemos os números de acesso UniProt das proteínas como o comprimento mínimo e máximo.

```{code-cell} ipython3
# mais pequena

pos = prot_table.n.idxmin()
pos
```

```{code-cell} ipython3
posmin = prot_table.n.idxmin()
posmax = prot_table.n.idxmax()
```

Com um valor de um `index` podemos obter a linha da *DataFrame* usando `.loc[]` (não é uma função é uma forma de indexação de *DataFrames*).

A proteína menor é:

```{code-cell} ipython3
prot_table.loc[posmin]
```

E a maior é (com 4910 aminoácidos!):

```{code-cell} ipython3
prot_table.loc[posmax]
```

Como obter a apenas a sequência da proteína maior de todas?

Como o resultado de `.loc` é ele próprio uma *Series* (ou uma *DataFrame* se houver mais do que um máximo) podemos voltar a indexar para obtermos apenas a sequência (uma *string*):

```{code-cell} ipython3
prot_table.loc[posmax].seq
```

Repare-se que não foi preciso fazer

    prot_table.loc[posmax]['seq']

Bastou fazer

    prot_table.loc[posmax].seq


Que PTMs existem na maior proteína?

```{code-cell} ipython3
prot_table.loc[posmax].PTMs
```

#### Quais as 20 proteínas mais pequenas de S.cerevisiae?

Para responder a esta pergunta podermos usar a possibilidade de ordenarmos as linhas de uma *DataFrame* pelos valores de uma coluna.

Depois de uma *DataFrame* ordenada as funções `.head()` e `.tail()`para obtermos uma *DataFrame* com as primeiras ou últimas linhas da *DataFrame*, respetivamente (indicamos o número de linhas no argumento destas funções.)

Assim, para obter as 20 proteínas mais curtas:

```{code-cell} ipython3
ord_prot_table = prot_table.sort_values(by='n')
ord_prot_table.head(20)
```
#### Quais as 20 proteínas maiores de S.cerevisiae?

Para as 20 maiores usamos a função `.tail()` da *DataFrame* ordenada:

```{code-cell} ipython3
ord_prot_table.tail(20)
```

#### Histograma da distribuição de tamanhos

De entre várias maneiras de obter o histograma de tamanhos, podemos usar a função `distplot()` do módulo `seaborn`. A ideia é aplicar esta função à coluna `n` da *dataFrame*:

```{code-cell} ipython3
from matplotlib import pyplot as plt
import seaborn as sns
f, ax = plt.subplots(figsize=(12,6))
sns.set()

sns.histplot(ord_prot_table.n, ax=ax, kde=False, bins=100)

plt.xlim(0,2500)
ax.tick_params(labelsize=16)

ax.set_xlabel('Protein length', fontsize=16)
ax.set_ylabel('Protein count', fontsize=16)
plt.show()
```

De entre os vários comandos e argumentos de natureza "cosmética" vale a pena indicar o argumanto `bins` que controla o número de intervalos em que se faz a contagem dos comprimentos.

#### Contagens e distribuição dos 20 aminoácidos nas proteínas

Este problema parece complicado: temos as sequências de mais de 6 000 proteínas e pretendemos contar os 20 aminoácidos em todas estas sequências.

Naturalmente poderíamos escrever um bloco `for`  em que passaríamos pro todas as linhas da *DataFrame*, obtendo a sequência e adicionando a contadores as novas contagens dos 20 aminoácidos por sequência.

Mas o *pandas* e um outro tipo de objetos pode-nos ajudar a resolver o problema de uma forma muito mais simples.

E se não tivessemos as sequências separadas? Se tivessemos todas as sequências numa imensa *string* com todos os aminoácidos de todas as proteínas? Seria mais fácil contar os 20 aminoácidos.

Comecemos por aí: juntar as sequências das 6 000 proteínas.

```{code-cell} ipython3
all_aminoacids = prot_table.seq.str.cat()
```

Se uma coluna (uma *Series*) tiver informação de natureza textual (*strings*) podemos usar [muitas funções](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#method-summary) com o prefixo `.str` que aplicam operações sobre *strings* **de uma forma vetorial** a toda a coluna.

Por exemplo, `.str.replace()` funciona como a função `replace()` das *strings* mas é aplicada a toda uma coluna de uma *DataFrame*.

Neste caso usámos `.str.cat()` à coluna da sequência. Esta função junta todas as *strings* da coluna.

Agora que `all_aminoacids` é uma *string* com milhões de letras, contendo todas sequências juntas, como contar os aminoácidos?

Faremos uso de algo que existe disponível na linguagem Python mas não pertence ao *pandas*: os objetos `Counter` do módulo `collections`.

Estes objetos `Counter` resolvem um problema que ocorre com muita frequência: contar os objetos diferentes que existem numa coleção (lista, dicionário, *string*).

Se um `Counter` for criado a partir de uma *string*, as letras diferentes são contadas e o resultado comporta-se como um dicionário, em que cada elemento é associado à sua contagem.

Basta criar `Counter` a partir de `all_aminoacids` e temos as contagens:

```{code-cell} ipython3
all_aminoacids = prot_table.seq.str.cat()

print(f'There are {len(all_aminoacids)} amino acids in all proteins')

from collections import Counter

aminoacid_counts = Counter(all_aminoacids)

# transformar o dicionário numa Series e ordenar

aminoacid_counts = pd.Series(aminoacid_counts).sort_values(ascending=False)

print(aminoacid_counts)
```

Mas o melhor é fazer um gráfico com as frequências:

```{code-cell} ipython3
all_aminoacids = prot_table.seq.str.cat()


from collections import Counter

aminoacid_counts = Counter(all_aminoacids)

aminoacid_counts = pd.Series(aminoacid_counts).sort_values(ascending=False)
aminoacid_counts = aminoacid_counts / aminoacid_counts.sum()

plt.subplots(figsize=(12,6))
barplot = sns.barplot(x=aminoacid_counts.index,
                      y=aminoacid_counts.values,
                      palette='tab20b')
```
O aminoácido mais frequente é a leucina e o menos frequente é o triptofano!

#### Contagens globais das PTM

Finalmente, repetindo o problema do capítulo sobre a extração da informação sobre PTMs, vamos contar os tipos diferentes de PTM usando o *pandas*.

A informação sobre PTMs aparentemente não está facilmente processável: está na coluna `PTMs` mas na forma de uma lista de pares.

A função `explode()` trata do problema de desdobrar a lista em várias linhas diferentes, ainda que à custa de ter de repetir os valore do `index`.

Vamos aplicar a função à coluna `PTMs`. Mas, já agora, descartamos as linhas para as quais não existem *PTMs* com a função `dropna()` que descarta linhas com valores em falta:

```{code-cell} ipython3
PTM_locs = prot_table.PTMs.explode()
PTM_locs = PTM_locs.dropna()
PTM_locs.head(30)
```

Como se pode ver com os primeiros 30 elementos, a função `explode()` desdobrou as listas.

Agora precisamos de obter apenas os nomes das *PTMs* e não precisamos de usar as localizações. Precisamos apenas, em cada par, dos elementos da posição 1.

`.str.get()` faz precisamente isso, de uma forma vetorial:

```{code-cell} ipython3
PTMs = PTM_locs.str.get(1)
PTMs
```

Agora só falta contar os elementos diferentes  nesta *Series*.

O *pandas* tem uma função muito semelhante aos `Counter`: a `value_counts()`:

```{code-cell} ipython3
PTM_counts = PTMs.value_counts(ascending=False)
PTM_counts
```

Agora só as PTMs que ocorrem mais do que 10 vezes:

```{code-cell} ipython3
more_than10 = PTM_counts[PTM_counts >= 10]
more_than10
```

Finalmente, um gráfico...

```{code-cell} ipython3
f, ax = plt.subplots(figsize=(8,12))

bp = sns.barplot(x=more_than10.values,
                 y=more_than10.index,
                 palette='tab20', orient='h', log=True)

ax.tick_params(labelsize=16)
plt.show()
```


