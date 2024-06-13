lst = []
for i in range(1,1000):
    N = i
    n = bin(N)[2:]
    n = n + str(n.count('1') % 2)
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if N % 2 == 0:
        n = n + '1'
    else:
        n = n + '0'
    r = int(n, 2)
    if r > 204:
        lst.append(r)
print(min(lst))
