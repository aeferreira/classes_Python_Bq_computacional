# Example: Simulation of the acid-base changes in an amino-acid solution
from numpy import linspace
import matplotlib.pyplot as pl

pK1, pK2, Gt = 2.3, 9.6, 0.1

pH = linspace(0, 14, 14000)
f1 = 10.0**(pH - pK1)
f2 = 10.0**(pH - pK2)
Gplus = Gt / (1 + f1 + f1*f2)
Gzero = f1 * Gplus
Gminus = f2 * Gzero
nOH = Gzero + 2 * Gminus

pl.plot(pH, Gplus, 'r-')
pl.plot(pH, Gzero, color='darkgreen')
pl.plot(pH, Gminus, color='darkblue')
pl.ylabel('concentration')
pl.xlabel('pH')
pl.legend(('$G^+$','$G^0$', '$G^-$'))
pl.title('Species distribution')
pl.figure()
pl.plot(nOH, pH, color='teal')
pl.ylabel('pH')
pl.xlabel('$nOH^{-}$')
pl.grid()
pl.show()