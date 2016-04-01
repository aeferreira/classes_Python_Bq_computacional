from matplotlib import pyplot as pl
from numpy import linspace

import matplotlib as mpl
mpl.rcParams['text.usetex'] = False

def f(x):
    return x**3 + 2*x**2 -1

def df(x):
    return 3*x**2 + 4*x

x = linspace(0, 2, 500)
y = f(x)

pl.plot(x, y, color='darkblue', linewidth=2)
pl.plot([0,2], [0,0], 'k-')
pl.ylim(-4,10)
pl.xlim(0,2)

x1 = 1.5
f1 = f(x1)

x2 = x1 - f(x1) / df(x1)
f2 = 0

pl.plot([x1, x1, x2], [0, f1, 0], 'g-')
pl.plot([x1, x1+1], [f1, df(x1)*1+f1], 'g-')

pl.plot([x1, x1, x2], [0, f1, 0], 'ro')
pl.text(x1-0.03, -0.6, '$x_1$', fontsize=16)
pl.text(x2-0.03, -0.6, '$x_2$', fontsize=16)
pl.text(x2-0.2, -2, r"$x_2 = x_1 - f(x_1) / f \mathrm{\,}' (x_1)$", fontsize=20)
pl.show()
