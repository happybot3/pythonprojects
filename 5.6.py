lst = []
for i in range(1,1000):
    N = i
    n = bin(N)[2:]
    if N % 2 == 0:
        n1 = n + '0'
    else:
        n1 = n + '1'
    if n.count('1') % 2 == 0:
        n1 = n1 + '0'
    else: 
        n1 = n1 + '1'
    r = int(n1, 2)
    if r > 2023:
        lst.append(r)
print(min(lst))
