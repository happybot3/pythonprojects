l = []
for i in range(1, 1000):
    N =  i
    n = bin(N)[2:]
    if n.count('1') % 4 == 0:
        n = '10' + n
    else:
        n = '11' + n 
    if n[-1] == '1':
        n = n + '0'
    else:
        n = n + '1'
    r = int(n, 2)
    if r <= 250:
        l.append(i)
print(max(l))