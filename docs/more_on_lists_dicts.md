# Listas e dicionários

## Revisão sobre coleções

No capítulo anterior, definiu-se o conceito de coleção e mostrou-se 4
dos tipos fundamentais de coleções na linguagem Python: as listas, as
*strings*, os dicionários e os conjuntos.

A função `len()`, para calcular o número de elementos de uma coleção, e o
operador `in`, para verificar se um elemento está contido numa coleção, podem
ser usados em qualquer coleção.

!!! note "Nota"
    Recorde que o operador `in`, ao ser usado com dicionários, verifica
    se um elemento está entre as **chaves** do dicionário.

    Recorde que o operador `in`, ao sr usado com *strings*, pode verificar se uma *substrings*
    está presente e não apenas uma letra:

    ```python3
    if 'AUG' in 'UCCAUGGCCAA':
        print('AUG existe na sequência')
    ```

Outra característica em comum a todas as coleções é a possibilidade de serem "iteradas"
usando o comando `for`.

!!! info "Nota"
    Recorde que, usando o comando `for`:

    - Passamos por todos os **elementos** de uma *lista* (pela sua ordem)
    - Passamos pelas **chaves** de um *dicionário*.
    - Passamos pelos **caracteres** de uma *string* (pela sua ordem)
    - Passamos pelos **elementos** de um *conjunto*.

Algo trivial é comum a todas as coleções: a possibilidade de criarmos "coleções vazias"

## Coleções vazias

Coleções vazias são simplesmente coleções sem nenhum elemento. Podemos criá-las explicitamente
desta forma:

<div class="python_box">
``` python3
# lista vazia
a = []

# string vazia
s = ''

# dicionário vazio
d = {}

# conjunto vazio
c = set()

print(a)
print(s)
print(d)
print(c)
```
</div>

```
[]

{}
set()
```

!!! note "Nota"
    O que aconteceu à *string* vazia?

    A função `print()` tira as aspas quando apresenta *strings*, logo, aparentemente não
    apareceu a *string* (embora haja uma mudança de linha)

    Porque temos de usar `set()` para o conjunto vazio?

    Porque `{}` já está reservado para os dicionários vazios. Mas, recorde-se que
    para definir explicitamente um conjunto usamos `{}` para delimitar o conjunto:

    ```python3
    c = {6, 9, 'A', 'T'}
    ```

    Mas não usamos pares chave:valôr entre `{}`. Isso seria um dicionário.

A utilidade destas versões vazias é clara: muitas vezes num programa precisamos de começar por
com um coleção vazia para depois, ao longo do programa, ir acrescentando elementos.

## Listas

Neste capítulo mostra-se algumas **funções** que são específicas de cada
coleção, começando pelas **listas** e **dicionários**. As funções características
das *strings* serão o tema do próximo capítulo.

Vejamos algumas funções que são **específicas das listas**.

A referência oficial destas funções pode ser consultada na [documentação da
linguagem Python.](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

#### Acrescentar elementos: `.append()`, `.insert()`

As funções `.append()`, `.insert()` acrescentam um elemento a uma lista. `.append()` acrescenta **no fim** da lista, ``.insert()` acrescenta numa determinada **posição**:

<div class="python_box">
``` python3
a = [1, 2, 3, 4]
print(a)

a.append(10)

print('\ndepois de append(10):', a)

a.insert(1, 20)

print('\ndepois de insert(1, 20):', a)
```
</div>

```
[1, 2, 3, 4]

depois de append(10): [1, 2, 3, 4, 10]

depois de insert(1, 20): [1, 20, 2, 3, 4, 10]
```

#### Acrescentar uma lista completa: `.extend()`

A função `extend()` permite acrescentar **ao fim** da lista uma outra lista completa.

A diferença (subtil) em relação à função `append()` é que a função `append()` acrescenta apenas **um** elemento novo.

<div class="python_box">
``` python3
a = [1, 2, 3, 4]
print(a)

novos = [11, 12, 13, 14]
a.extend(novos)

print('\ndepois de extend([11, 12, 13, 14]):')
print(a)
```
</div>

```
[1, 2, 3, 4]

depois de extend([11, 12, 13, 14]):
[1, 2, 3, 4, 11, 12, 13, 14]
```

#### Retirar elementos: `.remove()`, `.clear()`

`.remove(elem)` remove o elemento *elem* e `.clear()` remove todos os elementos.

A função `.remove()`, no entanto, só remove a "primeira ocorrência" do elemento
(considerando a ordem dos elementos na lista).

<div class="python_box">
``` python3
a = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(a)

a.remove(3)

print('\ndepois de remove(3):')
print(a)

a.clear()

print('\ndepois de clear():')
print(a)
```
</div>

```
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

depois de remove(3):
[1, 2, 4, 1, 2, 3, 4, 1, 2, 3, 4]

depois de clear():
[]
```
Repare-se que `.remove(3)` só removeu a primeira ocorrência de 3 na lista. Ficou um 3 na penúltima posição.

#### Contar elementos: `.count()`

A função `.count(elem)` conta o número de vezes que um elemento ocorre na lista (todas as ocorrências).

Esta função não modifica a lista e devolve um resultado, um número inteiro.

<div class="python_box">
``` python3
a = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(a)

print('\nresultado de count(1)')
print(a.count(1))
```
</div>

```
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

resultado de count(1)
3
```

!!! example "Problema"
    Dada a sequência de uma proteína, quantas lisinas (K) e leucinas (L) existem na sequência?

<div class="python_box">
``` python3
seq = 'ADKHLILTAVGGCWFHVAFWEVEKAGAHKWE'

seqlista = list(seq)

nK = seqlista.count('K')
nL = seqlista.count('L')

print(f'Existem {nK} lisinas e {nL} leucinas na sequência')
print(seq)
```
</div>

```
Existem 3 lisinas e 2 leucinas na sequência
ADKHLILTAVGGCWFHVAFWEVEKAGAHKWE
```

Relembremos que a função `list()` transforma a *string* numa lista, com as letras como
elementos da lista.

!!! important "Nota importante"
    A função `.count()` também funciona com *strings*.

Como a função `.count()` também funciona com *strings*, o programa anterior pode ser simplificado,
aplicando esta função diretamente à *string*:

<div class="python_box">
``` python3
seq = 'ADKHLILTAVGGCWFHVAFWEVEKAGAHKWE'

nK = seq.count('K')
nL = seq.count('L')

print(f'Existem {nK} lisinas e {nL} leucinas na sequência')
print(seq)
```
</div>

```
Existem 3 lisinas e 2 leucinas na sequência
ADKHLILTAVGGCWFHVAFWEVEKAGAHKWE
```


#### Exemplos de `.append()` para gerar listas novas

Recordar que as listas podem ser "iteradas" com o comando `for`.

A combinação da iteração de listas com a função `.append()` começando
por uma  **lista vazia** e acrescentando elemento a elemento, é uma maneira muito conveniente
de gerar listas novas durante a execução de um programa.

!!! example "Problema"
    Gerar uma lista com os 40 primeiros quadrados perfeitos $\{i^2: i=1, 2, 3,...,40\}$ .

Estratégia: passar por todos os números inteiros até ao 40, calcular o seu
quadrado e acrescentar no final de uma lista com `append()`. No início a lista tem
de existir e estar vazia.

<div class="python_box">
``` python3
a = []
for i in range(1, 41):
    a.append(i**2)

print(a)
```
</div>

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600]
```
Outro exemplo:

!!! example "Problema"
    Gerar uma lista com os 40 primeiros quadrados perfeitos
    $\{i^2: i=1, 2, 3, ... , 40\}$, que **estejam entre 400 e 800**.

Podemos combinar `.append()` com `for` e `if`:

<div class="python_box">
``` python3
a = []
for i in range(1, 41):
    q = i**2
    if q >= 400 and q <= 800:
        a.append(q)

print(a)
```
</div>


```
[400, 441, 484, 529, 576, 625, 676, 729, 784]
```


!!! example "Problema"
    Somar os 10 primeiros números ímpares
    $\sum\limits_{i=0}^9 2i+1$

Estratégia: construir uma lista com os números ímpares. Somar com a função `sum()`.

<div class="python_box">
``` python3
ímpares = []
for i in range(10):
    ímpares.append(2*i + 1)
print(ímpares)

resultado = sum(ímpares)

print('A soma dos 10 primeiros ímpares é', resultado)
print('Verificação:')
print('Pela soma de prog. aritm.',(1+19)/2*10)
```
</div>

```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
A soma dos 10 primeiros ímpares é 100
Verificação:
Pela soma de prog. aritm. 100.0
```

### Exemplos de indexação de listas.

As listas têm uma **numeração implícita, (a contar do zero)**, e podemos
**indexar** uma lista usando `lista[posição]`. Obtemos o elemento que está
numa posição.

Mostrando, com um comentário as posições implícitas dos elementos:

<div class="python_box">
``` python3
enzimas = ['HK', 'G6PDH', 'TPI', 'Ald', 'PFK', 'PK']
#           0       1       2      3      4      5   len()

print(enzimas[0])
print(enzimas[3])
# para obter o último elemento...
print(enzimas[len(enzimas) -1])
```
</div>

```
HK
Ald
PK
```

As listas têm também uma **numeração implícita com números negativos**:
o último elemento é -1, o penúltimo -2 e assim sucessivamente.

<div class="python_box">
``` python3
enzimas = ['HK', 'G6PDH', 'TPI', 'Ald', 'PFK', 'PK']
#                          -4     -3     -2     -1

print(enzimas[-4])
print(enzimas[-6])
print(enzimas[-1])
```
</div>

```
TPI
HK
PK
```

!!! tip "Dica"
    para obter o último elemento de uma lista podemos simplesmente indexar com -1
    ```python3
    último = a[-1]
    ```

A indexação permite também **modificar** um elemento que está numa
posição, usando `=` como se fossemos atribuír um nome.

No seguinte exemplo modificamos o elemento que está na posição 2:

<div class="python_box">
``` python3
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
print(a)

a[2] = 4 * 2**10 + a[-1]
print(a)
```
</div>

```
[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
[1, 1, 4100, 2, 2, 2, 3, 3, 3, 4, 4, 4]
```

Podemos aplicar um comando `for` não diretamente aos elementos de uma lista
mas sim aos números inteiros , geralmente gerados com `range()`, que podem funcionar como posições para indexar a lista.

Vejamos estas duas alternativas:

<div class="python_box">
``` python3
# Iteração direta dos elementos da lista

a = [1, 2, 3, 2, 1]

for e in a:
    print(e)
```
</div>

```
1
2
3
2
1
```

Esta é a maneira simples e direta de aplicar comandos (neste caso `print()`) a todos os
elementos da lista.

Mas o mesmo pode ser conseguido, de uma forma indireta, passando pelas posições, não pelos próprios elementos, e usando indexação para obter os elementos:

<div class="python_box">
``` python3
# iteração através das posições dos elementos
a = [1, 2, 3, 2, 1]

for i in range(len(a)):
    print(a[i])
```
</div>

```
1
2
3
2
1
```
Claro que a forma indireta é mais complicada e são raras as ocasiões onde teremos de a usar.

No entanto, um exemplo:

!!! example "Problema"
    Calcular as diferenças sucessivas entre os elementos de uma
    lista, pondo o resultado numa lista

<div class="python_box">
``` python3
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 7]

difs = []
for i in range(1, len(a)):
    d = a[i] - a[i-1]
    difs.append(d)

print('Lista')
print(a)
print('Diferenças sucessivas')
print(difs)
```
</div>

```
Lista
[1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 7]
Diferenças sucessivas
[0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 2]
```

Neste exemplo tivemos de usar posições, os índices dos elementos, porque
as diferenças sucessivas têm de ser calculadas por $d_i = a_i - a_{i-1}$ ou,
em Python,

```python3
d = a[i] - a[i-1]
```

Repare-se que a `range()` tem de começar em 1, uma vez que, se começasse em 0, a primeira
diferença calculada seria `d = a[0] - a[-1]` que não faria sentido, uma vez que `a[-1]`
representa o último elemento da lista.

Voltaremos a este exemplo mais tarde.

!!! example "Exemplo"
    Mostrar que as diferenças sucessivas entre os quadrados
    perfeitos, são os números ímpares (usar os 20 primeiros)

<div class="python_box">
``` python3
#calcular os quadrados perfeitos
quads = []
for i in range(20):
    quads.append(i**2)

#calcular as diferenças sucessivas
difs = []
for i in range(1, len(quads)):
    d = quads[i] - quads[i-1]
    difs.append(d)

print('quadrados perfeitos', quads)
print('diferenças sucessivas', difs)
```
</div>

```
quadrados perfeitos [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
diferenças sucessivas [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
```

A propriedade matemática anterior foi usada por Galileu no estudo da
queda livre dos corpos.

![](images/galileu.jpg)

As distâncias sucessivas percorridas durante a queda para a mesma
unidade de tempo estão entre si como a sucessão dos números ímpares, o
que implica que a distância acumulada cresce segundo o quadrado do tempo
decorrido: o movimento de queda livre é uniformemente acelerado.

Uma pequena nota final sobre a utilização de indexação para passar por
todos os elementos de uma lista:

!!! note "Nota"
    A maneira "indireta" de percorrer uma lista com `for`

    ```python3
    for i in range(len(lista)):
        "operações com lista[i]"
    ```

    é muito típica de outras linguagens de programação. Não na linguagem Python, onde é encorajado o uso da forma direta:

    ```python3
    for e in lista:
        "operações com e"
    ```

    Na linguagem Python é quase sempre possível reescrever a forma indireta na forma direta.
    
    Quando os índices dos elementos são mesmo necessários a função `enumerate()`,
    vista no capítulo anterior, pode muitas vezes substituír a indexação.

    Num dos próximos capítulos abordaremos ainda o uso de módulos de computação científica, em
    particular os módulos `numpy` e `pandas`, em que a iteração é substituída por operações "vetoriais", que, efetivamente, prescindem o uso de comandos `for`, quer na sua forma direta quer na sua forma indireta.

### Listas em compreensão

Existe uma outra forma muito conveniente e compacta de construír listas num programa,
as **listas em compreensão**.

Esta forma assemelha-se à notação matemática de descrever um conjunto através do seu
"termo geral".

A ideia é obter uma lista pela transformação de `range()` ou uma outra lista de partida
indicando uma expressão para essa transformação. Essa expressão indica a operação a efectuar a cada elemento da `range()` ou da lista de partida.

Um exemplo mostra a notação a usar.

!!! example "Problema"
    Obter uma lista com numeros ímpares (os primeiros 10)

<div class="python_box">
``` python3
ímpares = [2*i+1 for i in range(10)]

print(ímpares)
```
</div>

```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

Em resumo, entre`[]` indica-se, em primeiro lugar, um "termo geral", neste caso `2*i+1`. De seguida e um comando `for` para passar pelos elementos do `range()` ou da lista de partida. À frente do `for`, o nome `i` tem o mesmo papel que nos comandos `for` "normais", é o nome a dar a cada elemento de partida, um a um.

Tudo está entre `[]`, para indicar que estamos a construír uma lista.

Esta maneira pode também ser vista como uma substituição da construção de listas novas com `append()`,
começando a partir de uma lista vazia. A lista em compreensão que acabámos de ver é equivalente
a fazer o seguinte:

<div class="python_box">
``` python3
ímpares = []
for i in range(10):
    ímpares.append(2 * i + 1)
```
</div>

Um outro exemplo:

!!! example "Problema"
    Obter uma lista com os quadrados perfeitos entre 400 e 800. 

Este exemplo mostra que podemos, numa lista em compreensão, impôr condições (com `if`) aos valores
da lista, "filtrando" certos elementos.

<div class="python_box">
``` python3
quads = [i**2 for i in range(30) if i**2 > 400 and i**2 < 800]

print(quads)
```
</div>

```
[441, 484, 529, 576, 625, 676, 729, 784]
```

Revisitando um exemplo anterior, mas agora usando listas em compreensão:

!!! example "Problema"
    Obter uma lista com as diferenças sucessivas entre quadrados perfeitos, para mostrar que são os números ímpares

<div class="python_box">
``` python3
q = [i**2 for i in range(20)]
difs = [q[i] - q[i-1] for i in range(1, len(q))]

print('Quadrados: ', q)
print('\nDiferenças:', difs)
```
</div>

```
Quadrados:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

Diferenças: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
```

Note-se a maneira muito compacta de resolver o problema. Duas lista em compreensão foram suficientes.

Note-se a analogia com a notação matemática de indicar um conjunto "em compreensão"

<div class="python_box">
``` python3
q = [i**2 for i in range(20)]
```
</div>

e

$q = \{i^2 : i=0, 1, 2, ... ,20 \}$

Mais um exemplo. A função `.remove()` retira a primeira ocorrência de um 
elemento numa lista. Qual a maneira simples de retirar todas as ocorrências
desse elemento de uma só vez?

Usando uma lista em compreensão.

!!! example "Exemplo:"
    Retirar todas as ocorrências de um elemento de uma lista

<div class="python_box">
``` python3
# Remover todas as ocorrências de "Bad"
a = ['Good','Nice','OK','Bad','Cool','Bad','OK']
a_clean = [x for x in a if x != 'Bad']

print(a)
print(a_clean)
```
</div>

```
['Good', 'Nice', 'OK', 'Bad', 'Cool', 'Bad', 'OK']
['Good', 'Nice', 'OK', 'Cool', 'OK']
```

Neste exemplo a condição `if` é muito mais importante do que o "termo geral", daí
a estranha construção `[x for x in ...]`. Se a lista em compreensão fosse apenas
`a_clean = [x for x in a]` então copiaríamos a lista `a` para a lista `a_clean` sem filtrar os elementos. O `if` está a fazer o trabalho de filtrar os elementos `"Bad"`

!!! example "Exemplo:"
    Problema: retirar todas as ocorrências dos elemento pertencentes a uma "lista negra"

<div class="python_box">
``` python3
black_list = ['Bad', 'So so']
a = ['Good','So so','OK','Bad','Cool','Bad','OK']
a_clean = [x for x in a if x not in black_list]

print(a)
print(a_clean)
```
</div>

```
['Good', 'So so', 'OK', 'Bad', 'Cool', 'Bad', 'OK']
['Good', 'OK', 'Cool', 'OK']
```

!!! example "Exemplo:"
    Obter uma lista de numeros até 300 que sejam múltiplos de 3 e de 7

Como testar se um número $n$ é múltiplo de outro $p$? basta que o resto da divisão de
$n$ por $p$ seja 0. O resto da divisão pode ser obtido na linguagem Python pelo
operador `%`:

<div class="python_box">
``` python3
mult_3_7 = [x for x in range(301) if x%7==0 and x%3==0]

print(mult_3_7)
```
</div>

```
[0, 21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294]
```

Leitura interessante:

[Comprehensions in Python the Jedi
way](https://gist.github.com/bearfrieze/a746c6f12d8bada03589)

### Mais algumas funções de listas

#### `.pop()`, `.reverse()`, `.sort()`

As funções `.pop()`, `.reverse()`, `.sort()` também **modificam** uma lista, tal como, por exemplo, a função `.append()`.

`.reverse()` coloca os elementos da lista por uma ordem contrária aquela que é dada.

`.sort()` ordena os elemento da lista por ordem alfabética ou por ordem numérica.


<div class="python_box">
``` python3
a = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
print('lista original')
print(a)

a.reverse()
print('\nDepois de a.reverse()')
print(a)

a.sort()
print('\nDepois de a.sort()')
print(a)
```
</div>

```
lista original
['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

Depois de a.reverse()
['dom', 'sab', 'sex', 'qui', 'qua', 'ter', 'seg']

Depois de a.sort()
['dom', 'qua', 'qui', 'sab', 'seg', 'sex', 'ter']
```

`.pop()` é, praticamente, o contrário de `append()`, serve para retirar o **último** elemento de uma lista.
No entanto, se se usar com uma posição, é o elemento nessa posição que é retirado. Em qualquer caso, a função
devolve o valôr retirado, que pode ser usado mais tarde, se for necessário.

<div class="python_box">
``` python3
a = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
print('lista original')
print(a)

a.pop()
print('Depois de a.pop()')
print(a)
x = a.pop(2)
print('\nDepois de a.pop(2)   ')
print(a)
print('O valor retirado foi', x)
```
</div>

```
lista original
['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
Depois de a.pop()
['seg', 'ter', 'qua', 'qui', 'sex', 'sab']

Depois de a.pop(2)   
['seg', 'ter', 'qui', 'sex', 'sab']
O valor retirado foi qua
```

## Dicionários

Os dicionários são associações (não ordenadas) entre **chaves** e
**valores**.

!!! important "Nota"
    Num dicionário **cada chave é única**. Não pode haver chaves repetidas.

### Acrescentar e modificar elementos (chave:valor)

!!! info "Importante"
    A maneira de obter, inserir e modificar elementos de um dicionário é através 
    das suas chaves, usando **indexação**

De certa forma é mais fácil inserir e modificar elementos (pares chave: valor) num
dicionário do que numa lista. Basta usar indexação pela chave. O melhor será com um exemplo.

<div class="python_box">
``` python3
d = {'H':1, 'Li':3, 'Na':11, 'K':19}
print(d)

# inserir um elemento novo (par chave:valor)

d['O'] = 16
print(d)

# modificar um elemento já existente

d['O'] = 18
print(d)
```
</div>

```
{'H': 1, 'Li': 3, 'Na': 11, 'K': 19}
{'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 16}
{'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
```
Não esquecer que o operador `in` procura se existe ou não uma **chave**

<div class="python_box">
``` python3
d = {'H':1, 'Li':3, 'Na':11, 'K':19}

if 'N' in d:
    print('Existe info sobre o azoto')
else:
    print('Não existe info sobre o azoto')
```
</div>

```
Não existe info sobre o azoto
```


Não esquecer que o comando `for` aplicado a dicionários passa pelas **chaves**.

Um exemplo, com uma mini tabela periódica:

<div class="python_box">
``` python3
# elementos cujo símbolo tem 2 letras
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

for k in tperiodica:
    if len(k) == 2:
        print(k)
```
</div>

```
Li
Na
```

Mas, percorrendo as chaves, podemos obter os valores correspondentes por indexação:

<div class="python_box">
``` python3
# elementos com o número atómico superior a 10
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

for k in tperiodica:
    if tperiodica[k] > 10:
        print(k, '--->', tperiodica[k])
```
</div>

```
Na ---> 11
K ---> 19
O ---> 18
```

### `.update()`

`.update()` faz várias modificações de uma só vez: modifica um dicionário
com outro dicionário. Se uma chave já existir, o seu valor é modificado. Se não existir,
é inserido um novo elemento. Vejamos um exemplo:

<div class="python_box">
``` python3
d = {'a': 1, 'c': 3, 'b': 2}
print('original')
print(d)

novos = {'p': 10, 'q': 15, 'c': 20}
d.update(novos)

print('após update')
print(d)
```
</div>

```
original
{'a': 1, 'c': 3, 'b': 2}
após update
{'a': 1, 'c': 20, 'b': 2, 'p': 10, 'q': 15}
```

### `.clear()`

Uma função óbvia. (Note-se que já a vimos em listas).

<div class="python_box">
``` python3
d = {'a': 1, 'c': 3, 'b': 2}
print(d)

d.clear()
print(d)
```
</div>

```
{'a': 1, 'c': 3, 'b': 2}
{}
```

### Iterações usando `.values()`,`.items()`, `.keys()`

Apesar da iteração de dicionários ser feita pelas chaves `k` quando escrevemos

    for k in dicionário:

podemos usar as funções `.values()` e `.items()` para iterar por um dicionário de outra forma.

A função `.values()` faz com que a iteração seja pelos valores e não pelas chaves:

<div class="python_box">
``` python3
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

for v in tperiodica.values():
    print(v)
```
</div>

```
1
3
11
19
18
```

Mais interessante ainda é a função `.items()`. O melhor será ver um exemplo, usando sempre a mini tabela periódica:

<div class="python_box">
``` python3
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

for x in tperiodica.items():
    print(x)
```
</div>

```
('H', 1)
('Li', 3)
('Na', 11)
('K', 19)
('O', 18)
```
Isto é, o efeito da função `.items()` é fazer com que a iteração passe por **pares** do tipo *(chave, valor)*.

Quando usamos `.items()` podemos dar dois nomes à frente do comando `for` (e antes do `in`).

O resultado é semelhante ao que foi visto no capítulo anterior com a função `enumerate()`:
os pares resultantes de `.items()` são desdobrados pelos dois nomes, o que significa que 
o primeiro nome é atribuído a cada chave e o segundo nome atribuído a cada valor durante a
iteração do dicionário.

Vejamos com exemplo, repare-se no uso de dois nomes, `e` e `n`.

<div class="python_box">
``` python3
# elementos com o número atómico superior a 10
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

for e, n in tperiodica.items():
    if n > 10:
        print (e, '--->', n)
```
</div>

```
Na ---> 11
K ---> 19
O ---> 18
```

A última versão deste programa (sem `.items()`) usava indexação para obter os valores:

<div class="python_box">
``` python3
# elementos com o número atómico superior a 10
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

for k in tperiodica:
    if tperiodica[k] > 10:
        print(k, '--->', tperiodica[k])
```
</div>

```
Na ---> 11
K ---> 19
O ---> 18
```

!!! example "Problema"
    Virar um dicionário "do avesso", isto é, criar um novo dicionário
    em que as chaves "trocam" com os respetivos valores.

    Nota: é possível repetir valores num dicionário, mas não as chaves. O que significa
    que num problema destes podem-se "perder" chaves quando se trocam as chaves por valores.

Tentando resolver este problema usando indexação:

<div class="python_box">
``` python3
# Trocar os elementos da T.P. pelos n. atómicos
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

num2simbs = {}

for k in tperiodica:
    num2simbs[tperiodica[k]] = k
print(tperiodica)
print(num2simbs)
```
</div>

```
{'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
{1: 'H', 3: 'Li', 11: 'Na', 19: 'K', 18: 'O'}
```

Confuso? Um pouco.

Usando `.items()` tudo fica mais claro:

<div class="python_box">
``` python3
# Trocar os elementos da T.P. pelos n. atómicos
tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

num2simbs = {}

for elem, na in tperiodica.items():
    num2simbs[na] = elem
print(tperiodica)
print(num2simbs)
```
</div>

```
{'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
{1: 'H', 3: 'Li', 11: 'Na', 19: 'K', 18: 'O'}
```

!!! example "Problema"
    Contar os diferentes **valores** de um dicionário.

    Mais uma vez: as chaves são únicas, os valores não. Por isso
    faz sentido conta-los

<div class="python_box">
``` python3
fellowship = {'Aragorn':'Humano',
              'Frodo':'Hobbit',
              'Sam':'Hobbit',
              'Boromir':'Humano',
              'Merry':'Hobbit',
              'Took':'Hobbit',
              'Gandalf':'Feiticeiro',
              'Gimli':'Anão',
              'Legolas':'Elfo'}

# resultado das contagens num dicionário
# que associa espécie: nº personagens dessa espécie

contagens = {}

for espécie in fellowship.values():
    if espécie in contagens:
        contagens[espécie] = contagens[espécie] + 1
    else:
        contagens[espécie] = 1

# apresentação das contagens
for e, c in contagens.items():
    print(e, c)
```
</div>

```
Humano 2
Hobbit 4
Feiticeiro 1
Anão 1
Elfo 1
```

Confuso? Talvez o uso de um `if...else` não seja claro.

O dicionário `contagens`, inicialmente vazio, tem como objetivo conter as contagens
na forma de pares *espécie:contagem*.

A cada iteração dos **valores** do dicionário `fellowship` é obtida a "espécie" que terá de contar mais um 
para essa espécie no dicionário `contagens`. Mas só pode ser adicionado `+1` à chave correspondente a essa espécie
se ela já existir no dicionário. Se não existir, será a primeira contagem e terá o valor 1 pela primeira vez.
O teste `if espécie in contagens:` trata deste problema de averiguar se podemos somar ou não a um elemento
que pode existir ou não.

A solução deste problema inclui

- a iteração dos valores de um dicionário com `.values()`
- um teste de inclusão num dicionário com  `in`
- a atribuição de valores novos ou a modificação de um já existente com **indexação**
- a iteração das cahves e valores de um dicionário com desdobramento de nomes com `.items()`

Um exemplo a estudar...

Finalmente, algo quase inútil, a função `.keys()` pode ser usada para passar pelas chaves de um dicionário.

Inútil porque, se não usarmos a função o `for`, por convenção passa pelas chaves de um dicionário:

<div class="python_box">
``` python3
d = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

# isto poderia ser
# for i in d:
for i in d.keys():
    print(i)
```
</div>

```
H
Li
Na
K
O
```

### Dicionários em compreensão

Tal como as listas, podemos construir dicionários novos por *dicionários em compreensão*

Basicamente, comparando com as listas em compreensão, usamos `{}` porque estamos a construír dicionários e
agora temos de indicar o termo geral das chaves, depois usar `:` e finalmente indicar o termo geral dos
valores.

Por exemplo, um dicionário que associa números inteiros os seus quadrados, construído em compreensão:

<div class="python_box">
``` python3
d = {i:i**2 for i in range(10)}

# apresentação do resultado:
for k, v in d.items():
    print(k, '---->', v)
```
</div>

```
0 ----> 0
1 ----> 1
2 ----> 4
3 ----> 9
4 ----> 16
5 ----> 25
6 ----> 36
7 ----> 49
8 ----> 64
9 ----> 81
```

<div class="python_box">
``` python3
# Virar um dicionário "do avesso"
# usando um dicionário em compreensão

tperiodica = {'H':1, 'Li':3, 'Na':11, 'K':19, 'O':18}

num2simbs = {na: elem for elem, na in tperiodica.items()}

print(tperiodica)
print(num2simbs)
```
</div>

```
{'H': 1, 'Li': 3, 'Na': 11, 'K': 19, 'O': 18}
{1: 'H', 3: 'Li', 11: 'Na', 19: 'K', 18: 'O'}
```

### `dict()`

A função `dict()` tenta transformar o seu argumento num dicionário. É análoga à função
`list()` que tenta transformar o seu argumento numa lista.

Em particular, a função `dict()`pode aceitar uma lista de **pares** de objetos, interpretando-os como
associações de chaves a valores.

<div class="python_box">
``` python3
pares = [('Li', 3), ('K', 19), ('O',18)]

d = dict(pares)
print(d)
```
</div>

```
{'Li': 3, 'K': 19, 'O': 18}
```

## Função `zip()`

Embora formalmente esta função não seja nem de dicionários nem de listas, o seu uso é frequente
na linguagem Python e faz muito sentido introduzi-la aqui.

<div class="python_box">
``` python3
nomes = ['Enolase (S.cerevisiae)',
         'Enolase (S.pombe)',
         'Enolase (K.lactis)']
ids = ['P00924', 'P40370', 'Q70CP7']

for x in zip(ids, nomes):
    print(x)
```
</div>

```
('P00924', 'Enolase (S.cerevisiae)')
('P40370', 'Enolase (S.pombe)')
('Q70CP7', 'Enolase (K.lactis)')
```
Como se pode ver por este exemplo, a função `zip()` parece ter gerado pares de objetos a partir de duas
listas. O primeiro par é constituídos pelos dois elementos na posição 0, o segundo pelos dois elementos na
posição 1 e assim sucessivamente até esgotar a lista mais curta.

Como o resultado são pares de valores, podemos desdobrar nomes, tal como fizemos com a função `enumerate()`
ou com a função `.items()`:

<div class="python_box">
``` python3
nomes = ['Enolase (S.cerevisiae)',
         'Enolase (S.pombe)',
         'Enolase (K.lactis)']
ids = ['P00924', 'P40370', 'Q70CP7']

for n, i in zip(nomes, ids):
    print(i, ':', n)
```
</div>

```
P00924 : Enolase (S.cerevisiae)
P40370 : Enolase (S.pombe)
Q70CP7 : Enolase (K.lactis)
```

Com este exemplo (nomes de proteínas e seus *Uniprot accessions* que estão em listas diferentes) podemos
criar uma tabela a partir das duas listas, representada como um dicionário.

Começando por usar um dicionário em compreensão combinado com `zip()`:

<div class="python_box">
``` python3
nomes = ['Enolase (S.cerevisiae)',
         'Enolase (S.pombe)',
         'Enolase (K.lactis)']
ids = ['P00924', 'P40370', 'Q70CP7']

d = {n: i for i, n in zip(nomes, ids)}

print(d)
```
</div>

```
{'P00924': 'Enolase (S.cerevisiae)', 'P40370': 'Enolase (S.pombe)', 'Q70CP7': 'Enolase (K.lactis)'}
```

Combinando a função `zip()` com a função `dict()`, a criação do
dicionário fica ainda mais sucinta:

<div class="python_box">
``` python3
nomes = ['Enolase (S.cerevisiae)',
         'Enolase (S.pombe)',
         'Enolase (K.lactis)']
ids = ['P00924', 'P40370', 'Q70CP7']

d = dict(zip(nomes, ids))

print(d)
```
</div>

```
{'Enolase (S.cerevisiae)': 'P00924', 'Enolase (S.pombe)': 'P40370', 'Enolase (K.lactis)': 'Q70CP7'}
```

Como é que isto resultou?

`zip()` gera pares de objetos vindos das duas listas. `dict()` aceita uma lista de pares de valores como argumento e tenta interpreta-los como *chave:valor*. E é tudo muito sucinto:

    dict(zip(nomes, ids))

*juntem-se ordenadamente os elementos de cada lista aos pares e construa-se um dicionário a partir desses pares*