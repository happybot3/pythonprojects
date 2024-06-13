for N in range(2, 100):
    n = bin(N)[2:]
    su = n.count('1')
    if su % 2 == 0:
        n = n + n[-2:]
    else:
        n = n + str(int(not(int(n[-2])))) + str(int(not(int(n[-1]))))
    r = int(n, 2)
    if r > 154:
        print(N)
        break

