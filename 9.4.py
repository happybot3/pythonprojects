from math import*
f = open('9.4.txt')
n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    if prod(lst[:-1]) % lst[-1] == 0:
        n += 1
print(n)
