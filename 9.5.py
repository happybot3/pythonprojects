f = open('9.5.txt')
n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    sr = (lst[0] + lst[-1]) / 2
    if sr in lst:
        n += 1
print(n)