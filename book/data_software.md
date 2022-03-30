# Instalação de software

Para acompanhar as aulas da UC de Bioquímica Computacional será necessário instalar:

- Uma *distribuição* apropriada da linguagem Python
- Um editor de texto adequada para programação (tipo IDE)

Quanto à primeira, aconselha-se uma distribuição da linguagem Python para programação "científica".
Não existem muitas opções, por isso é fácil escolher. Aconselha-se a distribuição
[*Anaconda Individual Edition*](https://www.anaconda.com/distribution/).

Já para o editor de texto, a variedade é grande e a escolha é muitas vezes ditada pelo gosto pessoal após experimentar várias alternativas. Aconselha-se a instalação do
[*Visual Studio Code*](https://code.visualstudio.com/) da *Microsoft*. 

## Distribuições científicas da linguagem Python

A linguagem Python tem uma *distribuição* oficial que poderia ser obtida
a partir do portal da linguagem [www.python.org](http://www.python.org).

No entanto, para as aulas da UC de Bioquímica Computacional, em que se procura
mostrar as vertentes de cálculo científico, capacidades
gráficas e tratamento de dados estruturados, são necessários
**módulos adicionais** a instalar "sobre" a distribuição oficial.

Embora pudessem ser baixados dos respetivos *sites*, estes módulos
adicionais já foram integrados em distribuições alternativas da
linguagem Python orientados para o uso da linguagem em contextos de
ciência ou de engenharia.

**É de toda a conveniência que seja instalada uma destas distribuições
"científicas"**. Existem várias, mas aconselhamos a distribuição
**Anaconda** da empresa *Anaconda Inc*. Em alternativa, existe uma
versão "lite" da distribuição Anaconda designada por **Miniconda**.

## Instalação da distribuição Anaconda ou Miniconda

### Anaconda (aconselhada):

Instruções pormenorizadas sobre a instalação, com alguns conselhos úteis, 
podem ser lidas a partir de:

<https://docs.anaconda.com/anaconda/install/>

seguindo para a página de instrucões adequadas ao tipo de computador (Windows, MacOS ou Linux).

Em geral, basta correr o instalador, que pode ser baixado a partir de:

<https://www.anaconda.com/distribution/>

Deve-se escolher a última versão do Python (3.8 ou 3.9) e o instalador
apropriado ao sistema operativo do computador (Windows, MacOS ou Linux).

A distribuição é "grande" (mais de 1 GB), aconselha-se a instalação
"para o utilizador".

Um dos passos finais das instruções de instalação é a **verificação** de que
a instalação foi bem sucedida. **É importante realizar este passo**.

Por exemplo, em computadores com Windows 10, as instruções estão em 

<https://docs.anaconda.com/anaconda/install/windows/>

e a verificação é o ponto 15.

**NOTA**: não é necessário instalar o PyCharm. Esta é uma opção durante a instalação.

### Miniconda (para os que têm problemas de falta de espaço em disco):

Obter e correr o instalador do Miniconda, que pode ser baixado a partir
de:

<https://conda.io/en/latest/miniconda.html>

Deve-se escolher a última versão do Python (3.9) e o instalador
apropriado ao sistema operativo do computador (Windows, MacOS ou Linux).

No final da instalação deve ser executado, na *linha de comando* apropriada
(*Terminal* em Mac, *Anaconda Prompt* em Windows ou numa shell em Linux):

    conda install numpy sympy scipy matplotlib jupyter pandas


## Instalação do Visual Studio Code (VSCode)

A instalação é simples. Basta baixar e correr o instalador:

<https://code.visualstudio.com/Download>

Nota: aconselha-se o *User installer* em Windows e Linux

```{admonition} Notas
:class: note
- A plataforma **Jupyter** está incluída na instalação da Anaconda
- A **extensão Python** para o *VSCode* é automaticamente instalada na primeira tentativa de salvar um programa em Python (desde que o nome acabe em `.py`)
```
