def bissect(f, a, b):
    epsilon, epsilonf = 1e-6, 1e-10
    fa, fb = f(a), f(b)
    history = []
    while abs(b-a) > epsilon:
        history.append([a,b,fa,fb])
        xm = (a+b)/2.0
        fm = f(xm)
        if abs(fm) < epsilonf:
            return xm, fm, history
        if fm*fa > 0.0: 
            a,fa = xm,fm
        else:
            b,fb = xm,fm
    return a, f(a), history

def f(x):
    return x**3 -2

x, fx, h = bissect(f, 1, 2)

print "Root found:"
print "x = {}, f(x) = {:9.7f}".format(x,fx)

print 'history:'
print 'a       b       f(a)      f(b)'

for a,b,fa,fb in h:
    print "{0:7.5f} {1:7.5f} {2:8.6f} {3:8.6f}".format(a,b,fa,fb)
