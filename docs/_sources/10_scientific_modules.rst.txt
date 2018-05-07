
Python "científico"
===================

Embora não incluídas na distribuição oficial, disponibilizada em
http://www.python.org, as seguintes bibliotecas foram criadas para
adaptar (e aumentar a linguagem Python com a funcionalidade necessária
em muitas aplicações de natureza científica.

Estas bibliotecas são:

-  numpy: objetos de tipo ``array``, que suportam operações vetoriais
-  scipy: muitas funções de cálculo numérico
-  sympy: computação simbólica
-  ipython: deu origem ao projeto Jupyter, que contem a plataforma
   "Jupyter notebooks"
-  matplotlib: a grande bibloteca de gráficos científicos da linguagem
   Python
-  pandas: objetos adequados ao tratamento de dados em larga escala
   (``Series`` e ``DataFrame``)

.. figure:: images/sci_python.png
   :alt: 

``numpy``
---------

Operações "vectoriais"
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    import numpy as np

.. code-block:: ipython3

    numbers = [0.0, 0.2, 0.5, 1.0, 1.1]
    x = np.array(numbers)
    
    print('x = ')
    print(x)
    
    y = 4 * x
    
    print('\ny = 4 * x =')
    print(y)


.. code-block:: text

    x = 
    [ 0.   0.2  0.5  1.   1.1]
    
    y = 4 * x =
    [ 0.   0.8  2.   4.   4.4]
    

A função ``np.array()`` transformou a lista num objeto do tipo *array*.

Estes objetos suportam operações aritméticas "vetoriais": na expressão
``y = 4 * x`` a multiplicação por 4 é aplicada a todos os elementos de
``x``. O resultado é também um *array*.

Por outro lado, as operações aritméticas entre dois *arrays* são
realizadas elemento a elemento:

.. code-block:: ipython3

    a = np.array([0.0, 0.2, -0.5, 1.0, 1.1])
    b = np.array([0.0, 0.1, -1.0, 1.0, 1.0])
    print('a = ', a)
    print('b = ', b)
    
    y = a + b
    
    print('\ny = a + b =')
    print(y)


.. code-block:: text

    a =  [ 0.   0.2 -0.5  1.   1.1]
    b =  [ 0.   0.1 -1.   1.   1. ]
    
    y = a + b =
    [ 0.   0.3 -1.5  2.   2.1]
    

Criação de *arrays* com as funções ``.array()``, ``.arange()`` e ``.linspace()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    x = np.array([1, 1.2, 3, 3.5])
    print(x)


.. code-block:: text

    [ 1.   1.2  3.   3.5]
    

.. code-block:: ipython3

    x = np.arange(1.5, 2.0, 0.1)
    print(x)


.. code-block:: text

    [ 1.5  1.6  1.7  1.8  1.9]
    

.. code-block:: ipython3

    x = np.linspace(1, 2, 5)
    print(x)


.. code-block:: text

    [ 1.    1.25  1.5   1.75  2.  ]
    

.. code-block:: ipython3

    x = np.linspace(1, 2, 6)
    print('x')
    print(x)
    
    y = 4 * x**2 -3
    
    print('\ny = 4 * x**2 -3')
    print(y)


.. code-block:: text

    x
    [ 1.   1.2  1.4  1.6  1.8  2. ]
    
    y = 4 * x**2 -3
    [  1.     2.76   4.84   7.24   9.96  13.  ]
    

.. code-block:: ipython3

    # só necessário em Jupyter notebooks
    %matplotlib inline
    
    from matplotlib import pyplot as pl

.. code-block:: ipython3

    x = np.linspace(-2, 2, 100)
    y = 4 * x**3 -3
    
    pl.grid()
    g = pl.plot(x, y)



.. image:: 10_scientific_modules_files/10_scientific_modules_14_0.png


**Problema: somar os primeiros 1000 quadrados perfeitos**

.. code-block:: ipython3

    print(sum(np.arange(1000)**2))


.. code-block:: text

    332833500
    

Dimensões (``shape``)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    x = np.arange(1, 13)
    print(x)
    
    x.shape = (4,3)
    # significa 4 linhas e 3 colunas
    
    print('\nApós mudar "shape" para (4,3)\nx =\n{}'.format(x))


.. code-block:: text

    [ 1  2  3  4  5  6  7  8  9 10 11 12]
    
    Após mudar "shape" para (4,3)
    x =
    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    

Criação de *arrays* com ``.array()``, ``.ones()``, ``.zeros()``, ``.eye()``, ``.diag()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    x = np.array( [[1, 1.2, 3], [1.3,5.1,1.3]] )
    print(x)
    print('\nshape =', x.shape)


.. code-block:: text

    [[ 1.   1.2  3. ]
     [ 1.3  5.1  1.3]]
    
    shape = (2, 3)
    

.. code-block:: ipython3

    x = np.ones((3,2))
    print(x)


.. code-block:: text

    [[ 1.  1.]
     [ 1.  1.]
     [ 1.  1.]]
    

.. code-block:: ipython3

    x = np.zeros((3,2))
    print(x)


.. code-block:: text

    [[ 0.  0.]
     [ 0.  0.]
     [ 0.  0.]]
    

.. code-block:: ipython3

    x = np.eye(3)
    print(x)


.. code-block:: text

    [[ 1.  0.  0.]
     [ 0.  1.  0.]
     [ 0.  0.  1.]]
    

.. code-block:: ipython3

    x = np.diag([1.2, 3.2, 4.1, 6.3])
    print(x)


.. code-block:: text

    [[ 1.2  0.   0.   0. ]
     [ 0.   3.2  0.   0. ]
     [ 0.   0.   4.1  0. ]
     [ 0.   0.   0.   6.3]]
    

Indexação a várias dimensões
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    x = np.linspace(1,20,20).reshape((5,4))
    print(x)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    

.. code-block:: ipython3

    a = x[3,1]
    
    print(x)
    print('\nx[3,1] =', a)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    
    x[3,1] = 14.0
    

.. code-block:: ipython3

    a = x[3, :]
    
    print(x)
    print('\nx[3, :] =', a)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    
    x[3, :] = [ 13.  14.  15.  16.]
    

.. code-block:: ipython3

    a = x[1:4, 1:4]
    
    print(x)
    print('\nx[1:4, 1:4] =')
    print(a)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    
    x[1:4, 1:4] =
    [[  6.   7.   8.]
     [ 10.  11.  12.]
     [ 14.  15.  16.]]
    

Mas os slices de ``arrays`` unidimensionais também existem, tal como nas
listas:

.. code-block:: ipython3

    x =np.arange(0, 1.1, 0.1)[2:]
    print(x)


.. code-block:: text

    [ 0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]
    

**Problema: mostrar que as diferenças entre os quadrados perfeitos
sucessivos são os numeros ímpares**

.. code-block:: ipython3

    quads = np.arange(12)**2
    print(quads)
    
    difs = quads[1:] - quads[0:-1]
    print(difs)


.. code-block:: text

    [  0   1   4   9  16  25  36  49  64  81 100 121]
    [ 1  3  5  7  9 11 13 15 17 19 21]
    

Indexação booleana
~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    x = np.linspace(1, 10, 6)
    print('x =', x)
    
    a = x < 7
    print('\nx < 7')
    print(a)
    
    y = x[x < 7]
    print('\nx[x < 7]')
    print(y)


.. code-block:: text

    x = [  1.    2.8   4.6   6.4   8.2  10. ]
    
    x < 7
    [ True  True  True  True False False]
    
    x[x < 7]
    [ 1.   2.8  4.6  6.4]
    

**Problema: somar as raízes quadradas dos números inteiros até 100, mas
só as que sejam números inteiros**

.. code-block:: ipython3

    roots = np.arange(0,101)**0.5
    
    # usando a função np.trunc()
    s = sum(roots[np.trunc(roots) == roots])
    
    print(s)


.. code-block:: text

    55.0
    

Indexação com listas de inteiros ou outros *arrays*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    x = np.linspace(5, 15, 6)
    print('x =', x)
    
    i = [1,4,5]
    print('\ni =', i)
    
    y = x[i]
    print('\nx[i] =', y)


.. code-block:: text

    x = [  5.   7.   9.  11.  13.  15.]
    
    i = [1, 4, 5]
    
    x[i] = [  7.  13.  15.]
    

Funções associadas a *arrays*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os objetos do tipo *array* possuem muitas funções associadas.

Algumas são:

-  ``.sum()`` que calcula a soma dos elementos
-  ``.mean()`` que calcula a média dos elementos
-  ``.var()`` que calcula a variância dos elementos
-  ``.std()`` que calcula o desvio padrão dos elementos
-  ``.prod()`` que calcula o produto dos elementos

-  ``.ptp()`` (*peak to peak*) que calcula o máximo - mínimo

-  ``.cumsum()`` que calcula a soma cumulativa dos elementos
-  ``.cumprod()`` que calcula o produto cumulativo dos elementos

No caso da aplicação destas funções a *arrays* multidimensionais,
podemos especifica um "eixo" para aplicar o cálculo.

Vejamos a aplicação da função ``.sum()`` a um *array* unidimensional:

.. code-block:: ipython3

    a = np.linspace(1,20,20).sum()
    print(a)


.. code-block:: text

    210.0
    

E agora 3 maneiras de aplicar a função ``.sum()`` a um array
multidimensional

.. code-block:: ipython3

    # Como se fosse unidimensional
    # aplicando a todos os elementos
    x = np.linspace(1,20,20).reshape((5,4))
    print(x)
    
    s = x.sum()
    print('\n', s)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    
     210.0
    

.. code-block:: ipython3

    # Ao longo do eixo 0
    x = np.linspace(1,20,20).reshape((5,4))
    print(x)
    
    s = x.sum(axis=0)
    print('\n', s)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    
     [ 45.  50.  55.  60.]
    

.. code-block:: ipython3

    # Ao longo do eixo 1
    x = np.linspace(1,20,20).reshape((5,4))
    print(x)
    
    s = x.sum(axis=1)
    print('\n', s)


.. code-block:: text

    [[  1.   2.   3.   4.]
     [  5.   6.   7.   8.]
     [  9.  10.  11.  12.]
     [ 13.  14.  15.  16.]
     [ 17.  18.  19.  20.]]
    
     [ 10.  26.  42.  58.  74.]
    

**Problema: mostrar que a série alternada dos inversos converge para log
2**

.. code-block:: ipython3

    i = np.arange(1,80)
    termos = (-1)**(i+1) * 1/i 
    s = termos.cumsum()
    print(s[:4])


.. code-block:: text

    [ 1.          0.5         0.83333333  0.58333333]
    

.. code-block:: ipython3

    i = np.arange(1,80)
    termos = (-1)**(i+1) * 1/i 
    s = termos.cumsum()
    
    pl.ylim(0.6, 0.8)
    pl.axhline(np.log(2), color='red')
    g = pl.plot(i,s, '-o')



.. image:: 10_scientific_modules_files/10_scientific_modules_51_0.png


.. code-block:: ipython3

    # Agora com 300 termos
    i = np.arange(1, 300)
    termos = (-1)**(i+1) * 1/i 
    s = termos.cumsum()
    
    pl.ylim(0.6, 0.8)
    pl.axhline(np.log(2), color='red')
    g = pl.plot(i,s, alpha=0.7)



.. image:: 10_scientific_modules_files/10_scientific_modules_52_0.png


Exemplos de algumas funcionalidade do ``numpy``.
------------------------------------------------

Geração de números aleatórios. (sub-módulo ``numpy.random``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obter valores aleatórios das seguintes distribuições:

**Poisson** (usada para número de ocorrências durante um intervalo)

:math:`p(x, \lambda) = \frac{e^{-x} \lambda^x}{x!}` com
:math:`x = 0, 1, 2, ...`

**Normal (0,1)**

:math:`f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2 / 2}` com
:math:`x \in [-\infty, \infty]`

.. code-block:: ipython3

    print('20 valores aleatórios da dist. de Poisson')
    print(' com lambda = 3')
    
    x = np.random.poisson(3, 20)
    print(x)


.. code-block:: text

    20 valores aleatórios da dist. de Poisson
     com lambda = 3
    [6 2 0 4 1 9 1 4 2 5 0 3 4 7 7 2 3 5 1 4]
    

.. code-block:: ipython3

    print('5 valores aleatórios da distribuição N(0,1)')
    x = np.random.randn(5)
    print(x)


.. code-block:: text

    5 valores aleatórios da distribuição N(0,1)
    [ 1.04529894 -0.26523157  0.94498444  0.63413472 -1.38915953]
    

**Problema**: "Provar" que a média e a variância da distribuição de
Poisson são ambas iguais a :math:`\lambda`.

.. code-block:: ipython3

    sample = np.random.poisson(3, 100000)
    
    print('Média = ', sample.mean())
    
    print('Variância =', sample.var())


.. code-block:: text

    Média =  2.99868
    Variância = 3.0185382576
    

**Problema**: Mostar numericamente o *Teorema do Limite Central* para
uma distribuição de Poisson.

.. code-block:: ipython3

    # Distribuição de médias de amostras de 2
    sample = np.random.poisson(3, (100000,2) )
    
    means = sample.mean(axis=1)
    
    unique, counts = np.unique(means, return_counts=True)
    
    pl.vlines(unique, [0], counts, color='darkblue')
    g = pl.plot(unique, counts, 'o')



.. image:: 10_scientific_modules_files/10_scientific_modules_61_0.png


.. code-block:: ipython3

    # Distribuição de médias de amostras de 20
    sample = np.random.poisson(3, (100000,20) )
    means = sample.mean(axis=1)
    unique, counts = np.unique(means, return_counts=True)
    
    pl.vlines(unique, [0], counts, color='skyblue')
    g = pl.plot(unique, counts, 'o')



.. image:: 10_scientific_modules_files/10_scientific_modules_62_0.png


Matrizes e álgebra linear
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    A = np.matrix([[1, 2, 3], [2, 1, 6], [1, 7, 4]])
    print('A\n', A)
    B = np.matrix([1,2,3]).T
    print('B\n', B)
    
    C = A * B
    print('\nC = A * B\n', C)


.. code-block:: text

    A
     [[1 2 3]
     [2 1 6]
     [1 7 4]]
    B
     [[1]
     [2]
     [3]]
    
    C = A * B
     [[14]
     [22]
     [27]]
    

.. code-block:: ipython3

    A = np.matrix([[1.0, 2, 3], [2, 1, 6], [1, 7, 4]])
    B = np.matrix([1,2,3]).T
    
    X = np.linalg.solve(A, B)
    print('Solução de A*X = B')
    print(X)


.. code-block:: text

    Solução de A*X = B
    [[-5.]
     [ 0.]
     [ 2.]]
    

``sympy``
---------

Símbolos e álgebra básica
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    from sympy import Symbol
    
    x = Symbol('x')
    y = Symbol('y')
    
    print(x + y + x -y)


.. code-block:: text

    2*x
    

.. code-block:: ipython3

    a = (x+y)**2
    print(a)
    print(a.expand())
    print(a.subs(x, 1).expand())
    print(a.subs(x, 1).expand().subs(y, 1))


.. code-block:: text

    (x + y)**2
    x**2 + 2*x*y + y**2
    y**2 + 2*y + 1
    4
    

Limites
~~~~~~~

.. code-block:: ipython3

    from sympy import Symbol, limit, diff, integrate, sin, oo
    
    x = Symbol('x')
    y = Symbol('y')
    
    print(limit(sin(x)/x, x, 0))
    print(limit(x, x, oo))
    print(limit(1/x, x, oo))


.. code-block:: text

    1
    oo
    0
    

Derivadas e integrais
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ipython3

    print(diff(sin(x), x))
    print(diff(sin(2*x), x))
    print('----------------')
    expr = 2**x + x**2 -3
    print(expr)
    print(diff(expr, x))
    print(diff(expr, x, 3))


.. code-block:: text

    cos(x)
    2*cos(2*x)
    ----------------
    2**x + x**2 - 3
    2**x*log(2) + 2*x
    2**x*log(2)**3
    

.. code-block:: ipython3

    print(integrate(sin(x), x))


.. code-block:: text

    -cos(x)
    
