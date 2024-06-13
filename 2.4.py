from itertools import*

def f(x, y, z, w):
    return (x or (not y)) and (not(x == z)) and (not w)

for i in product([0, 1], repeat = 4):
    table = [(0, 0, 1, i[0]), (0, i[1], 0, 1), (i[2], 1, 1, i[3])]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
            if len(set(table)) == len(table):
                print(p)