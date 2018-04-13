
Instalação de software
======================

Distribuições científicas da linguagem Python
---------------------------------------------

A linguagem Python tem uma *distribuição* oficial que pode ser obtida a
partir do portal da linguagem
`www.python.org <http://www.python.org>`__.

Esta distribuição contem mais de uma centena de módulos que aumentam a
funcionalidade da linguagem base. Esta funcionalidade fica acessível
pela disponibilização de novas funções via comandos ``import``. Os
módulos não precisão de ser instalados, eles vêm com a distribuição e
constituem a chamada *biblioteca padrão* da linguagem Python.

Para as aulas da UC de Bioquímica Computacional, em que se procura
mostrar as vertentes de cálculo científico vetorial, capacidades
gráficas e tratamento de dados estruturados em tabelas, são necessários
**módulos adicionais** a instalar "sobre" a distribuição oficial.

Embora pudessem ser baixados dos respetivos sites, estes módulos
adicionais já foram integrados em distribuições alternativas da
linguagem Python orientados para o uso da linguagem em contextos de
ciência ou de engenharia.

**É de toda a conveniência que seja instalada uma destas distribuições
"científicas"**. Existem várias, mas aconselhamos a distribuição
**Anaconda** da empresa *Continuum Analytics*. Em alternativa, existe
uma versão "lite" da distribuição Anaconda designada por **Miniconda**.

Instalação da distribuição Anaconda ou Miniconda
------------------------------------------------

Anaconda (fortemente aconselhada):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basta correr o instalador, que pode ser baixado a partir de:

https://www.continuum.io/downloads

Deve-se escolher a última versão do Python (3.6) e o instalador
apropriado ao sistema operativo do computador (win 32 bit, win 64 bit,
OS ou Linux).

A distribuição é "grande" (mais de 1 GB), aconselha-se a instalação
"para o utilizador".

Miniconda (para os que têm problemas de falta de espaço em disco):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obter e correr o instalador do Miniconda, que pode ser baixado a partir
de :

https://conda.io/miniconda.html

Deve-se escolher a última versão do Python (3.6) e o instalador
apropriado ao sistema operativo do computador (win 32 bit, win 64 bit,
OS ou Linux).

No final da instalação deve ser executado, numa *linha de comando do
sistema operativo*:

::

    conda install six numpy sympy scipy matplotlib jupyter pandas
