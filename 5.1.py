l = []
for i in range(1, 1000):    
    N = i
    n = bin(N)[2:]
    if n.count('1') % 2 == 0:
        n = '1' + n + '00'
    else:
        n = '11' + n
    r = int(n, 2)
    if r >= 412:
        l.append(i)
print(min(l))

