from math import* 
f = open('9.2.txt')
n = 0
for i in f:
    a = sorted(map(int, i.split()))
    pov = [x for x in a if a.count(x) > 1]
    if len(pov) >= 2 and a[1] != a[3] and a[2] != a[3] and (2*a[0]**2) > (a[1] * a[2]):
        n += 1
print(n)