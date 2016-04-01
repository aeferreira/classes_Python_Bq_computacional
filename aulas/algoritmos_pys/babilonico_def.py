
def babilonico(a):
    x = 1.0
    for i in range(100):
        print x
        novo = 0.5 * (x + a/x)
        if abs(novo - x) < 1e-10:
            return novo
        x = novo
    return x

print babilonico(2.0)