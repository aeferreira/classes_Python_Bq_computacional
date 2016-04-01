def bissect(f, a, b):
    epsilon, epsilonf = 1e-6, 1e-10
    fa, fb = f(a), f(b)
    while abs(b-a) > epsilon:
        xm = (a+b)/2.0
        fm = f(xm)
        if abs(fm) < epsilonf:
            return xm, fm
        if fm*fa > 0.0: 
            a,fa = xm,fm
        else:
            b,fb = xm,fm
    return a, f(a)

def f(x):
    return x**3 -2

x, fx = bissect(f, 1, 2)

print "Root found:"
#print x, fx
print "x = {}, f(x) = {:9.7f}".format(x,fx)

