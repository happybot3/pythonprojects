from itertools import*
def f(x, y, z, w):
    return (not(w <= (not(x <= y)))) and ((not x) <= ((not y) == z))

for i in product([0, 1], repeat = 5):
    table = [(i[0], 1, 1, 1), (i[1], i[2], 0, 0), (0, i[3], i[4], 0)]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 1, 1]:
            if len(table) == len(set(table)):
                print(p)
