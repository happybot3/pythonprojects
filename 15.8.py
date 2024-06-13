from itertools import*
def f(x):
    p = 10 <= x <= 15
    q = 10 <= x <= 20
    r = 5 <= x <= 15
    a = a1 <= x <= a2
    return (a <= p) == (q <= r)

ox = [i/4 for i in range(5*4, 21*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(min(lst))