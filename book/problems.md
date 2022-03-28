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

# Exercícios de treino

## Exercícios Numéricos, usando comandos *for*

**1** - Dada a seguinte lista de números (da famosa sequência de Fibonacci),
calcule a percentagem de números pares

```{code-block} ipython3
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]
```

Note que no canto superior direito tem um botão para fazer *copy*.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

pares = []
for n in fibs:
    if n % 2 == 0:
        pares.append(n)

print('percentagem de pares:')
pp = 100 * len(pares) / len(fibs)
print(pp)
```

---

**2** - Usando a mesma lista de números do problema 1, crie uma
lista só com aqueles números que são quadrados perfeitos, isto é, aqueles
números $n$ para os quais existe uma raíz $r$ **inteira** $n = r . r$.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

quadrados = []
for n in fibs:
    raíz = n**0.5
    if raíz == int(raíz):
        quadrados.append(n)

print('quadrados perfeitos:')
print(quadrados)
```
        
---

3 - Usando a mesma lista de números do problema 1, crie uma
lista só com aqueles números que começam por 3. Sugestão: use a função `str()` para 
transformar o número numa *string* e depois teste se começa por `"3"`.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

começapor3 = []
for n in fibs:
    nstr = str(n)
    if nstr.startswith('3'):
        começapor3.append(n)

print('começam por 3:')
print(começapor3)
```

---

4 - Usando a mesma lista de números do problema 1, crie uma lista com os quocientes
entre dois números consecutivos.

Mostre essa lista numa coluna de números e veja como estes quocientes rapidamente convergem para
um número muito especial e conhecido. Procure que número é este (cujo valôr é $(1 + \sqrt{}5) / 2$).
Cuidado: não calcule o quociente entre os dois primeiros, porque dá divisão por zero e tenha
cuidado para não exceder o fim dos números (não existe `fibs[len(fibs)]`)

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

quocientes = []
for i in range (1, len(fibs)-1):
    q = fibs[i+1] / fibs[i]
    quocientes.append(q)

for q in quocientes:
    print(q)
```

## Exercícios sobre Listas em compreensão

5 - Repita o exercício 4, mas criando a lista de quocientes consecutivos como uma lista em compreensão.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

quocientes = [fibs[i+1] / fibs[i] for  i in range (1, len(fibs) - 1)]

for q in quocientes:
    print(q)
```

---

6 - Repita o exercício 3, mas criando a lista de números começados por 3 como uma lista em compreensão.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

começa_por3 = [n for n in fibs if str(n).startswith('3')]

print('começam por 3:')
print(começa_por3)
```

---

7 - Dada a seguinte sequência e uma *string* dos códigos dos aminoácidos com
carga, crie uma lista com todas os aminoácidos com carga na sequência, usando uma lista em compreensão

```{code-block} python3
seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

charged = 'KHRDE'
```

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

charged = 'KHRDE'

all_charged = [a for a in seq if a in charged]
print(all_charged)
```   

---

8 - Usando a mesma sequência do exercício 7, crie uma lista com as posições (números inteiros)
das serinas `S`, através de uma lista em compreensão.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

posS = [i for i, a in enumerate(seq) if a == 'S']
print(posS)
```

## Exercícios sobre slices, zip, split

9 - (difícil) Repita o exercício 5 (quocientes de 2 números consecutivos), mas obtendo estes números
consecutivos `n` e `m` pela função `zip()` para unir duas *slices* da lista de números `fibs`.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
        39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,
        1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

quocientes = [m / n for  m, n in zip(fibs[2:], fibs[1:])]

for q in quocientes:
    print(q)
```

---

10 - (difícil) Dada a mesma sequência do exercício 7, crie um dicionário, através de um dicionário
em compreensão, cujos valores são as letras `"GV"` e as chaves são as posições em que `GV`ocorre na
sequência. Tipo

```{code-block} python3
{147: 'GV', 170: 'GV', .... }
```

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

GV = {i: seq[i:i+2] for i in range(0, len(seq) - 1) if seq[i:i+2] == 'GV'}
print(GV)
```

---

11 - A sequência do exercício 7 é dada numa *string* que ocupa várias linhas (tem `"\n"` no meio).
Transforme essa *string* numa *string* sem mudanças de linha

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

seq = seq.splitlines()
seq = ''.join(seq)
# ou seq = seq.replace('\n', '')
print(seq)
```

## Exercícios de criação de funções (com *def*)

12 - Escreva uma função que, ao ser aplicada a um número inteiro, dá `True` ou `False` consoante
o número começa ou não por 3. Chame à função `startswith3`.

Experimente aplicar a função a vários números.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
def startswith3(n):
    nstr = str(n)
    return nstr.startswith('3')

print(startswith3(324))
print(startswith3(1024))
```

---

13 - Escreva uma função que, ao ser aplicada a um número inteiro, dá o número de dígitos desse número. Chame à função `ndigits`.

Experimente aplicar a função a vários números.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
def ndigits(n):
    nstr = str(n)
    return len(nstr)

print(ndigits(7))
print(ndigits(3278344))
print(ndigits(10256234774))
```

---

14 - Escreva uma função que, ao ser aplicada a uma *string* com uma sequência, dá como
resultado as últimas 50 letras . Chame à função `last50`.

Experimente aplicar a função à sequência do problema 7. Cuidado: livre-se das mudanças de linha (`\n`)

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
def last50(seq):
    seq = seq.replace('\n', '')
    return seq[-50:]

seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

print(last50(seq))
```

---

15 - Escreva uma função que, ao ser aplicada a uma *string* com uma sequência, dá como
resultado a mesma *string* sem os aminoácidos com carga . Chame à função `remove_charged`.

Experimente aplicar a função à sequência do problema 7.

**Solução**

```{code-cell} ipython3
:tags: ["hide-cell"]
def remove_charged(seq):
    seq = seq.replace('\n', '')
    nocharged = [a for a in seq if a not in 'KHRDE']
    return ''.join(nocharged)

seq = """
MVRLGPKKPPARKGSMADVPANLMEQIHGLETLFTVSSEKMRSIVKHFISELDKGLSKKG
GNIPMIPGWVVEYPTGKETGDFLALDLGGTNLRVVLVKLGGNHDFDTTQNKYRLPDHLRT
GTSEQLWSFIAKCLKEFVDEWYPDGVSEPLPLGFTFSYPASQKKINSGVLQRWTKGFDIE
GVEGHDVVPMLQEQIEKLNIPINVVALINDTTGTLVASLYTDPQTKMGIIIGTGVNGAYY
DVVSGIEKLEGLLPEDIGPDSPMAINCEYGSFDNEHLVLPRTKYDVIIDEESPRPGQQAF
EKMTSGYYLGEIMRLVLLDLYDSGFIFKDQDISKLKEAYVMDTSYPSKIEDDPFENLEDT
DDLFKTNLNIETTVVERKLIRKLAELVGTRAARLTVCGVSAICDKRGYKTAHIAADGSVF
NRYPGYKEKAAQALKDIYNWDVEKMEDHPIQLVAAEDGSGVGAAIIACLTQKRLAAGKSV
GIKGE"""

print(remove_charged(seq))
```

