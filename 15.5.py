from itertools import*
def f(x):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = a1 <= x <= a2
    return (p == a) <= (not a)

ox = [i/4 for i in range(5*4, 31*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        lst.append(a2-a1)
print(max(lst))