from itertools import*
def f(x):
    p = 10 <= x <= 29
    q = 13 <= x <= 18
    a = a1 <= x <= a2
    return (a <= p) or q

ox = [i/4 for i in range(10*4, 30*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(max(lst))