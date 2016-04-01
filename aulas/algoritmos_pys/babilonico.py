a = 2.0

x = 1.0
for i in range(100):
    print x
    novo = 0.5 * (x + a/x)
    if abs(novo - x) < 1e-10:
        x = novo
        break
    x = novo

print x