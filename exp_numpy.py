import numpy as np
import matplotlib.pyplot as plt

pK1 = 2.3
pK2 = 9.6
Gt  = 0.1 # M

pH = np.linspace(0, 14, 14000)
f1 = 10.0**(pH - pK1)
f2 = 10.0**(pH - pK2)

Gplus = Gt / (1 + f1 + f1*f2)
Gzero = f1 * Gplus
Gminus = f2 * Gzero
nOH = Gzero + 2 * Gminus

plt.plot(pH, Gplus)
plt.plot(pH, Gzero)
plt.plot(pH, Gminus)

plt.ylabel('concentration')
plt.xlabel('$pH$')
plt.legend(('$G^+$','$G^0$', '$G^-$'))
plt.title('Species distribution')
plt.show()

plt.plot(nOH, pH)

plt.ylabel('$pH$')
plt.xlabel('$nOH^{-}$')
plt.grid()
plt.show()