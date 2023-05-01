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

# Módulo `sympy`


## Símbolos e álgebra básica

```{code-cell} ipython3
from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

print(x + y + x -y)
```


```{code-cell} ipython3
a = (x+y)**2
print(a)
print(a.expand())
print(a.subs(x, 1).expand())
print(a.subs(x, 1).expand().subs(y, 1))
```


## Limites

```{code-cell} ipython3
from sympy import Symbol, limit, diff, integrate, sin, oo

x = Symbol('x')
y = Symbol('y')

print(limit(sin(x)/x, x, 0))
print(limit(x, x, oo))
print(limit(1/x, x, oo))
```


## Derivadas e integrais

```{code-cell} ipython3
print(diff(sin(x), x))
print(diff(sin(2*x), x))
print('----------------')
expr = 2**x + x**2 -3
print(expr)
print(diff(expr, x))
print(diff(expr, x, 3))
```


```{code-cell} ipython3
print(integrate(sin(x), x))
```

