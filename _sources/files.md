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

# Ficheiros de texto

## Leitura

O modelo mais simples é ler todo o conteúdo de um ficheiro para uma
*string*:

![](./images/fichs.png)

A leitura de um ficheiro segundo este modelo é feito através da função
`.read()`.

Mas o processo é um pouco mais complicado do que o uso simples de uma
função.

O acesso (programático) a um ficheiro existente num computador requer
que num programa se indique que esse acesso vai começar, a *abertura* de
um ficheiro e que o acesso vai terminar, o *fecho* de um ficheiro.

### `.read()`, com `open()` e `close()` explícitos

```{code-cell} ipython3
a = open('eno1.fasta')
seq = a.read()
a.close()

print(type(seq))

print('A sequência, em FASTA é')
print(seq)
```


### `.read()`, dentro do bloco de um comando `with`

Numa versão mais "moderna" podemos abrir e **automaticamente fechar** o
ficheiro é utilizar o comando `with`:

```{code-cell} ipython3
with open('eno1.fasta') as a:
    seq = a.read()

print('A sequência, em FASTA é')
print(seq)
```


O comando `with` faz o ficheiro permanecer *aberto* até ao fim do
"bloco", (também aqui) indicado pelo alinhamento mais à direita de um ou
mais comandos a seguir à linha em que se encontra o `with`. Quando
termina o bloco o ficheiro é fechado sem usar a função `close()`.

Além de `read()`, em que todo o conteúdo de um ficheiro é lido para uma
*string*, existem outras maneiras de ler um ficheiro.

### `.readlines()`

A função `readlines()` lê e separa **as linhas** de um ficheiro para uma
lista:

```{code-cell} ipython3
with open('eno1.fasta') as a:
    seq = a.readlines()

print(seq)
```


O que são os `\n` no fim das *strings*?

**Numa string,** `\n` **indica a mudança de linha**. (Conta como apenas
**1** caractere).

Neste caso eles aparecem porque no ficheiro original há mudanças de
linha.

Muitas vezes, é necessário elimina-los. Para isso podemos usar a função
`.strip()`:

```{code-cell} ipython3
with open('eno1.fasta') as a:
    seq = a.readlines()

seq = [linha.strip() for linha in seq]
print(seq)
```


Ou, de uma forma sucinta, usando uma lista em compreensão:

```{code-cell} ipython3
with open('eno1.fasta') as a:
    seq = [linha.strip() for linha in a.readlines()]
print(seq)
```


Com ficheiros muito grandes, a leitura pelas funções `.read()` e
`.readlines()` pode esgotar a memória de um computador e "congelar" um
programa.

Existe uma terceira maneira de ler um ficheiro (que não traz problemas
com ficheiros grandes):

### Iteração de ficheiros com `for`.

**A iteração de um ficheiro "percorre" as linhas do ficheiro**

```{code-cell} ipython3
with open('eno1.fasta') as a:
    for linha in a:
        linha = linha.strip()
        print('Linha:', linha)
```


Podemos até usar a função `enumerate()` com um ficheiro. São gerados os
pares de valores

`(num linha, linha)`.

```{code-cell} ipython3
with open('eno1.fasta') as a:
    for i, linha in enumerate(a):
        linha = linha.strip()
        print('linha', i, ':', linha)
```


**Problema: ler uma ficheiro FASTA e separar o cabeçalho da sequência em
duas strings (juntando toda a sequência numa só string)**

```{code-cell} ipython3
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
```


Às vezes os ficheiros não têm cabeçalho! É melhor testar se a primeira
linha começa por "&gt;" !

```{code-cell} ipython3
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
```


As linhas em branco podem por vezes causar alguns problemas. Mas é fácil
"ignora-las".

Vamos supor que o ficheiro **gre3.txt** tem o seguinte conteúdo:

------------------------------------------------------------------------

:

    >sp|P38715|GRE3_YEAST NADPH-dependent aldose reductase GRE3 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) GN=GRE3 PE=1 SV=1

    MSSLVTLNNGLKMPLVGLGCWKIDKKVCANQIYEAIKLGYRLFDGACDYGNEKEVGEGIR
    KAISEGLVSRKDIFVVSKLWNNFHHPDHVKLALKKTLSDMGLDYLDLYYIHFPIAFKYVP
    FEEKYPPGFYTGADDEKKGHITEAHVPIIDTYRALEECVDEGLIKSIGVSNFQGSLIQDL
    LRGCRIKPVALQIEHHPYLTQEHLVEFCKLHDIQVVAYSSFGPQSFIEMDLQLAKTTPTL
    FENDVIKKVSQNHPGSTTSQVLLRWATQRGIAVIPKSSKKERLLGNLEIEKKFTLTEQEL
    KDISALNANIRFNDPWTWLDGKFPTFA

------------------------------------------------------------------------

Como separar o cabeçalho da sequência?

```{code-cell} ipython3
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
```


Exemplo: Extração de informação de um ficheiro FASTA múltiplo.
--------------------------------------------------------------

**Problema: extraír os cabeçalhos e as sequências de um ficheiro FASTA
múltiplo. Mostrar o comprimento das proteínas e o número de triptofanos
(W)**

```{code-cell} ipython3
with open('proteins.fasta') as a:
    tudo = a.read()
prots = tudo.split('>')

for p in prots:
    print(len(p))
```


```{code-cell} ipython3
with open('proteins.fasta') as a:
    tudo = a.read()
prots = tudo.split('>')
prots = [p for p in prots if len(p) > 0]

for p in prots:
    print(len(p))
    print(p[:30])
```


```{code-cell} ipython3
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
```


```{code-cell} ipython3
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
```


Escrita
-------

### Função `print()` para ficheiros

Basta abrir o ficheiro em *modo de escrita* usando o argumento `w` na
função `open()`. Depois, modificar a função `print()`, com o argumento
`file`, indicando que o resultado da escrita deve ser *enviado* para o
ficheiro.

```{code-cell} ipython3
with open('exp.txt', 'w') as a:
    print('1, 2, 3, experiência, som, som', file=a)
    for i in range(30):
        print(i, i**0.5, file=a)
```

Aparentemente não aconteceu nada, mas um ficheiro novo foi criado

Vamos ler o ficheiro:

```{code-cell} ipython3
with open('exp.txt') as a:
    print(a.read())
```


### Função `.write()`

Também existe a função `.write()` que funciona como o contrário de
`.read()`:

```{code-cell} ipython3
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
```


**Problema: ler uma ficheiro com dados numéricos e converter o ponto
decimal em vírgula decimal**

No ficheiro `exp.txt`, recentemente criado, podemos, de uma form
sucinta, passar os `.` a `,` ?

```{code-cell} ipython3
with open('exp.txt') as a:
    tudo = a.read().replace('.', ',')

with open('exp.txt', 'w') as a:
    a.write(tudo)

with open('exp.txt') as a:
    print(a.read())
```


## Módulo `requests`

```{code-cell} ipython3
:tags: [output_scroll]
import requests

url = 'https://www.uniprot.org/uniprot/?query=proteome:UP000002407%20reviewed:yes&format=list'

data = requests.get(url).text

print(data)
```


```{code-cell} ipython3
import requests
r = requests.get('http://www.uniprot.org/uniprot/P00924.fasta')
print(r.text)
```


```{code-cell} ipython3
import requests
r = requests.get('http://www.uniprot.org/uniprot/P00924.fasta')
linhas = r.text.split('\n')

if linhas[0].startswith('>'):
    cab = linhas[0]
    seq = ''.join(linhas[1:])
else:
    cab = ""
    seq = ''.join(linhas)

print("cabeçalho: ", cab)
print("sequência:")
print(seq)
```

```{code-cell} ipython3
:tags: [output_scroll]
import requests
r = requests.get('http://www.uniprot.org/uniprot/P00924.txt')
print(r.text)
```


```{admonition} Problema
:class: question

-   obter a informação relativa à proteína P00924
-   filtar a linha começada por **SQ**
-   mostar o numero de aminoácidos e a massa molecular

```

A informação relativa ao formato desta linha (embora seja evidente
olhando para um exemplo) está descrita na [documentação da
UniProt](http://web.expasy.org/docs/userman.html#SQ_line)

A linha tem o formato

`SQ   SEQUENCE XXXX AA; XXXXX MW; XXXXXXXXXXXXXXXX CRC64;`

```{code-cell} ipython3
import requests
info = requests.get('http://www.uniprot.org/uniprot/P00924.txt').text

linhas = info.split('\n')

sq = ''
for i in linhas:
    if i.startswith('SQ'):
        sq = i

print('linha SQ:')
print(sq)

# SQ   SEQUENCE XXXX AA; XXXXX MW; XXXXXXXXXXXXXXXX CRC64;
partes = sq.split()
print(partes[2], 'aminoácidos')
print(partes[4], 'Da')
```


Na [documentação da
UniProt](http://web.expasy.org/docs/userman.html#FT_keys), realtiva às
linhas começadas por `FT` pode-se ler...

    INIT_MET - Initiator methionine.

    This feature key is associated with a '1' value in the 'FROM' and 'TO' fields to indicate that the initiator methionine has been cleaved off:


        FT   INIT_MET      1      1       Removed.

    It is not used when the initiator methionine is not cleaved off

```{admonition} Problema
:class: question

Para as seguintes proteínas,

`Q96UH7, Q8J0N6, Q9URB4, Q9C2U0, P36580, P14540`

gerar uma tabela com

`AC       AA         MW       init M cleaved`
```
