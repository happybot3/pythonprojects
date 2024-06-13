from itertools import*
def f(x):
    p = 8 <= x <= 39
    q = 23 <= x <= 58
    a = a1 <= x <= a2
    return (p <= a) <= (q or a)

ox = [i/4 for i in range(8*4, 59*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(min(lst))