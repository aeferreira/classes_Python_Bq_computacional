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

# Conceitos básicos

## Programas como textos

Um programa é simplesmente um texto escrito numa linguagem de programação, por exemplo na linguagem Python.

Na linguagem Python, esse texto é interpretável por um computador como um conjunto de "comandos" de "ordens" para serem executados.

![](images/prog.gif)

Quando "corremos" ou "executamos" um programa essas ordens são executadas (a grande velocidade, diga-se) e o programa produz um resultado.

![](images/prog_has_run.gif)

Os comandos são executados um a um à medida que aparecem no texto ("de cima para baixo"), embora esta ordem possa ser alterada por indicações especiais capazes de **repetir comandos** ou executar **comandos em alternativa**, como veremos mais tarde.

(objects_names)=
## Objetos e nomes

### Objetos fundamentais

Para as primeiras impressões sobre a linguagem Python começaremos não por escrever
e executar pequenos programas mas por usar um modo interativo chamado a *Python Shell*.

Neste modo interativo, escrevem-se comandos que são executados imediatamente originando um resultado.

Tendo uma distribuição da linguagem Python instalada, podemos iniciar uma *Python shell* numa
janela de terminal ("linha de comando", "shell").

No sistema Windows, por exemplo, usando a Anaconda Prompt da distribuição Anaconda escrevemos

    python

para iniciar uma *Python shell*.

![](images/open_shell.gif)

Como alternativa, podemos iniciar uma aplicação que contem uma *Python shell* chamada *Idle*,
escrevendo

    idle

![](images/open_idle.gif)

Reconhece-se a *Python shell* por apresentar

```{code-cell} pycon
>>>
```

a indicar que podemos escrever um comando do Python.
Ao terminar o comando com `Enter` obtemos imediatamente uma resposta.

Vamos experimentar alguns comandos.

Muitas vezes, os comandos da linguagem Python consistem na manipulação daquilo que se designa genericamente por **objetos** (virtuais, claro).

Estes *objetos* são valores que estão representados na memória do computador, num determinado momento durante a execução do programa.

#### Números

Números são uns dos objetos mais fundamentais da linguagem Python. Podemos usar a *Python Shell* como uma calculadora. Experimente estes comandos:


```{code-cell} pycon
:tags: [remove-output]
>>> 45 + 32
77
>>> 3.27 * 0.18
0.5886
>>> (1 + 5**0.5) / 2
1.618033988749895
>>>
```

Numa expressão envolvendo números, podemos usar (vários níveis de) parêntesis curvos `()` e as seguintes operações:

| Operador   | Operação         |
|:----------:|:-----------------|
|`+`         | adição           |
|`-`         | subtração        |
|`*`         | multiplicação    |
|`/`         | divisão          |
|`**`        | potenciação      |
|`%`         | resto da divisão |

As regras de prioridade são: `**` tem maior prioridade do que `*` `/` que têm maior prioridade do que `+ -`. Em caso de “empate” e sem parêntesis, os cálculos são feitos da esquerda para a direita.

```{code-cell} pycon
:tags: [remove-output]
>>> - (4.2 * 0.01)**(1/3)
-0.347602664488645
>>> (1 + 5**(1/2)) / 2
1.618033988749895
>>> 5 % 3
2
```

Naturalmente, podemos trabalhar com números com casas decimais, designados genericamente como *números em vírgula flutuante*. 

Na gíria é muitas vezes usada a designação *floats*.


```{code-cell} pycon
:tags: [remove-output]
>>> 4.2 * 0.01
0.042
>>> 4.2 * 1e-2
0.042
>>> 4.2e3 - 2e2
4000.0
```


Note a utilização da representação “de engenharia”, por exemplo `4.2e3`, equivalente a 4.2 x 10<sup>3</sup>.

```{admonition} Atenção
:class: warning
Nos números em Python usa-se sempre um ponto decimal `.` (e não uma vírgula)
```

#### *Strings*

Um outro tipo de objetos fundamentais num programa são as *strings*.

Estas são pequenos textos entre `""` ou `''`.

São sequências de caracteres (além das letras, os espaços e pontuação, desde que estejam entre as aspas,
contam como caracteres).

```{code-cell} pycon
:tags: [remove-output]
>>> "Hoje fiquei em casa"
'Hoje fiquei em casa'
>>> 'Mas fiz uns programas'
'Mas fiz uns programas'
>>> "Com muita determinação"
'Com muita determinação'
>>>
```

É indiferente usar `"` ou `'`. Se precisarmos de usar um tipo de aspas "no interior" de uma *string*
podemos usar o outro tipo para delimitar a *string*:


```{code-cell} pycon
:tags: [remove-output]
>>> "Hoje não fui p'rá FCUL"
"Hoje não fui p'rá FCUL"
>>>
```

Podemos "somar" *strings* e multiplicar *strings* por um número inteiro:

```{code-cell} pycon
:tags: [remove-output]
>>> 'Hoje vai' + " chover"
'Hoje vai chover'
>>> "Blá" * 4
'BláBláBláBlá'
>>>
```


Mas não podemos fazer certo tipo de operações entre números e strings:

```{code-cell} pycon
---
tags: [raises-exception, remove-output]
---
>>> 2 + "muito"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    2 + "muito"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```


Nem mesmo quando um número é, realmente, uma *string*:

```{code-cell} pycon
---
tags: [raises-exception, remove-output]
---
>>> 4 / "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>>
```

#### Objetos booleanos

No Python existem dois objetos que representam os conceitos de *verdadeiro* e *falso*.
São eles `True` e `False` (começam por maiúscula).

Estes objetos surgem como resul11tado de expressões lógicas, isto é, cujo resultado pode ser considerado falso ou verdadeiro.

```{code-block} pycon
>>> 5 > 5
False
>>> 7 > 5
True
>>> 2 < 1
False
>>> 4.0 == 16**0.5
True
>>> 5 != 5
False
```

Os símbolos `==` e `!=` são pouco usuais: eles significam **igual** e **diferente** em comparações lógicas, respetivamente.

O conjunto dos operadores de comparação é o seguinte:

|operador |significado|
|---------|-----------|
|`>`      | maior     |
|`<`      | menor     |
|`>=`     | maior ou igual|
|`<=`     | menor ou igual|
|`==`     | igual a (Nota: **são dois sinais de igual consecutivos**)|
|`!=`     | diferente de|

E podemos usar as seguintes operações lógicas:

|operador |significado|
|---------|-----------|
|`and`    | conjunção (*e*)      |
|`or`     | disjunção (*ou*)     |
|`not`    | negação   (*não*)    |


Por exemplo:

```{code-block} pycon
>>> (5 >= 5) and not (7 > 10)
True
```


#### Números complexos

Finalmente, o Python permite usar números complexos.

Usando a letra `j` no fim de um número indicamos a parte imaginária de um número complexo:

```{code-block} pycon
>>> 1j * 1j
(-1+0j)
>>> 2 + 3j + 4 + 7j
(6+10j)
>>> (3 + 2j) * (5 + 1j)
(13+13j)
>>>
```

#### Função `type()`

Por vezes é necessário saber qual o tipo de um objeto ou do resultado de uma expressão.

A função `type()` dá como resultado o tipo do objeto ao qual é aplicada:

:::{code-block} pycon
>>> type(36)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("Ha " * 5)
<class 'str'>
>>> type(5 >= 5)
<class 'bool'>
:::

### Atribuição de nomes a "objetos"

```{admonition} Nota
:class: note
Este é um dos mais fundamentais comandos em programação!
```

A forma geral é

    <nome> = <expressão>

Vejamos um exemplo:

```{code-block} pycon
>>> a = 4
>>> b = 3.2
>>> c = a + b
>>> d = c ** 0.5
>>> a
4
>>> b
3.2
>>> c
7.2
>>> d
2.6832815729997477
>>>
```

Numa *Python shell* ou num programa, a atribuição de um nome ao resultado
de uma expressão não produz imediatamente um resultado mas permite dar um nome a um valor
para utilizar mais à frente.

Depois de uma atribuição, **o nome pode ser usado em vez do valor do
objeto (ou resultado de uma expressão)**. Mesmo em atribuições seguintes.

No exemplo anterior, os valores com os nomes `a`e `b` (respetivamente 4 e 3.2) foram
usados no cálculo de uma expressão `a + b` ao qual foi dado o nome `c`.

Um exemplo com *strings*:

```{code-block} pycon
>>> hoje = "Hoje é quinta feira"
>>> mês = "Março"
>>> tudo = hoje + ' e estamos em ' + mês
>>> tudo
'Hoje é quinta feira e estamos em Março'
>>>
```

**Que nomes podemos usar?**

As regras são:

1.  Um nome é uma combinação de letras minúsculas ou maiúsculas (podendo
    ser acentuadas) ou dígitos (0 to 9) ou o *underscore*. Nomes como
    `x`, `Km_1` ou `velocidade_da_reaccao` são exemplos válidos.
    
    ![](images/piso_2.jpg)

2.  Um nome não pode começar com um dígito. `1x` é inválido, mas `x1` é
    aceitável.
3.  Palavras usadas como comandos da linguagem (*keywords*) não são
    permitidas (por exemplo, `for`). Na documentação do Python pode-se
    encontrar uma [lista](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
    com estas palavras "reservadas".
4.  Não são permitidos espaços ou símbolos como `!, @, #, %` nos nomes.

:::{warning}
A partir deste ponto todos os exemplos serão baseados em programas e não numa *Python shell*.

Aconselha-se a familiarização com uma aplicação de edição e execução de programas,
por exemplo o *Visual Studio Code*.
:::

Um outro exemplo, mais útil, o cálculo do perímetro de um círculo, a partir do valôr do diâmetro:

```{code-cell} ipython3
pi = 3.1415
diâmetro = 10
perímetro = pi * diâmetro

perímetro
```

Podemos realizar várias atribuições de nomes na mesma linha. Para isso indicamos vários nomes do lado
esquerdo do sinal  `=` e (um mesmo número de) expressões do lado direito. Os nomes e as expressões são
**separados por vírgulas** `,`

Modificando um pouco o exemplo anterior para ilustrar esta técnica:

```{code-cell} ipython3
pi, diâmetro = 3.1415, 10

perímetro = pi * diâmetro

perímetro
```


```{code-cell} ipython3
# Comentários começam por #

# Podemos dar nomes a vários objetos
# de uma só vez:
a, b  =  3, "experiência"

a, b
```

Mais tarde veremos uma generalização desta técnica muito útil.

Já agora, linhas começadas por `#` são *comentários*.

Comentários são linhas completamente ignoradas durante a execução de um programa.
Servem como notas importantes deixadas para que o autor do programa ou outras pessoas
possam mais tarde, ao ler o programa, melhor comprender o que um programa está a fazer.


### `print()`

Um programa em Python é, como foi dito, uma sequência de comandos
que são executados um a um, a grande velocidade, quando o programa é
executado.

Ao contrário de uma *Python shell*, durante a execução de um programa os comandos
**não produzem resultados imediatamente**. Por exemplo, executando este programa:


``` python3
a = 4
b = 3.2
c = a + b
d = c ** 0.5
```

O resultado é o seguinte:

```
 
```

Num programa, podemos **apresentar** o valor que um objeto tem com a
função `print()`.

Um exemplo:

```{code-cell} ipython3
a = 4
b = 3.2
c = a + b
d = c ** 0.5
print(a)
print(b)
print(c, d)
```

Embora este programa faça vários cálculos e atribuições de nome, o resultado visível da execução do programa
resulta das funções `print()`.

Como se viu com a última linha (`print(c,d)`) numa só função `print()` podemos apresentar vários objetos, ou valores associados a nomes ou expressões **separado-os por vírgulas**. No resultado de um programa é inserido um espaço entre as várias partes.

Usando `print()` com *strings*, as aspas são eliminadas.


```{code-cell} ipython3
hoje = "Hoje é quinta feira"
mês = "Março"
tudo = hoje + ' e estamos em ' + mês

print(hoje)
print(mês)
print(tudo)
```

### Alteração dos objetos associados a um nome

Durante a execução de um programa, os objetos associados a um mesmo nome
podem variar:

```{code-cell} ipython3
a = 2
b = 3
c = 'Olá'

b = a + b
a = a + 1
c = a + b

print("a =", a)
print("b =", b)
print("c =", c)
```

Para melhor compreender as mudanças que ocorrem nos valores atribuídos
aos nomes de `a`, `b` e `c` no programa anterior, podemos modifica-lo,
mostrando, com `print()`, os valores atualizados desses nomes, após cada
atribuição. Associe cada `print()` a cada linha do resultado do programa
e compreenda as diferentes alterações dos valores associados a cada nome:


```{code-cell} ipython3
a = 2
b = 3
c = 'Olá'
print("a =", a, "b =", b, "c =", c)

b = a + b
print("a =", a, "b =", b, "c =", c)
a = a + 1
print("a =", a, "b =", b, "c =", c)
c = a + b
print("a =", a, "b =", b, "c =", c)
```

É claro que estas variações de nomes e valores ocorrem muito depressa.

````{admonition} A assimetria de uma atribuição de nome
:class: note
Note-se que um comando de atribuição de nome é completamente **assimétrico**:

:::{tip}
Do lado esquerdo do `=` fica apenas um nome.

Do lado direito fica uma expressão a calcular, seja ela qual for.
:::

Repare que, em programação, é perfeitamente possível escrever a "falsidade matemática"

```
a = a + 1
```

Não se trata de dizer que o lado esquerdo é igual ao lado direito. Trata-se de calcular
o lado direito e dar o nome que está do lado esquerdo. Estamos a dar uma ordem *usa o valor
de `a`, acrescenta 1 e dá o nome `a` ao resultado*.

Mas, no Python, dá um erro escrever uma coisa como

```
2 * a + 4 = a
```

Resumo: à direita uma expressão, à esquerda o nome a dar ao resultado
````

### Interpolação de valores em *strings* (_"Strings f"_)

As *strings* podem ter valores "interpolados", usando os nomes desses
valores ou expressões. Para isso, usam-se `{}` para identificar em que
sítio da *string* deve ficar cada valor e a *string* deve ter a letra
`f` como prefixo. Um exemplo:


```{code-cell} ipython3
a = 4.8
b = 3.2
c = a + b

print(f'a é igual a {a}, mas b = {b}, enquanto que c = {c}')
```

Um outro exemplo, introduzindo mais pormenores:

```{code-cell} ipython3
a, b  =  3, "experiência"

print(f"a = {a} b = {b}")

# print() deixa uma linha de intervalo
print()

a, b = 3, 4
print(f"a = {a} b = {b}\n")

# Podemos trocar dois nomes desta maneira
a, b = b, a
print('Depois de trocar a e b...')
print(f"a = {a} b = {b}")
```

Nota: quando numa *string* aparece o caractere "especial" `\n`, este
provoca uma linha suplementar quando a *string* é apresentada com a
função `print()`.

## Funções e módulos

### Funções "integradas" na linguagem

#### `abs()`, `int()`

Além da função `print()`, as funções `int()`, que calcula a parte inteira de 
um número e `abs()`, que calcula o valor absoluto (módulo) de um número, fazem parte
integrante da linguagem Python.


```{code-cell} ipython3
numero = -3.8
x = int(numero)
y = abs(numero)

print(numero, '\n')
print(x)
print(y)
```

Podemos encontrar a lista destas funções na documentação oficial da
linguagem Pyhton:

[Python Built-in functions](https://docs.python.org/3/library/functions.html)

### Conversão entre tipos de objetos

#### `int()`, `float()`, `complex()` e `str()`

As funções `int()`, `float()`, `complex()` e `str()` fazem conversões
para os vários **tipos** de objetos:

-   **inteiros**
-   *floats*
-   **complexos** (em que `j` é a unidade imaginária)
-   *strings*

```{code-cell} ipython3
x = 3.8

print(x,'\n')
print(int(x))
print(complex(x))
print(str(x))
```

```{code-cell} ipython3
s = '3.4e4'
f = float(s)
c = complex(s)

print(s, '\n')
print(f)
print(c)
```

As conversões nem sempre são possíveis...

```{code-cell} ipython3
---
tags: [raises-exception]
---
s = 'Vamos ver...'
print(s, '\n')

print(float(s))
```

## Módulos: funções adicionais

Além das funções integradas, existem muitos **módulos** contendo funções
adicionais.

Estes módulos têm de ser *importados* para que as funções fiquem
disponíveis.

Um exemplo é o módulo **math** que contem muitas funções (e algumas
constantes) matemáticas:

```{code-cell} ipython3
import math

x = 2.0

y = math.log(x)
print('ln(2.0) =', y)

y = math.log10(x * 5)
print('ln10(2.0 * 5) =', y)

y = math.exp(x)
print('exp(2.0) =', y)

y = math.sin(x)
print('sin(2.0) =', y)
```

```{code-cell} ipython3
y = math.sin(math.radians(90))
print('sin(90°) =', y)

print('pi =', math.pi)

print('e =', math.e)

y = math.sin(math.pi / 2.0)
print('sin(π / 2) =', y)
```

```{code-cell} ipython3
y = math.factorial(100)
print('100! =', y)
```

[Leitura interessate sobre o módulo `math`](https://realpython.com/python-math-module/)

Um outro exemplo é o módulo **calendar** que contem muitas funções
relacionadas com datas e calendário.

Um exemplo é a função `weekday()`, que, ao ser dado um ano, mês e dia,
calcula um número que representa o dia da semana. (0 - seg, 1 - ter, 2 -
qua, 3 - qui, 4 - sex, 5 - sab, 6 - dom)

```{code-cell} ipython3
import calendar

print(calendar.weekday(2017, 3, 30))
#nota: 0:seg 1:ter 2:qua 3:qui 4:sex 5:sab 6:dom
```

Outro exemplo é a função `calendar()`, que constrói uma *string* com um
calendário de um determinado ano:


```{code-cell} ipython3
import calendar
print(calendar.calendar(2022))
```

## Exemplo: Raízes da equação do 2º grau

Calcular as soluções da equação do 2º grau

$a x^2 + b x + c = 0$

ou seja

Dados $a, b$ e $c$, calcular

$x_1 = \frac{-b + \sqrt{b^2 -4 a c}}{2 a}$ e
$x_2 = \frac{-b - \sqrt{b^2 -4 a c}}{2 a}$

```{code-cell} ipython3
# Este programa calcula x tal que a x2 + b x + c = 0
# testar com os seguintes valores (1,4,1) , (1,2,1) , (1,1,1)

a, b, c = 1, 4, 1

# cálculo do discriminante
delta = b**2 - 4.0 * a * c
rdelta = delta**0.5

x1 = (- b + rdelta) / (2.0 * a)
x2 = (- b - rdelta) / (2.0 * a)

print('a =', a, 'b =', b, 'c =', c, '\n')
print(f"x1 ={x1}, x2 = {x2}")
```

Da matemática, sabemos que uma equação do segundo grau pode ter 2
soluções reais, uma solução real "dupla", ou duas soluções complexas,
que neste caso serão complexos conjugados.

Podemos correr o programa várias vezes, para diferentes valores de $a$,
$b$, $c$, tentando obter as três situações. Ao fazer isto estamos a
**testar** o programa.

Para fazer estes testes, basta modificar as linhas que definem os
valores para `a`, `b` e `c` e voltar a executar o program.

Com a = 1, b = 4, c = 1:

    a = 1 b = 4 c = 1 

    x1 =-0.2679491924311228, x2 = -3.732050807568877

Com a = 1, b = 2, c = 1:

    a = 1 b = 2 c = 1 

    x1 =-1.0, x2 = -1.0

Com a = 1, b = 1, c = 1:

    a = 1 b = 1 c = 1 

    x1 =(-0.49999999999999994+0.8660254037844386j), x2 = (-0.5-0.8660254037844386j)

O programa funciona e parece dar resultados corretos para as três
situações pretendidas (embora se note um pequeno erro no caso das duas
soluções complexas que deveriam ser, exatamente, dois complexos
conjugados).

No entanto, seria mais adequado se o programa pudesse apresentar uma
pequena mensagem que indicasse em qual das três situações está o
resultado (2 soluções reais ou uma solução real dupla ou duas soluções
complexas).

(Podemos também tentar corrigir o pequeno erro).

Para isto, o programa deve ter um **comportamento diferente**, consoante
o tipo de resultado.

Da matemática, sabemos que o que define o tipo de resultado é o valor do
"discriminante", $\Delta = b^2 - 4 a c$.

-   quando $\Delta > 0$ temos duas soluções reais.
-   quando $\Delta = 0$ temos uma solução real (solução dupla).
-   quando $\Delta < 0$ temos duas uma soluções complexas (complexos
    conjugados).

Podemos reescrever o programa de modo a realizar o cálculo das soluções
e apresentar uma mensagem de um modo diferente, consoante o valor de
$\Delta$ ?

## Execução alternativa

### Alternativa `if...else`

A linguagem Python permite a execução **alternativa** de blocos de
comandos.

Continuando com o exemplo anterior, vamos primeiro distinguir o caso das
soluções reais ($\Delta \geqslant 0$) do caso das soluções complexas
($\Delta < 0$).

```{code-cell} ipython3
# Este programa calcula x tal que a x2 + b x + c = 0
# testar com os seguintes valores (1,4,1) , (1,2,1) , (1,1,1)

a, b, c = 1, 4, 1

# cálculo do discriminante
delta = b**2 - 4.0 * a * c

# separar soluções reais das complexas
if delta < 0.0:
    rdelta = (-delta)**0.5 * 1j
    print('Soluções complexas:')
else:
    rdelta = (delta)**0.5
    print('Soluções reais:')

x1 = (- b + rdelta) / (2.0 * a)
x2 = (- b - rdelta) / (2.0 * a)

print(f'Para a = {a}  b = {b}  c = {c}')
print(f"x1 = {x1}\nx2 = {x2}")
```

Testando agora o programa para as três situações possíveis:

$\Delta > 0$:

    Soluções reais:
    Para a = 1  b = 4  c = 1
    x1 = -0.2679491924311228
    x2 = -3.732050807568877

$\Delta = 0$:

    Soluções reais:
    Para a = 1  b = 2  c = 1
    x1 = -1.0
    x2 = -1.0

$\Delta < 0$:

    Soluções complexas:
    Para a = 1  b = 1  c = 1
    x1 = (-0.5+0.8660254037844386j)
    x2 = (-0.5-0.8660254037844386j)

O programa funciona, agora, sem problemas.

É feito um teste ao valor de `delta` à frente do comando `if` e é
executado **um** de dois blocos alternativos:

-   as linhas entre `if` e `else:`, caso `delta` seja negativo, ou
-   as duas linhas depois de `else:`, caso `delta` seja positivo.

A forma geral de incluir **blocos alternativos** com `if...else` é:

    if <condição> :
        <comandos para condição verdadeira>
    else:
        <comandos para condição falsa>

Podemos ter várias linhas no bloco `if` e no bloco `else`.

É o **alinhamento** das linhas do programa (também chamada *indentação*)
que define os dois blocos:

![](images/blocks_if_else.png)

Note-se que, no programa anterior, as linhas

    x1 = (- b + r_delta) / (2.0 * a)
    x2 = (- b - r_delta) / (2.0 * a)

já **não pertencem** ao bloco `else`. Isto porque o seu alinhamento é
(de novo) igual ao de todas as outras linhas fora dos blocos `if...else`
(e estão alinhadas com as próprias linhas dos comandos `if` e `else`)


O programa está bem melhor na maneira de apresentar os resultados,
separando o caso real do complexo.

Mas, perfeito, perfeito, seria tratar o caso em que $\Delta = 0$ de uma
forma diferente, tendo o cuidado de apresentar **um único valor, no caso
de uma raíz dupla**.

Precisamos, para isso, que o programa possa se adaptar a cada uma das
**três alternativas**.

### Alternativas `if...elif...else`

Usando o comando `elif` podemos testar **mais do que uma condição** e
executar em alternativa e, consequentemente, **mais do que dois blocos**
de comandos.

Seguindo o exemplo da resolução de uma equação do segundo grau, podemos
separar os três casos associados ao valor de $\Delta$ da seguinte forma:

```{code-cell} ipython3
# Este programa calcula x tal que a x2 + b x + c = 0
# testar com os seguintes valores (1,4,1) , (1,2,1) , (1,1,1)

a, b, c = 1, 4, 1

# cálculo do discriminante
delta = b**2 - 4.0 * a * c

if delta < 0.0:
    rdelta = (-delta)**0.5 * 1j
    print('Soluções complexas:')
elif delta > 0:
    rdelta = (delta)**0.5
    print('Soluções reais:')
else:
    x = - b / (2.0 * a)
    print('Solução real (dupla):')
    
x1 = (- b + rdelta) / (2.0 * a)
x2 = (- b - rdelta) / (2.0 * a)    

print(f'Para a = {a}  b = {b}  c = {c}')

if delta == 0:
    print("x =", x)
else:
    print(f"x1 = {x1}\nx2 = {x2}")
```

O comando `elif` é uma abreviatura de *else* + *if* e possibilita o
teste de uma nova condição para além daquela já usada no comando `if`.

Podem ser usados **vários comandos** `elif`.

E note-se que, mais uma vez, podemos ter várias linhas em cada bloco : o
**alinhamento** (*identação*) define os blocos:

![](images/blocks_if_elif.png)

Testando agora o programa para as três situações possíveis:

$\Delta > 0$:

    Soluções reais:
    Para a = 1  b = 4  c = 1
    x1 = -0.2679491924311228
    x2 = -3.732050807568877

$\Delta = 0$:

    Solução real (dupla):
    Para a = 1  b = 2  c = 1
    x = -1.0

$\Delta < 0$:

    Soluções complexas:
    Para a = 1  b = 1  c = 1
    x1 = (-0.5+0.8660254037844386j)
    x2 = (-0.5-0.8660254037844386j)

Pode ser usado todo um conjunto de blocos `if...else...` **"dentro"** de
um bloco `if` ou `elif` ou `else`.

Por exemplo, o o programa também poderia ser escrito da seguinte forma:

```{code-cell} ipython3
# Este programa calcula x tal que a x2 + b x + c = 0
# testar com os seguintes valores (1,4,1) , (1,2,1) , (1,1,1)

a, b, c = 1, 4, 1
print(f"Para a = {a}, b = {b}, c = {c}\n")

# cálculo do discriminante
delta = b**2 - 4.0 * a * c

if delta == 0.0:
    print('Solução real (dupla):')
    x = -b / (2.0 * a)
    print("x =", x)
else:
    if delta < 0:
        print('Soluções complexas:')
        r_delta = (-delta)**0.5 * 1j
    else:
        print('Soluções reais:')
        r_delta = (delta)**0.5

    x1 = (- b + r_delta) / (2.0 * a)
    x2 = (- b - r_delta) / (2.0 * a)    
    print("x1 =", x1, ", x2 =", x2)
```

:::{note}
O bloco `else` não é obrigatório. Se não fizer sentido a
existência de uma condição alternativa ao `if`, este bloco pode ser
omitido.
:::

Vejamos agora um outro exemplo da utilização de blocos alternativos.

**Exemplo: Regra dos anos bissextos**

-   Se o ano é divisível por 4, então é bissexto

Regra em vigor até 1582 (calendário Juliano, de Júlio César)

```{code-cell} ipython3
# Este programa determina de um ano é bissexto
# Testar com 2015 N, 2012 S, 1900 N, 2000 S

a = 2015

if a % 4 == 0:
    print(a , "é bissexto")
else: 
    print(a, "não é bissexto")
```

Correndo o programa com diferentes valores de a:

    2015 nao é bissexto

    2012 é bissexto

    1900 é bissexto

    2000 é bissexto

Este programa parece falhar para 1900. Isto acontece porque, na
realidade, a regra actual dos anos bissextos é um pouco mais complexa.

**Exemplo: Regra dos anos bissextos (calendário moderno)**

-   Se o ano é divisível por 4, então é bissexto
-   Excepto os que são divisíveis por 100: não são bissextos
-   Excepto os divisíveis por 100 que sejam exactamente divisíveis por
    400: são bissextos.

Esta regra entrou em vigor após 1582 (calendário Gregoriano, do papa
Gregorio XIII)

Da aplicação desta regra resulta que alguns anos de mudança de século
(sempre divisíveis por 4) não sejam bissextos. É o caso de 1900. E
alguns anos de mudança de século, por exemplo os anos 1600; 2000; 2400,
sejam bissextos.

Podemos adaptar o programa anterior para incluir as duas últimas regras:

```{code-cell} ipython3
a = 2015

if a % 4 == 0 and not (a % 100 == 0 and not a % 400 == 0):
    print(a , "é bissexto")
else: 
    print(a, "não é bissexto")
```

Correndo o programa com diferentes valores:

    2015 nao é bissexto

    2012 é bissexto

    1900 nao é bissexto

Reparar que o resultado é diferente para 1900.

    1900 não é bissexto

Os interessados na história da introdução do calendário gregoriano podem
consultar o artigo

<http://en.wikipedia.org/wiki/Gregorian_calendar>

É desaconselhável escrever uma condição tão complicada num comando `if`:
prejudica muito a legibilidade do programa.

Um programa equivalente, combinando vários blocos de `if...else...` e a
negação lógica `not` que será (possivelmente) mais fácil de perceber é:

```{code-cell} ipython3
a = 2015

if not a % 4 == 0:
    print(a, "não é bissexto")
else:
    if not a % 100 == 0:
        print(a , "é bissexto")
    else:
        if a % 400 == 0:
            print(a , "é bissexto")
        else:
            print(a , "não é bissexto")
```

Correndo o programa com diferentes valores de a:

    2015 não é bissexto
    2012 é bissexto
    1900 não é bissexto
    2000 é bissexto

## Função `input()`


Até agora, nos exemplos foram apresentados, são incluídos no programa os
valores a partir dos quais se fazem os cálculos (tradicionalmente
chamados o *input* do programa).

Por exemplo, nos exemplos da resolução de uma equação do segundo grau
incluímos no princípio do programa os valores dos coeficientes:

    a, b, c = 1, 4, 1

Os programas partem destes valores, realizam cálculos e apresentam
resultados.

A linguagem Python suporta também um outro mecanismo: **o pedido de
valores ao** *utilizador* durante a execução do programa.

A função `input()` tem este papel: durante a execução de um programa, ao
passar por uma função `input()` o programa pára esperando que seja
introduzido uma *string*. A função permite também seja apresentada uma
mensagem de indicação do que está a ser pedido.

Vejamos com um exemplo:

```{code-cell} ipython3
:tags: [raises-exception, remove-stderr, remove-output]
a = input('Valor de a? ')
b = input('Valor de b? ')
c = input('Valor de c? ')

a = float(a)
b = float(b)
c = float(c)

# cálculo do discriminante
delta = b**2 - 4.0 * a * c

if delta == 0.0:
    print('Solução real (dupla):')
    x = -b / (2.0 * a)
    print("x =", x)
else:
    if delta < 0:
        print('Soluções complexas:')
        r_delta = (-delta)**0.5 * 1j
    else:
        print('Soluções reais:')
        r_delta = (delta)**0.5

    x1 = (- b + r_delta) / (2.0 * a)
    x2 = (- b - r_delta) / (2.0 * a)    
    print("x1 =", x1, ", x2 =", x2)
```

Executando este programa várias vezes, testando com os diferentes
casos, agora os valores dos coeficientes são "pedidos" pelo programa:

```
Valor de a? 1
Valor de b? 4
Valor de c? 1
Soluções reais:
x1 = -0.2679491924311228 , x2 = -3.732050807568877
```

```
Valor de a? 1
Valor de b? 2
Valor de c? 1
Solução real (dupla):
x = -1.0
```

```
Valor de a? 1
Valor de b? 1
Valor de c? 1
Soluções complexas:
x1 = (-0.5+0.8660254037844386j) , x2 = (-0.5-0.8660254037844386j)
```

## Exercícios sobre conceitos fundamentais

**Software**

- *Python Shell* ou *Idle com Python Shell*
- *Visual Studio Code*.

### Exercício 1 (Números, *strings*, números complexos)

1. Abra uma Python Shell ou uma Python Shell no Idle.
2. Corra vários dos comandos das secção {ref}`objects_names`. Familiarize-se com
    - Números
    - Números em vírgula flutuante (com casas decimais)
    - *Strings*
    - Expressões booleanas, `True` e `False`
    - Dar nomes a objetos

### Exercício 2 (cálculos simples)

Ainda na *Python Shell*, calcule

1. O número de codões no código genético (4<sup>3</sup>)
2. O número de diferentes sequências possíveis num péptido com 50 aminoácidos (20<sup>50</sup>)
3. A **percentagem** de vitórias de uma equipa que conseguiu vencer 30 jogos em 46 disputados.

### Exercício 3 (VSCode e "número de ouro")

- Crie uma pasta de trabalho onde irá criar uma série de programas em Python

```{admonition} Nota
:class: Note
Um programa em Python deve ter um nome acabado em `.py`

```

Os programas vão ser criados como ficheiros de texto editados com o VSCode.

- Abra o editor de texto *Visual Studio Code*. Para isso, use o botão direito sobre a pasta e selecione "Open with Code":
- ![](images/folder_vscode.gif)
- Em alternativa, se o método anterior não funcionar, abra a app *Visual Studio Code* e faça
*File – Open Folder* para a pasta que criou.
- Inicie um ficheiro novo, com *File – New File*.
- Escreva um programa que calcule e mostre, com `print()`, a "proporção de ouro", isto é, o número
    phi = (1+√5)/2 e também o seu quadrado e seu inverso.

```{admonition} Importante
:class: warning
Logo que começar a escrever o programa deve salvá-lo o mais depressa
possível com *File – Save As…*!

Deve-lhe dar um nome acabado em `.py`, por exemplo `phi.py`.

```

- Ao salvar o programa com o nome acabado em `.py`, a extensão Python para o VSCode será instalada:
- ![](images/python_ext_vscode.gif)
- Só precisa de instalar esta extensão uma vez (em cada computador que usar)!
- Caso não fique imediatamente instalada, escreva "Python" em "Search Extensions in ...". A primeira que aparece é a extensão Python da Microsoft. Use o botão "Install" para instalar a extensão. Só precisa de o fazer uma vez!


```{admonition} Nota
:class: note
Se o VSCode indicar que falta selecionar um “Python interpreter”, deve escolher o interpretador instalado do Anaconda, clicando no canto inferior direito onde diz “No Interpreter”. Depois de escolher, deve ver o seguinte no canto inferior direito do VSCode:

![](images/chosen_interpreter.gif)

Ver o ponto "Select Python interpreter" [Nesta página](https://marketplace.visualstudio.com/items?itemName=ms-python.python&ssr=false#overview)

```

- Familiarize-se com a edição de um programa no *VSCode*. Use alguns *shortcuts* do teclado: `Home` e `End`. `Ctrl-C (copy)`, `Ctrl-V (paste)`. Selecione com o rato e com o teclado. 
- Execute (corra) o programa. Para isso utilize o botão no canto superior direito
    ![](images/run_vscode.gif)
- Observe o resultado do programa. Corra o programa outra vez. 
- Note as propriedades $\phi^2 = \phi +1$ e $1 / \phi = \phi  - 1$

### Exercício 4 (°C para °F)

Escreva um outro programa (faça *File – New File* para criar um novo programa) que calcula os graus Farenheit correspondentes a 36.5 graus Celsius. Não se esqueça de salvar o programa com um nome acabado em `.py`. A fórmula de conversão é:

&deg;F = 32 + (9/5) * &deg;C

Use a função `print()` com *strings* para apresentar mensagens explicativas sobre o resultado (tipo *36.5 graus Celsius são ....*)

````{admonition} Solução
:class: tip, dropdown
```{code-block} ipython3
C = 36.5
F = (9/5) * C + 32

print(f"{C} °C correspondem a {F} °F")
```
````

### Exercício 5 (`import` e função `input()`)

Escreva o seguinte programa novo (sugestão: copy-paste).

Note que há muita coisa neste programa um pouco avançada,
mas o objetivo é ilustrar a função `input()`:

```{code-block} python3
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_PT.utf8")

print('Programa: tempo até agora')

name = input('Qual o seu nome? ')
day = input('Em que dia nasceu? ')
month = input('Em que mês nasceu (1-12)? ')
year = input('Em que ano nasceu? ')

year = int(year)
month = int(month)
day = int(day)

birth = datetime(year, month, day)
now = datetime.now()

dif = now - birth

print(f'\n{name}, o seu tempo de vida é')
print(dif)
print('ou seja,', int(dif.total_seconds()), 'segundos')
print('Nasceu em', birth.strftime("%d %B %Y, %A"))
```

Este programa usa o módulo `datetime` para realizar cálculos com datas e tempos. Para isso é necessário fazer `from datetime import datetime` no início do programa.

Corra o programa e observe que, no terminal de resultados, o programa pára em cada função `input()`, “pedindo” a introdução de um valor:

![](images/prompts.gif)

O programa só continua fazendo `Enter`, após a introdução de cada valor.

```{admonition} Nota
:class: note
Para correr o programa do princípio pode sempre “destruír” os resultados anteriores de um programa usando o botão

![](images/killshell.gif)

```

### Exercício 6 (Acesso programático à UniProt)

- Escreva e corra o seguinte programa (novo, com outro nome, outro ficheiro .py):

```{code-block} python3
import requests

proteína = 'P00924'
link = f'http://www.uniprot.org/uniprot/{proteína}.fasta'

página = requests.get(link).text

print('Sequência da proteína', proteína, 'é')
print(página)
```

- Escreva um novo programa semelhante mudando `.fasta` para  `.txt`.

### Exercício 7 (Solução de equação 1º grau)

- Escreva o seguinte programa:

```{code-block} python3
"""Cálculo da solução de uma equação do 1º grau 0 = mx + b."""

m = input('declive (m) = ')
b = input('ordenada na origem (b) = ')

m = float(m)
b = float(b)

r = -b / m
print(f'raíz = {r}')
```

- Corra o programa e observe os resultados. Experimente correr várias vezes, com diferentes valores de m e b para teste. Inclua um teste com m = 0.

- Corrija o programa de forma a não dar erro com m = 0. Para isso modifique o programa da seguinte maneira:

```{code-block} python3
"""Cálculo da raíz de uma equação do 1º grau 0 = mx + b."""

m = input('declive (m) = ')
b = input('ordenada na origem (b) = ')

m = float(m)
b = float(b)

if m == 0:
    print('Reta horizontal: não há raízes')
else:
    r = -b / m
    print(f'raíz = {r}')
```

Explicação: a parte `if... else ...` faz com que o programa execute **em alternativa** certas partes, consoante o valor de uma condição. Neste exemplo, a condição é m == 0.

### Exercício 8 (Solução equação do 2º grau)

- Escreva um programa que calcule as duas soluções de uma equação do segundo grau

$a \cdot x^2 + b \cdot x + c = 0$

- Para testar o programa, corra com diferentes valores para a, b e c:
    - a = 1, b = 4, c = 2 dá duas soluções reais.
    - a = 1, b = 2, c = 1 dá uma solução dupla: -1
    - a = 1, b = 1, c = 1 dá duas soluções complexas. 


````{admonition} Solução
:class: tip, dropdown
```{code-block} ipython3
# Este programa calcula x tal que a x2 + b x + c = 0
# testar com os seguintes valores (1,4,1) , (1,2,1) , (1,1,1)

a, b, c = 1, 4, 1
print('a =', a, 'b =', b,'c =',c, '\n')

# cálculo do discriminante
delta = b**2 - 4.0 * a * c

if delta < 0.0:
    print('Soluções complexas:')
    r_delta = (-delta)**0.5 * 1j
    x1 = (- b + r_delta) / (2.0 * a)
    x2 = (- b - r_delta) / (2.0 * a)    
    print("x1 =", x1, ", x2 =", x2)
elif delta > 0:
    print('Soluções reais:')
    r_delta = (delta)**0.5
    x1 = (- b + r_delta) / (2.0 * a)
    x2 = (- b - r_delta) / (2.0 * a)    
    print("x1 =", x1, ", x2 =", x2)
else:
    print('Solução real (dupla):')
    x = -b / (2.0 * a)
    print("x =", x)
```
````

### Exercício 9 (Conversão entre F e ω)

- Escreva um programa que converta a velocidade angular de rotação (ω em 10<sup>3</sup> rpm) em força centrípeta (F, em *g*), dado o raio de um rotor de centrifugação (r, em mm). 

A fórmula (**usando aquelas unidades**)  é:

$F = 1.12 \cdot r \cdot \omega^2$

- Teste o programa com r = 108 mm, ω = 10 x 10<sup>3</sup> rpm F = 12 096 *g*

- Escreva outro programa que faça a conversão contrária (de *g* para rpm).

````{admonition} Solução
:class: tip, dropdown
```{code-block} ipython3
# Conversões F centrífuga <-> w (velocidade angular)

print('Escolha:')
resposta = input("Converter 1: w para F ou  2: F para w ?")
resposta = int(resposta)

if resposta == 1:
    w = float(input('w (em 1000 rpm) = '))
    r = float(input('r (em mm) = '))
    F = 1.12 * r * w**2
    print(f'Com r = {r}mm e w = {w}x1000 rpm, F = {F} g')
else:
    F = float(input('F (em g) = '))
    r = float(input('raio (em mm) = '))
    w = (F / (1.12 * r))**0.5
    print(f'Com r = {r}mm e F = {F} g, w = {w} x1000 rpm')
```
````
