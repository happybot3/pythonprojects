def f(k, base):
    l = []
    while k > 0:
        l.append(k % base)
        k = k // base
    return l[::-1]

lst = []
for i in range(1, 1000):
    N = i
    n = f(N, 3)
    if N % 3 == 0:
        n = n + [n[-2]] + [n[-1]]
    else:
        n = n + f((N % 3) * 5, 3)
    n = ''.join(map(str, n))
    r = int(n, 3)
    if r > 133:
        print(r)
        break