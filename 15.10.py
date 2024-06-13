from itertools import*
def f(x):
    p = 10 <= x <= 21
    q = 13 <= x <= 38
    r = 18 <= x <= 25
    a = a1 <= x <= a2
    return (not(q <= (p or r))) <= ((not a) <= (not q))

ox = [i/4 for i in range(10*4, 39*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(min(lst))