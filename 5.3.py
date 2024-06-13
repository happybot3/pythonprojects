lst = []
for i in range(1,1000):
    N = i
    n = bin(N)[2:]
    if n.count('1') % 2 == 1:
        n = n + '11'
    else:
        n = '11' + n
    r = int(n, 2)
    if r > 102:
        lst.append(i)
print(min(lst))
