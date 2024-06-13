
lst = []
for i in range(1, 1000):
    N = i
    n = bin(N)[2:]
    if n.count('1') > n.count('0'):
        n = n + '0'
    else:
        n = n + '11'
    r = int(n, 2)
    if r > 2019:
        lst.append(i)
print(min(lst))

