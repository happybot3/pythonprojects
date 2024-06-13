from itertools import*
def f(x):
    p = 3 <= x <= 38
    q = 21 <= x <= 57
    a = a1 <= x <= a2
    return (q <= p) <= (not a)

ox = [i/4 for i in range(3*4, 58*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(max(lst))