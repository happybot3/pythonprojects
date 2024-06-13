from itertools import*
def f(x):
    p = 4 <= x <= 15
    q = 12 <= x <= 20
    a = a1 <= x <= a2
    return (p and q) <= a

ox = [i/4 for i in range(4*4, 21*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(min(lst))