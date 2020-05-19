
# `sympy`


### Símbolos e álgebra básica

<div class="python_box">
``` python3
from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

print(x + y + x -y)
```
</div>

```
2*x
```

<div class="python_box">
``` python3
a = (x+y)**2
print(a)
print(a.expand())
print(a.subs(x, 1).expand())
print(a.subs(x, 1).expand().subs(y, 1))
```
</div>

```
(x + y)**2
x**2 + 2*x*y + y**2
y**2 + 2*y + 1
4
```

### Limites

<div class="python_box">
``` python3
from sympy import Symbol, limit, diff, integrate, sin, oo

x = Symbol('x')
y = Symbol('y')

print(limit(sin(x)/x, x, 0))
print(limit(x, x, oo))
print(limit(1/x, x, oo))
```
</div>

```
1
oo
0
```

### Derivadas e integrais

<div class="python_box">
``` python3
print(diff(sin(x), x))
print(diff(sin(2*x), x))
print('----------------')
expr = 2**x + x**2 -3
print(expr)
print(diff(expr, x))
print(diff(expr, x, 3))
```
</div>

```
cos(x)
2*cos(2*x)
----------------
2**x + x**2 - 3
2**x*log(2) + 2*x
2**x*log(2)**3
```

<div class="python_box">
``` python3
print(integrate(sin(x), x))
```
</div>

```
-cos(x)
```
