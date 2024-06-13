def d(n, m):
    return n%m == 0

def f(x, a):
    return (a + x < 123) <= (d(x, 5) <= (not d(x, 7)))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break