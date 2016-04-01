a = 2.0

x = 1.0
for i in range(20):
    print x
    x = 0.5 * (x + a/x)

print x
