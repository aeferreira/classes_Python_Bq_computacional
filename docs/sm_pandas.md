# pandas


[![](images/pandas.svg)](https://pandas.pydata.org/)

### `Series`

> `Series` is a one-dimensional **labeled** array capable of holding any
> data type (integers, strings, floating point numbers, Python objects,
> etc.). The axis labels are collectively referred to as the **index**.

<div class="python_box">
``` python3
import pandas as pd
```
</div>

Uma Série (*Series*) é um conjunto (ordenado) de valores, mas cada valor
é associado a uma "etiqueta" (*label*).

Ao conjunto das etiquetas dá-se o nome de "**índice**".

Quando construímos uma Série, usando a função `Series()`, podemos
indicar o índice.

<div class="python_box">
``` python3
s = pd.Series([1.4, 2.2, 3.2, 6.5, 12],
              index=['a', 'b', 'c', 'd', 'e'])
print(s)
```
</div>

```
a     1.4
b     2.2
c     3.2
d     6.5
e    12.0
dtype: float64
```

Se não indicarmos um índice, o conjunto dos inteiros sucessivos será o
índice.

<div class="python_box">
``` python3
s = pd.Series([1.4,2.2,3.2,6.5,12])
print(s)
```
</div>

```
0     1.4
1     2.2
2     3.2
3     6.5
4    12.0
dtype: float64
```

As Séries podem ser construídas a partir de um dicionário, em que as
chaves são o índice.

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d)
print(s)
```
</div>

```
a    0.0
b    1.0
c    2.0
dtype: float64
```

Podemos, mesmo neste caso, indicar um índice. Caso o índice tenha
elementos para além das chaves do dicionário, haverá **valores em
falta**.

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)
```
</div>

```
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
```

O uso do marcador `NaN` para indicar **valores em falta** e a existência
de muitas funções de análise que levam em conta valores em falta são uma
característica muito poderosa do módulo `pandas`.

### Funções descritivas dos valores

As Séries têm algumas funções de estatística descritiva de grande
utilidade.

Note-se que, em geral, **os valores em falta são ignorados nos
cálculos**.

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)
print('\nMédia =', s.mean())
```
</div>

```
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64

Média = 1.0
```

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)
print('-----')
print(s.describe())
```
</div>

```
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
```

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s.cumsum())
```
</div>

```
b    1.0
c    3.0
d    NaN
a    3.0
dtype: float64
```

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])

print(s.values)
print(s.index.values)
```
</div>

```
[  1.   2.  nan   0.]
['b' 'c' 'd' 'a']
```

### Indexação e operações vetoriais

As Séries podem ser usadas com indexação por números inteiros,
comportando-se como uma lista ou um *array* do `numpy`.

A função `len()`também funciona com séries.

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(len(s))
print(s[0])
print(s[-1])
```
</div>

```
4
1.0
0.0
```

As Séries podem ser usadas **como dicionários: as etiquetas comportam-se
como chaves** e são usadas para indexar uma Série. para obter um valor
(e também para modificar um valor).

Tal como nos dicionários, o operador `in` **testa a existência de uma
etiqueta**.

<div class="python_box">
``` python3
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)
print('-----------')
print(s['b'])
print(s.c) # notação abreviada
print('z' in s)
print('d' in s)
```
</div>

```
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
```

Mas as Séries são muito mais poderosas: elas comportam-se como *arrays*
do módulo `numpy`. Podemos usar:

-   *slices*
-   **operações vetoriais**.

<div class="python_box">
``` python3
d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
print(s)

print(s[:3])
```
</div>

```
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
```

<div class="python_box">
``` python3
d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
print(s)

print(s**2)
```
</div>

```
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
```

<div class="python_box">
``` python3
d = {'a' : 0.5, 'b' : 1.0, 'c' : 3.0, 'e': 1.8}
s = pd.Series(d, index=['b', 'c', 'd', 'e', 'a']) 
print(s)

print(s[s > 1.1])
```
</div>

```
b    1.0
c    3.0
d    NaN
e    1.8
a    0.5
dtype: float64
c    3.0
e    1.8
dtype: float64
```

Também muito poderoso é o facto de que, quando aplicamos operações
vetoriais sobre Séries (por exemplo, na soma de duas séries), **os
valores são "alinhados" pelos respetivos *labels*** antes da operação.
Vejamos estas duas séries:

<div class="python_box">
``` python3
s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})

print('Soma')
print(s1 + s2)
```
</div>

```
Soma
a    1.0
b    2.0
e    NaN
f    NaN
dtype: float64
```

A soma das duas Séries resulta numa Série em que todas as etiquetas
estão presentes (**união de conjuntos**).

As que só existirem numa das Séries ou as que, numa das Séries, têm o
valor `NaN`, terão o valor `NaN` no resultado final.

A função `.dropna()` permite eliminar os *valores em falta*.

<div class="python_box">
``` python3
s1 = pd.Series({'a' : 0.5, 'b' : 1.0, 'e': 1.8})
s2 = pd.Series({'a' : 0.5, 'b' : 1.0, 'f': 1.8})
s3 = s1 + s2

print(s3.dropna())
```
</div>

```
a    1.0
b    2.0
dtype: float64
```

### `DataFrame`

> `DataFrame` is a **2-dimensional labeled data structure** with columns
> of potentially different types. You can think of it like a spreadsheet
> or SQL table, or a **dict of Series objects**. It is generally the
> most commonly used pandas object.

Uma *DataFrame* é um quadro bidimensional, em que cada coluna se
comporta como uma Série, mas em que existe um índice comum a todas as
colunas.

Para ilustar o uso de uma `DataFrame`, vamos ler e processar a
informação da UniProt sobre a levedura *S. cerevisiae*.

## Exemplo: Tabela com informação Uniprot txt

### Preparação

Ficheiro _Unitprot text_ com a informação sobre as proteínas da levedura _S. cerevisiae_. Para obter este ficheiro,

- na UniProt procurar pelo "proteoma" da levedura _S. cerevisiae_ [www.uniprot.org/proteomes/UP000002311](https://www.uniprot.org/proteomes/UP000002311)
- Passar para resultados UniProtKB em "Map to Reviewed"
- Download -> Text
- Se o download tiver sido em modo "compressed", extraír o ficheiro do zip.
- Alterar o nome do ficheiro para `uniprot_scerevisiae.txt`


### Extração dos dados

<div class="python_box">
```python3
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

print(f'The number of protein records in "{data_filename}" is {len(prots)}')

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
for p in all_prots[:4]:
    print('-----------------------------------')
    print(p)
```
</div>

```
The number of protein records in "uniprot_scerevisiae.txt" is 6049
-----------------------------------
{'ac': 'P38090', 'n': 596, 'PTMs': [], 'seq': 'MTKERMTIDYENDGDFEYDKNKYKTITTRIKSIEPSEGWLEPSGSVGHINTIPEAGDVHVDEHEDRGSSIDDDSRTYLLYFTETRRKLENRHVQLIAISGVIGTALFVAIGKALYRGGPASLLLAFALWCVPILCITVSTAEMVCFFPVSSPFLRLATKCVDDSLAVMASWNFWFLECVQIPFEIVSVNTIIHYWRDDYSAGIPLAVQVVLYLLISICAVKYYGEMEFWLASFKIILALGLFTFTFITMLGGNPEHDRYGFRNYGESPFKKYFPDGNDVGKSSGYFQGFLACLIQASFTIAGGEYISMLAGEVKRPRKVLPKAFKQVFVRLTFLFLGSCLCVGIVCSPNDPDLTAAINEARPGAGSSPYVIAMNNLKIRILPDIVNIALITAAFSAGNAYTYCSSRTFYGMALDGYAPKIFTRCNRHGVPIYSVAISLVWALVSLLQLNSNSAVVLNWLINLITASQLINFVVLCIVYLFFRRAYHVQQDSLPKLPFRSWGQPYTAIIGLVSCSAMILIQGYTVFFPKLWNTQDFLFSYLMVFINIGIYVGYKFIWKRGKDHFKNPHEIDFSKELTEIENHEIESSFEKFQYYSKA'}
-----------------------------------
{'ac': 'Q12001', 'n': 544, 'PTMs': [], 'seq': 'MAIGKRLLVNKPAEESFYASPMYDFLYPFRPVGNQWLPEYIIFVCAVILRCTIGLGPYSGKGSPPLYGDFEAQRHWMEITQHLPLSKWYWYDLQYWGLDYPPLTAFHSYLLGLIGSFFNPSWFALEKSRGFESPDNGLKTYMRSTVIISDILFYFPAVIYFTKWLGRYRNQSPIGQSIAASAILFQPSLMLIDHGHFQYNSVMLGLTAYAINNLLDEYYAMAAVCFVLSICFKQMALYYAPIFFAYLLSRSLLFPKFNIARLTVIAFATLATFAIIFAPLYFLGGGLKNIHQCIHRIFPFARGIFEDKVANFWCVTNVFVKYKERFTIQQLQLYSLIATVIGFLPAMIMTLLHPKKHLLPYVLIACSMSFFLFSFQVHEKTILIPLLPITLLYSSTDWNVLSLVSWINNVALFTLWPLLKKDGLHLQYAVSFLLSNWLIGNFSFITPRFLPKSLTPGPSISSINSDYRRRSLLPYNVVWKSFIIGTYIAMGFYHFLDQFVAPPSKYPDLWVLLNCAVGFICFSIFWLWSYYKIFTSGSKSMKDL'}
-----------------------------------
{'ac': 'P53309', 'n': 568, 'PTMs': [('449', 'Phosphothreonine')], 'seq': 'MSSLYTKLVKGATKIKMAPPKQKYVDPILSGTSSARGLQEITHALDIRLSDTAWTIVYKALIVLHLMIQQGEKDVTLRHYSHNLDVFQLRKISHTTKWSSNDMRALQRYDEYLKTRCEEYGRLGMDHLRDNYSSLKLGSKNQLSMDEELDHVESLEIQINALIRNKYSVSDLENHLLLYAFQLLVQDLLGLYNALNEGVITLLESFFELSIEHAKRTLDLYKDFVDMTEYVVRYLKIGKAVGLKIPVIKHITTKLINSLEEHLREETKRQRGEPSEPQQDRKPSTAISSTSSHNNNSNDKNKSIAQKKLEQIREQKRLLEQQLQNQQLLISPTVPQDAYNPFGSQQQDLNNDTFSFEPTQPQMTAQVPQPTANPFLIPQQQQQALQLTSASTMPQPSEIQITPNLNNQQTGMYASNLQYTPNFTGSGFGGYTTTENNAIMTGTLDPTKTGSNNPFSLENIAREQQQQNFQNSPNPFTLQQAQTTPILAHSQTGNPFQAQNVVTSPMGTYMTNPVAGQLQYASTGAQQQPQMMQGQQTGYVMVPTAFVPINQQQQQQQHQQENPNLIDI'}
-----------------------------------
{'ac': 'P40467', 'n': 964, 'PTMs': [('166', 'Phosphoserine'), ('186', 'Phosphoserine'), ('963', 'Phosphoserine')], 'seq': 'MPEQAQQGEQSVKRRRVTRACDECRKKKVKCDGQQPCIHCTVYSYECTYKKPTKRTQNSGNSGVLTLGNVTTGPSSSTVVAAAASNPNKLLSNIKTERAILPGASTIPASNNPSKPRKYKTKSTRLQSKIDRYKQIFDEVFPQLPDIDNLDIPVFLQIFHNFKRDSQSFLDDTVKEYTLIVNDSSSPIQPVLSSNSKNSTPDEFLPNMKSDSNSASSNREQDSVDTYSNIPVGREIKIILPPKAIALQFVKSTWEHCCVLLRFYHRPSFIRQLDELYETDPNNYTSKQMQFLPLCYAAIAVGALFSKSIVSNDSSREKFLQDEGYKYFIAARKLIDITNARDLNSIQAILMLIIFLQCSARLSTCYTYIGVAMRSALRAGFHRKLSPNSGFSPIEIEMRKRLFYTIYKLDVYINAMLGLPRSISPDDFDQTLPLDLSDENITEVAYLPENQHSVLSSTGISNEHTKLFLILNEIISELYPIKKTSNIISHETVTSLELKLRNWLDSLPKELIPNAENIDPEYERANRLLHLSFLHVQIILYRPFIHYLSRNMNAENVDPLCYRRARNSIAVARTVIKLAKEMVSNNLLTGSYWYACYTIFYSVAGLLFYIHEAQLPDKDSAREYYDILKDAETGRSVLIQLKDSSMAASRTYNLLNQIFEKLNSKTIQLTALHSSPSNESAFLVTNNSSALKPHLGDSLQPPVFFSSQDTKNSFSLAKSEESTNDYAMANYLNNTPISENPLNEAQQQDQVSQGTTNMSNERDPNNFLSIDIRLDNNGQSNILDATDDVFIRNDGDIPTNSAFDFSSSKSNASNNSNPDTINNNYNNVSGKNNNNNNITNNSNNNHNNNNNDNNNNNNNNNNNNNNNNNSGNSSNNNNNNNNNKNNNDFGIKIDNNSPSYEGFPQLQIPLSQDNLNIEDKEEMSPNIEIKNEQNMTDSNDILGVFDQLDAQLFGKYLPLNYPSE'}
```

### Transformação numa *DataFrame*



<div class="python_box">
```python3
prot_table = pd.DataFrame(all_prots)
prot_table
```
</div>


|    | ac     |   n | PTMs                                                                           | seq                      |
|:---|:-------|:----|:-------------------------------------------------------------------------------|:-------------------------|
|  0 | P38090 | 596 | []                                                                             | MTKERMTIDYENDGDFEYDKN... |
|  1 | Q12001 | 544 | []                                                                             | MAIGKRLLVNKPAEESFYASP... |
|  2 | P53309 | 568 | [('449', 'Phosphothreonine')]                                                  | MSSLYTKLVKGATKIKMAPPK... |
|  3 | P40467 | 964 | [('166', 'Phosphoserine'), ('186', 'Phosphoserine'), ('963', 'Phosphoserine')] | MPEQAQQGEQSVKRRRVTRAC... |
|  4 | P0CZ17 | 362 | []                                                                             | MRSLNTLLLSLFVAMSSGAPL... |
| ... |    |    |    |    |

6049 rows × 4 columns

<div class="python_box">
```python3
prot_table = prot_table.set_index('ac')
prot_table
```
</div>


|        | n   | PTMs                                                                           | seq                      |
|:-------|:----|:-------------------------------------------------------------------------------|:-------------------------|
| ac  |  |  | |
| P38090 | 596 | []                                                                             | MTKERMTIDYENDGDFEYDKN... |
| Q12001 | 544 | []                                                                             | MAIGKRLLVNKPAEESFYASP... |
| P53309 | 568 | [('449', 'Phosphothreonine')]                                                  | MSSLYTKLVKGATKIKMAPPK... |
| P40467 | 964 | [('166', 'Phosphoserine'), ('186', 'Phosphoserine'), ('963', 'Phosphoserine')] | MPEQAQQGEQSVKRRRVTRAC... |
| P0CZ17 | 362 | []                                                                             | MRSLNTLLLSLFVAMSSGAPL... |
| ... |    |    |      |

6049 rows × 3 columns

### Uso da DataFrame

#### Qual a proteína mais pequena. Qual a maior?

<div class="python_box">
```python3
# mais pequena

pos = prot_table.n.idxmin()
pos
```
</div>

```
'Q3E775'
```

<div class="python_box">
```python3
posmin = prot_table.n.idxmin()
posmax = prot_table.n.idxmax()
```
</div>

<div class="python_box">
```python3
prot_table.loc[posmin]
```
</div>


```
n                     16
PTMs                  []
seq     MLSLIFYLRFPSYIRG
Name: Q3E775, dtype: object
```


<div class="python_box">
```python3
prot_table.loc[posmax]
```
</div>

```
n                                                    4910
PTMs    [(1026, Phosphothreonine), (2971, Phosphoserin...
seq     MSQDRILLDLDVVNQRLILFNSAFPSDAIEAPFHFSNKESTSENLD...
Name: Q12019, dtype: object
```

Como obter a sequência da proteína maior de todas?

<div class="python_box">
```python3
prot_table.loc[posmax].seq
```
</div>



```
'MSQDRILLDLDVVNQRLILFNSAFPSDAIEAPFHFSNKESTSENLDNLAGTILHSRSITGHVFLYKHIFLEIVARWIKDSKKKDYVLVIEKLASIITIFPVAMPLIEDYLDKENDHFITILQNPSTQKDSDMFKILLAYYRLLYHNKEVFARFIQPDILYQLVDLLTKEQENQVVIFLALKVLSLYLDMGEKTLNDMLDTYIKSRDSLLGHFEGDSGIDYSFLELNEAKRCANFSKLPSVPECFTIEKKSSYFIIEPQDLSTKVASICGVIVPKVHTIHDKVFYPLTFVPTHKTVSSLRQLGRKIQNSTPIMLIGKAGSGKTFLINELSKYMGCHDSIVKIHLGEQTDAKLLIGTYTSGDKPGTFEWRAGVLATAVKEGRWVLIEDIDKAPTDVLSILLSLLEKRELTIPSRGETVKAANGFQLISTVRINEDHQKDSSNKIYNLNMIGMRIWNVIELEEPSEEDLTHILAQKFPILTNLIPKLIDSYKNVKSIYMNTKFISLNKGAHTRVVSVRDLIKLCERLDILFKNNGINKPDQLIQSSVYDSIFSEAADCFAGAIGEFKALEPIIQAIGESLDIASSRISLFLTQHVPTLENLDDSIKIGRAVLLKEKLNIQKKSMNSTLFAFTNHSLRLMEQISVCIQMTEPVLLVGETGTGKTTVVQQLAKMLAKKLTVINVSQQTETGDLLGGYKPVNSKTVAVPIQENFETLFNATFSLKKNEKFHKMLHRCFNKNQWKNVVKLWNEAYKMAQSILKITNTENENENAKKKKRRLNTHEKKLLLDKWADFNDSVKKFEAQSSSIENSFVFNFVEGSLVKTIRAGEWLLLDEVNLATADTLESISDLLTEPDSRSILLSEKGDAEPIKAHPDFRIFACMNPATDVGKRDLPMGIRSRFTEIYVHSPERDITDLLSIIDKYIGKYSVSDEWVGNDIAELYLEAKKLSDNNTIVDGSNQKPHFSIRTLTRTLLYVTDIIHIYGLRRSLYDGFCMSFLTLLDQKSEAILKPVIEKFTLGRLKNVKSIMSQTPPSPGPDYVQFKHYWMKKGPNTIQEQAHYIITPFVEKNMMNLVRATSGKRFPVLIQGPTSSGKTSMIKYLADITGHKFVRINNHEHTDLQEYLGTYVTDDTGKLSFKEGVLVEALRKGYWIVLDELNLAPTDVLEALNRLLDDNRELFIPETQEVVHPHPDFLLFATQNPPGIYGGRKILSRAFRNRFLELHFDDIPQDELEIILRERCQIAPSYAKKIVEVYRQLSIERSASRLFEQKNSFATLRDLFRWALRDAVGYEQLAASGYMLLAERCRTPQEKVTVKKTLEKVMKVKLDMDQYYASLEDKSLEAIGSVTWTKGMRRLSVLVSSCLKNKEPVLLVGETGCGKTTICQLLAQFMGRELITLNAHQNTETGDILGAQRPVRNRSEIQYKLIKSLKTALNIANDQDVDLKELLQLYSKSDNKNIAEDVQLEIQKLRDSLNVLFEWSDGPLIQAMRTGNFFLLDEISLADDSVLERLNSVLEPERSLLLAEQGSSDSLVTASENFQFFATMNPGGDYGKKELSPALRNRFTEIWVPSMEDFNDVNMIVSSRLLEDLKDLANPIVKFSEWFGKKLGGGNATSGVISLRDILAWVEFINKVFPKIQNKSTALIQGASMVFIDALGTNNTAYLAENENDLKSLRTECIIQLLKLCGDDLELQQIETNEIIVTQDELQVGMFKIPRFPDAQSSSFNLTAPTTASNLVRVVRAMQVHKPILLEGSPGVGKTSLITALANITGNKLTRINLSEQTDLVDLFGADAPGERSGEFLWHDAPFLRAMKKGEWVLLDEMNLASQSVLEGLNACLDHRGEAYIPELDISFSCHPNFLVFAAQNPQYQGGGRKGLPKSFVNRFSVVFIDMLTSDDLLLIAKHLYPSIEPDIIAKMIKLMSTLEDQVCKRKLWGNSGSPWEFNLRDTLRWLKLLNQYSICEDVDVFDFVDIIVKQRFRTISDKNKAQLLIEDIFGKFSTKENFFKLTEDYVQINNEVALRNPHYRYPITQNLFPLECNVAVYESVLKAINNNWPLVLVGPSNSGKTETIRFLASILGPRVDVFSMNSDIDSMDILGGYEQVDLTRQISYITEELTNIVREIISMNMKLSPNATAIMEGLNLLKYLLNNIVTPEKFQDFRNRFNRFFSHLEGHPLLKTMSMNIEKMTEIITKEASVKFEWFDGMLVKAVEKGHWLILDNANLCSPSVLDRLNSLLEIDGSLLINECSQEDGQPRVLKPHPNFRLFLTMDPKYGELSRAMRNRGVEIYIDELHSRSTAFDRLTLGFELGENIDFVSIDDGIKKIKLNEPDMSIPLKHYVPSYLSRPCIFAQVHDILLLSDEEPIEESLAAVIPISHLGEVGKWANNVLNCTEYSEKKIAERLYVFITFLTDMGVLEKINNLYKPANLKFQKALGLHDKQLTEETVSLTLNEYVLPTVSKYSDKIKSPESLYLLSSLRLLLNSLNALKLINEKSTHGKIDELTYIELSAAAFNGRHLKNIPRIPIFCILYNILTVMSENLKTESLFCGSNQYQYYWDLLVIVIAALETAVTKDEARLRVYKELIDSWIASVKSKSDIEITPFLNINLEFTDVLQLSRGHSITLLWDIFRKNYPTTSNSWLAFEKLINLSEKFDKVRLLQFSESYNSIKDLMDVFRLLNDDVLNNKLSEFNLLLSKLEDGINELELISNKFLNKRKHYFADEFDNLIRYTFSVDTAELIKELAPASSLATQKLTKLITNKYNYPPIFDVLWTEKNAKLTSFTSTIFSSQFLEDVVRKSNNLKSFSGNQIKQSISDAELLLSSTIKCSPNLLKSQMEYYKNMLLSWLRKVIDIHVGGDCLKLTLKELCSLIEEKTASETRVTFAEYIFPALDLAESSKSLEELGEAWITFGTGLLLLFVPDSPYDPAIHDYVLYDLFLKTKTFSQNLMKSWRNVRKVISGDEEIFTEKLINTISDDDAPQSPRVYRTGMSIDSLFDEWMAFLSSTMSSRQIKELVSSYKCNSDQSDRRLEMLQQNSAHFLNRLESGYSKFADLNDILAGYIYSINFGFDLLKLQKSKDRASFQISPLWSMDPINISCAENVLSAYHELSRFFKKGDMEDTSIEKVLMYFLTLFKFHKRDTNLLEIFEAALYTLYSRWSVRRFRQEQEENEKSNMFKFNDNSDDYEADFRKLFPDYEDTALVTNEKDISSPENLDDIYFKLADTYISVFDKDHDANFSSELKSGAIITTILSEDLKNTRIEELKSGSLSAVINTLDAETQSFKNTEVFGNIDFYHDFSIPEFQKAGDIIETVLKSVLKLLKQWPEHATLKELYRVSQEFLNYPIKTPLARQLQKIEQIYTYLAEWEKYASSEVSLNNTVKLITDLIVSWRKLELRTWKGLFNSEDAKTRKSIGKWWFYLYESIVISNFVSEKKETAPNATLLVSSLNLFFSKSTLGEFNARLDLVKAFYKHIQLIGLRSSKIAGLLHNTIKFYYQFKPLIDERITNGKKSLEKEIDDIILLASWKDVNVDALKQSSRKSHNNLYKIVRKYRDLLNGDAKTIIEAGLLYSNENKLKLPTLKQHFYEDPNLEASKNLVKEISTWSMRAAPLRNIDTVASNMDSYLEKISSQEFPNFADLASDFYAEAERLRKETPNVYTKENKKRLAYLKTQKSKLLGDALKELRRIGLKVNFREDIQKVQSSTTTILANIAPFNNEYLNSSDAFFFKILDLLPKLRSAASNPSDDIPVAAIERGMALAQSLMFSLITVRHPLSEFTNDYCKINGMMLDLEHFTCLKGDIVHSSLKANVDNVRLFEKWLPSLLDYAAQTLSVISKYSATSEQQKILLDAKSTLSSFFVHFNSSRIFDSSFIESYSRFELFINELLKKLENAKETGNAFVFDIIIEWIKANKGGPIKKEQKRGPSVEDVEQAFRRTFTSIILSFQKVIGDGIESISETDDNWLSASFKKVMVNVKLLRSSVVSKNIETALSLLKDFDFTTTESIYVKSVISFTLPVITRYYNAMTVVLERSRIYYTNTSRGMYILSTILHSLAKNGFCSPQPPSEEVDDKNLQEGTGLGDGEGAQNNNKDVEQDEDLTEDAQNENKEQQDKDERDDENEDDAVEMEGDMAGELEDLSNGEENDDEDTDSEEEELDEEIDDLNEDDPNAIDDKMWDDKASDNSKEKDTDQNLDGKNQEEDVQAAENDEQQRDNKEGGDEDPNAPEDGDEEIENDENAEEENDVGEQEDEVKDEEGEDLEANVPEIETLDLPEDMNLDSEHEESDEDVDMSDGMPDDLNKEEVGNEDEEVKQESGIESDNENDEPGPEEDAGETETALDEEEGAEEDVDMTNDEGKEDEENGPEEQAMSDEEELKQDAAMEENKEKGGEQNTEGLDGVEEKADTEDIDQEAAVQQDSGSKGAGADATDTQEQDDVGGSGTTQNTYEEDQEDVTKNNEESREEATAALKQLGDSMKEYHRRRQDIKEAQTNGEEDENLEKNNERPDEFEHVEGANTETDTQALGSATQDQLQTIDEDMAIDDDREEQEVDQKELVEDADDEKMDIDEEEMLSDIDAHDANNDVDSKKSGFIGKRKSEEDFENELSNEHFSADQEDDSEIQSLIENIEDNPPDASASLTPERSLEESRELWHKSEISTADLVSRLGEQLRLILEPTLATKLKGDYKTGKRLNMKRIIPYIASQFRKDKIWLRRTKPSKRQYQIMIALDDSKSMSESKCVKLAFDSLCLVSKTLTQLEAGGLSIVKFGENIKEVHSFDQQFSNESGARAFQWFGFQETKTDVKKLVAESTKIFERARAMVHNDQWQLEIVISDGICEDHETIQKLVRRARENKIMLVFVIIDGITSNESILDMSQVNYIPDQYGNPQLKITKYLDTFPFEFYVVVHDISELPEMLSLILRQYFTDLASS'
```



<div class="python_box">
```python3
prot_table.loc[posmax].PTMs
```
</div>



    [('1026', 'Phosphothreonine'),
     ('2971', 'Phosphoserine'),
     ('4353', 'Phosphoserine'),
     ('4388', 'Phosphothreonine'),
     ('4555', 'Phosphoserine')]



#### Quais as 20 proteínas mais pequenas de S.cerevisiae?

<div class="python_box">
```python3
ord_prot_table = prot_table.sort_values(by='n')
ord_prot_table.head(20)
```
</div>


|            |   n | PTMs   | seq                           |
|:-----------|:----|:-------|:------------------------------|
| ac         |     |        |                               |
| Q3E775     |  16 | []     | MLSLIFYLRFPSYIRG              |
| P08521     |  25 | []     | MFSLSNSQYTCQDYISDHIWKTSSH     |
| P0CX86     |  25 | []     | MRAKWRKKRTRRLKRKRRKVRARSK     |
| P0CX87     |  25 | []     | MRAKWRKKRTRRLKRKRRKVRARSK     |
| P0C5N4     |  26 | []     | MYFHSFLDTFSKYLGSTSCPLLRLSR    |
| P0C5S1     |  26 | []     | MVYVMSMVSLLKRLLTVTRWKLQITG    |
| Q8TGV0     |  26 | []     | MRLNYSRCYYSSQRRRQSLPKRFPLI    |
| Q3E7Z6     |  27 | []     | MTAFASLREPLVLANLKIKVHIYRMKR   |
| Q3E801     |  27 | []     | MTRCISKKMLLEVDALSLIYSPHLYMS   |
| P0C5K9     |  27 | []     | MWGLNRWLTFTMLILLITSHCCYWNKR   |
| Q8TGN3     |  28 | []     | MPGIAFKGKDMVKAIQFLEIVVPCHCTT  |
| A0A0B7P221 |  28 | []     | MIRQKIFVFIVKSRRNSICPAIRRKEDY  |
| Q8TGS7     |  28 | []     | MRKPSAFHACNIIFLPLVKCASATIMLN  |
| Q3E838     |  28 | []     | MLPRKYKPAYKKQAHRVKSNPQPAYTFQ  |
| Q8TGT8     |  28 | []     | MNLNAYFEAYQAIFPFLLEAFLRKEQKV  |
| Q8TGU0     |  28 | []     | MLPSISFDYIKRPNIVLFSNVLSLSSNI  |
| Q8TGT6     |  29 | []     | MKIKFSRGARFSATFSFDKYPFLLYEVVR |
| P0C5M8     |  29 | []     | MPLEVLGHLSKAFLFLARNNEHSHKKYNQ |
| Q8TGS6     |  29 | []     | MFKMKFGDTLPRSDFGTGGNKQAPGLELG |
| P0C1Z1     |  29 | []     | MKRSYKTLPTYFFSFFGPFKERAVFLLVL |

#### Quais as 20 proteínas maiores de S.cerevisiae?

<div class="python_box">
```python3
ord_prot_table.tail(20)
```
</div>


|        |    n | PTMs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | seq                      |
|:-------|:-----|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| ac |   |    |    |
| P34756 | 2278 | [('2', 'N-acetylserine'), ('186', 'Phosphoserine'), ('1627', 'Phosphoserine'), ('1630', 'Phosphoserine'), ('1938', 'Phosphoserine'), ('1953', 'Phosphothreonine')]                                                                                                                                                                                                                                                                                                                                                           | MSSEEPHASISFPDGSHVRSS... |
| P38111 | 2368 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MESHVKYLDELILAIKDLNSG... |
| P40468 | 2376 | [('141', 'Phosphoserine'), ('1144', 'Phosphoserine'), ('2264', 'Phosphothreonine'), ('2267', 'Phosphoserine'), ('2355', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                                                    | MASRFTFPPQRDQGIGFTFPP... |
| P33334 | 2413 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MSGLPPPPPGFEEDSDLALPP... |
| P35169 | 2470 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MEPHEEQIWKSKLLKAANNDM... |
| P32600 | 2474 | [('10', 'Phosphothreonine')]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | MNKYINKYTTPPNLLSLRQRA... |
| Q06116 | 2489 | [('2254', 'Phosphoserine'), ('2278', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | MSMLPWSQIRDVSKLLLGFML... |
| P35194 | 2493 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MAKQRQTTKSSKRYRYSSFKA... |
| Q06179 | 2628 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MMFPINVLLYKWLIFAVTFLW... |
| P33892 | 2672 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MTAILNWEDISPVLEKGTRES... |
| Q00402 | 2748 | [('611', 'Phosphoserine'), ('675', 'Phosphoserine'), ('746', 'Phosphoserine'), ('881', 'Phosphoserine'), ('945', 'Phosphoserine'), ('1009', 'Phosphoserine'), ('1201', 'Phosphoserine'), ('1265', 'Phosphoserine'), ('1329', 'Phosphoserine'), ('2162', 'Phosphoserine'), ('2164', 'Phosphoserine'), ('2197', 'Phosphoserine'), ('2217', 'Phosphoserine'), ('2220', 'Phosphoserine'), ('2221', 'Phosphoserine'), ('2360', 'Phosphoserine'), ('2424', 'Phosphoserine'), ('2494', 'Phosphoserine'), ('2545', 'Phosphoserine')] | MSHNNRHKKNNDKDSSAGQYA... |
| P38110 | 2787 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MEDHGIVETLNFLSSTKIKER... |
| Q12150 | 2958 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MEAISQLRGVPLTHQKDFSWV... |
| P19158 | 3079 | [('635', 'Phosphothreonine')]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | MSQPTKNKKKEHGTDSKSSRM... |
| P18963 | 3092 | [('497', 'Phosphoserine'), ('915', 'Phosphoserine'), ('1342', 'Phosphoserine'), ('1753', 'Phosphoserine'), ('3004', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                                                        | MNQSDPQDKKNFPMEYSLTKH... |
| Q07878 | 3144 | [('1364', 'Phosphoserine'), ('1382', 'Phosphoserine'), ('1715', 'Phosphoserine'), ('1729', 'Phosphoserine'), ('1731', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                                                      | MLESLAANLLNRLLGSYVENF... |
| Q03280 | 3268 | [('1890', 'Phosphoserine'), ('2096', 'Phosphothreonine'), ('2119', 'Phosphoserine'), ('2376', 'Phosphoserine'), ('2406', 'Phosphoserine'), ('2418', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                        | MVLFTRCEKARKEKLAAGYKP... |
| P38811 | 3744 | [('2', 'N-acetylserine'), ('172', 'Phosphoserine'), ('542', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                                                                                                                | MSLTEQIEQFASRFRDDDATL... |
| P36022 | 4092 | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | MCKNEARLANELIEFVAATVT... |
| Q12019 | 4910 | [('1026', 'Phosphothreonine'), ('2971', 'Phosphoserine'), ('4353', 'Phosphoserine'), ('4388', 'Phosphothreonine'), ('4555', 'Phosphoserine')]                                                                                                                                                                                                                                                                                                                                                                                | MSQDRILLDLDVVNQRLILFN... |

#### Histograma da distribuição de tamanhos

<div class="python_box">
```python3
from matplotlib import pyplot as plt
import seaborn as sns
f, ax = plt.subplots(figsize=(12,6))
sns.set()

sns.distplot(ord_prot_table.n, kde=False, bins=100)

plt.xlim(0,2500)
ax.tick_params(labelsize=16)

ax.set_xlabel('Protein length', fontsize=16)
plt.show()
```
</div>


![](images/n_hist.png)


#### Contagens e distribuição dos 20 aminoácidos nas proteínas

<div class="python_box">
```python3
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
</div>


![](images/aa_freq.png)


#### Contagens globais das PTM

<div class="python_box">

```python3
PTM_locs = prot_table.PTMs.explode()
PTM_locs = PTM_locs.dropna()
PTM_locs.head(30)
```
</div>



```
ac
P53309    (449, Phosphothreonine)
P40467       (166, Phosphoserine)
P40467       (186, Phosphoserine)
P40467       (963, Phosphoserine)
P36076        (42, Phosphoserine)
P36076       (116, Phosphoserine)
P36076       (121, Phosphoserine)
P36076       (124, Phosphoserine)
P36076       (264, Phosphoserine)
P53388        (22, Phosphoserine)
P00431     (220, Phosphotyrosine)
P53968    (170, Phosphothreonine)
P53968       (175, Phosphoserine)
P53968       (245, Phosphoserine)
P53968       (385, Phosphoserine)
P89105      (1015, Phosphoserine)
P89105      (1017, Phosphoserine)
P07262        (2, N-acetylserine)
P38859      (4, Phosphothreonine)
P38859        (17, Phosphoserine)
P38859       (237, Phosphoserine)
P38859    (962, Phosphothreonine)
P54861       (629, Phosphoserine)
P14020        (2, N-acetylserine)
P14020       (141, Phosphoserine)
P32892       (208, Phosphoserine)
P43616       (451, Phosphoserine)
Q00684       (467, Phosphoserine)
Q06440       (441, Phosphoserine)
Q06440       (454, Phosphoserine)
Name: PTMs, dtype: object
```


<div class="python_box">
```python3
PTMs = PTM_locs.str.get(1)
PTMs
```
</div>


```
ac
P53309    Phosphothreonine
P40467       Phosphoserine
P40467       Phosphoserine
P40467       Phosphoserine
P36076       Phosphoserine
                ...       
Q04461       Phosphoserine
Q04461    Phosphothreonine
P38260       Phosphoserine
P42837       Phosphoserine
P32806       Phosphoserine
Name: PTMs, Length: 7070, dtype: object
```


<div class="python_box">
```python3
PTM_counts = PTMs.value_counts(ascending=False)
PTM_counts
```
</div>



```
Phosphoserine                                       5172
Phosphothreonine                                    1028
N-acetylserine                                       345
N-acetylmethionine                                   106
Phosphotyrosine                                       55
N6-(pyridoxal phosphate)lysine                        46
N6-acetyllysine                                       46
N-acetylalanine                                       37
Asymmetric dimethylarginine                           33
N6-methyllysine                                       24
Cysteine methyl ester                                 23
N6,N6,N6-trimethyllysine                              22
N6,N6-dimethyllysine                                  15
Omega-N-methylarginine                                15
N-acetylthreonine                                     12
N6-succinyllysine                                     11
N6-butyryllysine                                       8
N6-biotinyllysine                                      5
N,N-dimethylproline                                    4
Phosphohistidine                                       4
N5-methylglutamine                                     4
N6-lipoyllysine                                        4
N6-carboxylysine                                       4
Lysine derivative                                      3
Pyruvic acid (Ser)                                     3
N6-malonyllysine                                       3
S-glutathionyl cysteine                                3
O-(pantetheine 4'-phosphoryl)serine                    3
4-aspartylphosphate                                    3
3,4-dihydroxyproline                                   2
Tele-8alpha-FAD histidine                              2
N6-propionyllysine                                     2
Hypusine                                               2
N5-methylarginine                                      2
N-acetylvaline                                         2
Leucine methyl ester                                   2
Cysteine sulfinic acid (-SO2H)                         1
Thiazolidine linkage to a ring-opened DNA abasic       1
1-thioglycine                                          1
N6-crotonyllysine                                      1
N-formylmethionine                                     1
Pros-8alpha-FAD histidine                              1
Dimethylated arginine                                  1
Pros-methylhistidine                                   1
2,3-didehydroalanine (Cys)                             1
S-methylcysteine                                       1
S-(dipyrrolylmethanemethyl)cysteine                    1
N,N,N-trimethylglycine                                 1
Lysine methyl ester                                    1
Diphthamide                                            1
N6-glutaryllysine                                      1
Name: PTMs, dtype: int64
```


<div class="python_box">
```python3
more_than10 = PTM_counts[PTM_counts >= 10]
more_than10
```
</div>



```
Phosphoserine                     5172
Phosphothreonine                  1028
N-acetylserine                     345
N-acetylmethionine                 106
Phosphotyrosine                     55
N6-(pyridoxal phosphate)lysine      46
N6-acetyllysine                     46
N-acetylalanine                     37
Asymmetric dimethylarginine         33
N6-methyllysine                     24
Cysteine methyl ester               23
N6,N6,N6-trimethyllysine            22
N6,N6-dimethyllysine                15
Omega-N-methylarginine              15
N-acetylthreonine                   12
N6-succinyllysine                   11
Name: PTMs, dtype: int64
```


<div class="python_box">
```python3
f, ax = plt.subplots(figsize=(8,12))

bp = sns.barplot(x=more_than10.values, y=more_than10.index, palette='tab20', orient='h', log=True)
ax.tick_params(labelsize=16)
plt.show()
```
</div>

![](images/ptm_counts.png)



