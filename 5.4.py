lst = []
for i in range(1,1000):
    N = i
    n = bin(N)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    r = int(n, 2)
    if r > 89:
        lst.append(i)
print(min(lst))