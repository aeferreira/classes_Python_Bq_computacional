
Instalação de software
======================

Distribuições científicas da linguagem Python
---------------------------------------------

A linguagem Python tem uma *distribuição* oficial que poderia ser obtida a
partir do portal da linguagem
`www.python.org <http://www.python.org>`__.

Para as aulas da UC de Bioquímica Computacional, em que se procura
mostrar as vertentes de cálculo científico vetorial, capacidades
gráficas e tratamento de dados estruturados em tabelas, são necessários
**módulos adicionais** a instalar "sobre" a distribuição oficial.

Embora pudessem ser baixados dos respetivos *sites*, estes módulos
adicionais já foram integrados em distribuições alternativas da
linguagem Python orientados para o uso da linguagem em contextos de
ciência ou de engenharia.

**É de toda a conveniência que seja instalada uma destas distribuições
"científicas"**. Existem várias, mas aconselhamos a distribuição
**Anaconda** da empresa *Anaconda Inc*. Em alternativa, existe
uma versão "lite" da distribuição Anaconda designada por **Miniconda**.

Instalação da distribuição Anaconda ou Miniconda
------------------------------------------------

Anaconda (fortemente aconselhada):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basta correr o instalador, que pode ser baixado a partir de:

https://www.anaconda.com/distribution/

Deve-se escolher a última versão do Python (3.7) e o instalador
apropriado ao sistema operativo do computador (Windows, MacOS ou Linux).

A distribuição é "grande" (mais de 1 GB), aconselha-se a instalação
"para o utilizador".

Miniconda (para os que têm problemas de falta de espaço em disco):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obter e correr o instalador do Miniconda, que pode ser baixado a partir
de :

https://conda.io/en/latest/miniconda.html

Deve-se escolher a última versão do Python (3.7) e o instalador
apropriado ao sistema operativo do computador (Windows, MacOS ou Linux).

No final da instalação deve ser executado, numa *linha de comando do
sistema operativo*:

::

    conda install numpy sympy scipy matplotlib jupyter pandas
