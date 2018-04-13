
Example: Simulation of the acid-base changes in an amino-acid solution
======================================================================

Here we make a simple simulation of the changes in pH and charge
distribution of an amino acid in solution.

Focus will be on Glycine first, but the derivarion and the analysis can
easily be applied to the other amino acids if the values of the pKa are
known.

Derivation of the relevant equations
------------------------------------

We first seek to calculate the charge distribution of glycine in
solution as a function of pH.

At any pH, we can find glycine as a mixture of three species:

:math:`NH^{+}_3 - CH_2 - COOH` the positive form, here represented by
:math:`G^+`.

:math:`NH_2 - CH_2 - COOH` the neutral form, here represented by
:math:`G^0`.

:math:`NH_2 - CH_2 - COO^{-}` the negative form, here represented by
:math:`G^-`.

Total of different forms is constant:

:math:`G^+ + G^0 + G^- = G_{tot}`

There are two equilibria

:math:`pH = pK1 + log_{10} \left( \frac{G^0}{G^+} \right)`

:math:`pH = pK2 + log_{10} \left( \frac{G^-}{G^0} \right)`

We need to calculate all the forms of the amino acid as a function of
pH.

Let's make

:math:`f1 = \frac{G^0}{G^+}` and :math:`f2 = \frac{G^-}{G^0}`

Then

:math:`f1 = 10^{pH - pK1}` and :math:`f2 = 10^{pH - pK2}`

Now, using these in the total amino acid conservation equation,

:math:`G^+ + G^+ f1 + G^+ f1 f2 = G_{tot}`

or

:math:`G^+ = \frac{G_{tot}}{1 + f1 + f1f2}`

And, by definition of :math:`f1` and :math:`f2`,

:math:`G^0 = G^+ f1`

:math:`G^- = G^0 f2`

The sequence of calculations is then

:math:`pH \longrightarrow f1, f2 \longrightarrow G^+ \longrightarrow G^0 \longrightarrow G^-`

An additional problem is the calculation of the amount of :math:`OH^-`
than must be used to drive the solution to a given pH, starting from a
very low pH solution

This is simply

:math:`nOH^- = nG^0 + 2 nG^-`

Analysis
--------

Computation
~~~~~~~~~~~

Make the necessary imports

.. code:: ipython3

    from numpy import linspace

Use derived equations to compute species distribution and the amount of
base necessary to change the solution into a given pH value.

.. code:: ipython3

    pK1 = 2.3
    pK2 = 9.6
    Gt  = 0.1 # M
    
    pH = linspace(0, 14, 14000)
    f1 = 10.0**(pH - pK1)
    f2 = 10.0**(pH - pK2)
    
    Gplus = Gt / (1 + f1 + f1*f2)
    Gzero = f1 * Gplus
    Gminus = f2 * Gzero
    nOH = Gzero + 2 * Gminus

Plots
~~~~~

Obtain a plot of the distribution of the three different species of the
amino acid as a function of pH.

.. code:: ipython3

    %matplotlib inline 
    # This is to be used in IPython/Jupyter notebooks
    # This makes plots appear "inline" as part of cell's outputs.

.. code:: ipython3

    import matplotlib.pyplot as pl
    
    pl.plot(pH, Gplus)
    pl.plot(pH, Gzero)
    pl.plot(pH, Gminus)
    
    pl.ylabel('concentration')
    pl.xlabel('$pH$')
    pl.legend(('$G^+$','$G^0$', '$G^-$'))
    t = pl.title('Species distribution')



.. image:: 12_scipy_pH_files/12_scipy_pH_20_0.png


Plot also the amount of base necessary to change the pH of the solution,
but **exchange the x and y axis**, so that it looks like we are
titrating the solution.

.. code:: ipython3

    pl.plot(nOH, pH)
    
    pl.ylabel('$pH$')
    pl.xlabel('$nOH^{-}$')
    pl.grid()



.. image:: 12_scipy_pH_files/12_scipy_pH_22_0.png

