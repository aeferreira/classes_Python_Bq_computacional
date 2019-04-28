#  _Strings_

## Definição literal, iteração e indexação


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
aspas**: `"`, `'` ou `"""`.

As *aspas triplas* permitem definir literalmente uma *string* com várias
linhas.

``` python
a = "O Neo tomou o comprimido vermelho"

b ='What is the matrix?'

c ="There's no spoon"

d = """ Um pequeno texto que até
ocupa várias linhas

algumas das linhas estão em branco"""
```

### operador `+`.

O operador `+` serve para "juntar" várias *strings*, uma operação
designada por *concatenação*.

``` python
c = "There's no spoon"
print('c = ', c)

c = c + ', really, ' + 'none' + '.'

print('c = ', c)
```

```
c =  There's no spoon
c =  There's no spoon, really, none.
```

As strings têm muitas funções em comum com as listas:

-   `len()`, `count()`, `in`, `not in`
-   Indexação: `a[i]`
-   Iteração: `for i in a:`

Isto acontece porque as *strings* se comportam como uma **sequência de
caracteres**, tal como uma lista é uma sequência de quaisquer objetos.

### `len()`, `.count()`, operador `in`.

``` python
c = "There's no spoon"
print('c = ', c)
print('len(c) =', len(c))

print('c.count("s") = ', c.count('s'))

print('z' in c)
print('r' in c)
print('ere' in c)
```

```
c =  There's no spoon
len(c) = 16
c.count("s") =  2
False
True
True
```

### Iteração e indexação.

``` python
frase = "There's no spoon"

for i, c in enumerate(frase):
    print(i, c)
```

```
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
```

``` python
frase = "There's no spoon"

for i in range(-1, -len(frase)-1, -1):
    print(i, frase[i])
```

```
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
```

## Funções associadas a *strings*

Existem muitas funções associadas a *strings*

Consultar a documentação oficial em
[docs.python.org](https://docs.python.org/3/library/stdtypes.html#string-methods)

![](images/docspython_strmethods.png)

**São cerca de 40!**

## Imutabilidade

As *strings* são **imutáveis**.

Isto significa que (ao contrário das listas e dicionários) **não existem
funções para modificar uma** *string*.

**Não existe**, por exemplo, `s.append('a')`.

**Todas as operações com** *strings* **resultam numa** *string*
**nova**, à qual é, geralmente, atribuído um nome (mesmo que seja o
mesmo nome da *string* original)

Podemos, por isso, usar `s = s + 'a'`

### `.strip()`, `.startswith()`.

``` python
c = "    There's no spoon      "
print('c:')
print(c)

s = c.strip()
print('c.strip():')
print(s)
```

```
c:
    There's no spoon      
c.strip():
There's no spoon
```

``` python
c = "    There's no spoon      "

if s.strip().startswith('Th'):
    print('Começa por Th')
```

```
Começa por Th
```

### `.upper()`, `.lower()`.

``` python
c = "    There's no spoon      "

c_upper = c.upper()
print('c.upper():',c_upper)

c_lower = c.lower()
print('c.lower():',c_lower)
```

```
c.upper():     THERE'S NO SPOON      
c.lower():     there's no spoon      
```

### `.replace()`.

``` python
palavra = 'pois'
print(palavra)

palavra = palavra.replace('p', 'd')
print(palavra)
```

```
pois
dois
```

### `.split()` e `.join()`

``` python
a = "There's no spoon"

b = a.split()
c = a.split('e')
d = a.split("'")

print(b)
print(c)
print(d)
```

```
["There's", 'no', 'spoon']
['Th', 'r', "'s no spoon"]
['There', 's no spoon']
```

A função `.split()` **gera uma lista de partes**, encontrando um
separador numa *string*.

O separador a encontrar é o argumento da função.

Se não se usar um argumento, considera-se que as partes são separadas
por espaços, tabs ou mudanças de linha (no inglês genericamente
designados por *white space*)

A função `.join()` é uma espécie de inversa de `.split()`: transforma
**uma lista** de *strings* **numa única** *string*, interpondo um
separador:

``` python
aas = ['Arg', 'Tyr', 'Gly', 'Asp']

print(" ".join(aas))
print("-".join(aas))
print("".join(aas))
print("+".join(aas))
print("-CONH-".join(aas))
```

```
Arg Tyr Gly Asp
Arg-Tyr-Gly-Asp
ArgTyrGlyAsp
Arg+Tyr+Gly+Asp
Arg-CONH-Tyr-CONH-Gly-CONH-Asp
```

**Problema: transformar** `AUGUUCAAGGAGUAAUGCCCCCGACUA` **em**
`AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA`

``` python
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
```

```
AUGUUCAAGGAGUAAUGCCCCCGACUA
['AUG', 'UUC', 'AAG', 'GAG', 'UAA', 'UGC', 'CCC', 'CGA', 'CUA']
AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA
```

Tem de haver uma maneira mais sucinta de de juntar vários caracteres
consecutivos!

### `.splitlines()`

``` python
d = """ Um pequeno texto que até
ocupa várias linhas

algumas das linhas estão em branco"""

print(d.splitlines())
```

```
[' Um pequeno texto que até', 'ocupa várias linhas', '', 'algumas das linhas estão em branco']
```

A função `.splitlines()` é praticamente equivalente a `.split('\n')`.

É muito interessante o facto de podermos usar funções de *strings* em
conjunção com listas em compreensão:

**Problema: num texto com várias linhas, obter numa lista as linhas que
começam por uma vogal e têm menos de 20 caracteres**

``` python
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
```

```
['', 'Um pequeno texto que até', 'ocupa várias', 'linhas', '', 'mas haverá', 'Algumas em branco']
['ocupa várias', 'linhas', 'mas haverá', 'Algumas em branco']
['ocupa várias', 'Algumas em branco']
```

## _Slices_ 

Já vimos que podemos indexar listas e *strings*, usando `[]` e a posição
do elemento.

Os `[]` podem ser usados para um outro tipo de indexação de listas ou
_strings_: os **slices** (em português: "fatias").

Os *slices* extraem uma parte de uma lista ou *string* que podem ter
mais de um elemento.

A forma geral é `[início : fim(exclusivé) : passo]`. O `passo` é
opcional.

``` python
a = "O Neo tomou o comprimido vermelho"
#    012345678901234567890123456789012

print(a[2:5])
print(a[0:5])
print(a[6:-1])
```

```
Neo
O Neo
tomou o comprimido vermelh
```

``` python
a = "O Neo tomou o comprimido vermelho"
#    012345678901234567890123456789012

print(a[ :5])
print(a[6: ])
print(a[ : ])
print(a[0:12:2])
```

```
O Neo
tomou o comprimido vermelho
O Neo tomou o comprimido vermelho
ONotmu
```

**Problema: transformar** `AUGUUCAAGGAGUAAUGCCCCCGACUA` **em**
`AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA`

``` python
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
```

```
AUGUUCAAGGAGUAAUGCCCCCGACUA
AUG-UUC-AAG-GAG-UAA-UGC-CCC-CGA-CUA
```

Usando uma lista em compreensão como argumento da função `.join()` o
programa pode ficar mais compacto:

``` python
s = "AUGTTCAAGGAGUAAUGCCCCCGACUA"
sf = "-".join([s[i:i+3] for i in range(0,len(s),3)])

print(s)
print(sf)
```

```
AUGTTCAAGGAGUAAUGCCCCCGACUA
AUG-TTC-AAG-GAG-UAA-UGC-CCC-CGA-CUA
```

**Os** *slices* **também funcionam com listas**

``` python
aas = ['Arg', 'Tyr', 'Gly', 'Asp']

s1 = aas[ :2]
s2 = aas[-2: ]
s3 = aas[ : :2]

print(s1)
print(s2)
print(s3)
```

```
['Arg', 'Tyr']
['Gly', 'Asp']
['Arg', 'Gly']
```

!!! info "Importante"
    Os *slices* produzem sempre **novos** objetos

No caso de uma **lista**, podemos **atribuír valores a um** *slice* **da
lista**, mudando alguns elementos de uma só vez:

``` python
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(nums)
nums[3:5] = [8, 9]
print(nums)
```

```
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
[1, 2, 2, 8, 9, 3, 4, 4, 4, 4]
```

**Problema: Converter uma sequência com códigos de uma letra de
aminoácidos para códigos de 3 letras, usando um dicionário para a
conversão.**

Numa secção anterior, este problema foi resolvido anteriormente da
seguinte forma:

``` python
trans = {'A': 'Ala', 'C': 'Cys', 'E': 'Glu', 'D': 'Asp', 'G': 'Gly', 'F': 'Phe', 'I': 'Ile', 'H': 'His', 'K': 'Lys', 'M': 'Met', 'L': 'Leu', 'N': 'Asn', 'Q': 'Gln', 'P': 'Pro', 'S': 'Ser', 'R': 'Arg', 'T': 'Thr', 'W': 'Trp', 'V': 'Val', 'Y': 'Tyr'}

# Problema: transformar s1 numa string
# com os códigos de 3 letras dos aa
s1 = 'ADKLITCWFHHWE'

s3 = ''
for aa in s1:
    s3 = s3 + trans[aa] + '-'

print(s1, 'é o mesmo que ', s3)
```

```
ADKLITCWFHHWE é o mesmo que  Ala-Asp-Lys-Leu-Ile-Thr-Cys-Trp-Phe-His-His-Trp-Glu-
```

Podemos compactar o programa e melhorar o aspeto do resultado.

Por um lado, podemos usar uma lista em compreensão para gerar os códigos
de 3 letras (em vez de uma *string*), por outro podemos usar a função
`.join()` para apresenta-los separados por `-`.

``` python
trans = {'A': 'Ala', 'C': 'Cys', 'E': 'Glu', 'D': 'Asp', 'G': 'Gly', 'F': 'Phe', 'I': 'Ile', 'H': 'His', 'K': 'Lys', 'M': 'Met', 'L': 'Leu', 'N': 'Asn', 'Q': 'Gln', 'P': 'Pro', 'S': 'Ser', 'R': 'Arg', 'T': 'Thr', 'W': 'Trp', 'V': 'Val', 'Y': 'Tyr'}

s1 = 'ADKLITCWFHHWE'

s3 = '-'.join([trans[aa] for aa in s1])

print(s1, 'é o mesmo que', s3)
```

```
ADKLITCWFHHWE é o mesmo que Ala-Asp-Lys-Leu-Ile-Thr-Cys-Trp-Phe-His-His-Trp-Glu
```

**Problema: calcular o complemento reverso de uma sequência, mas
separando os codões por "-".**

``` python
bcompl = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

a = "ATGGTTACCTAGTATTTAGGATTA"
c = ''.join([bcompl[b] for b in a[ : :-1]])

print("Seq:")
print('-'.join([a[i:i+3] for i in range(0,len(a),3)]))

print("\nComplemento reverso:")
print('-'.join([c[i:i+3] for i in range(0,len(c),3)]))
```

```
Seq:
ATG-GTT-ACC-TAG-TAT-TTA-GGA-TTA

Complemento reverso:
TAA-TCC-TAA-ATA-CTA-GGT-AAC-CAT
```

Formatação de *strings* com `.format()`
---------------------------------------

``` python
x = 11
y = 20
z = 3

print('x = {}, y = {}, z = {}'.format(x, y, z))
```

```
x = 11, y = 20, z = 3
```

``` python
d = {'H':1, 'Li':3, 'Na':11, 'K':19}

for k, v in d.items():
    print('O elemento com n = {1} é o {0}'.format(k, v))
```

```
O elemento com n = 1 é o H
O elemento com n = 3 é o Li
O elemento com n = 11 é o Na
O elemento com n = 19 é o K
```

``` python
d = {'H':1, 'Li':3, 'Na':11, 'K':19}

for k, v in d.items():
    print('O elemento com  n = {1:2} é o {0}'.format(k, v))
```

```
O elemento com  n =  1 é o H
O elemento com  n =  3 é o Li
O elemento com  n = 11 é o Na
O elemento com  n = 19 é o K
```

``` python
d = {'H':1, 'Li':3, 'Na':11, 'K':19}

for k, v in d.items():
    print('O elemento com  n = {1:<2} é o {0}'.format(k, v))
```

```
O elemento com  n = 1  é o H
O elemento com  n = 3  é o Li
O elemento com  n = 11 é o Na
O elemento com  n = 19 é o K
```

``` python
import math
log2 = math.log(2)

soma = 0.0 # acumula a soma parcial da série

for i in range(1, 21):
    soma = soma + (-1)**(i+1) / i
    dif = abs(soma - log2)
    print(i , soma , dif)
```

```
1 1.0 0.3068528194400547
2 0.5 0.1931471805599453
3 0.8333333333333333 0.14018615277338797
4 0.5833333333333333 0.10981384722661203
5 0.7833333333333332 0.09018615277338793
6 0.6166666666666666 0.0764805138932787
7 0.7595238095238095 0.0663766289638642
8 0.6345238095238095 0.058623371036135796
9 0.7456349206349207 0.052487740074975364
10 0.6456349206349207 0.047512259925024614
11 0.7365440115440116 0.043396830984066326
12 0.6532106782106782 0.039936502349267045
13 0.7301337551337552 0.03698657457380994
14 0.6587051837051838 0.03444199685476146
15 0.7253718503718505 0.03222466981190519
16 0.6628718503718505 0.030275330188094807
17 0.7216953797836152 0.028548199223669912
18 0.6661398242280596 0.027007356331885668
19 0.718771403175428 0.025624222615482695
20 0.6687714031754279 0.02437577738451735
```

``` python
import math
log2 = math.log(2)

soma = 0.0 # acumula a soma parcial da série

print('{:>4} {:^9} {:^9}'.format('n' , 'S' , 'dif'))
for i in range(1, 21):
    soma = soma + (-1)**(i+1) / i
    dif = abs(soma - log2)
    print('{:4d} {:9.6f} {:9.6f}'.format(i,soma,dif))
```

```
n     S        dif   
1  1.000000  0.306853
2  0.500000  0.193147
3  0.833333  0.140186
4  0.583333  0.109814
5  0.783333  0.090186
6  0.616667  0.076481
7  0.759524  0.066377
8  0.634524  0.058623
9  0.745635  0.052488
```

> 10 0.645635 0.047512 11 0.736544 0.043397 12 0.653211 0.039937 13
> 0.730134 0.036987 14 0.658705 0.034442 15 0.725372 0.032225 16
> 0.662872 0.030275 17 0.721695 0.028548 18 0.666140 0.027007 19
> 0.718771 0.025624 20 0.668771 0.024376

Consultar a documentação da [Format Specification
Mini-Language](https://docs.python.org/3/library/string.html#formatspec)
