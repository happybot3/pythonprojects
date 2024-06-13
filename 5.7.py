lst = []
for i in range(4,1000):
    N = i
    n = bin(N)[2:]
    if N % 3 == 0:
        n = n + n[-3] + n[-2] + n[-1]
    else:
        n = n + bin((N % 3) * 3)[2:]
    r = int(n, 2)
    if r < 170:
        lst.append(r)
print(max(lst))

