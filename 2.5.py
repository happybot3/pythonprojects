from itertools import * 
def f(x, y, z, w):
    return  (x and (not y)) or (x == z) or w

for i in product([0, 1], repeat = 4):
    table = [(i[0], i[1], 0, 1), (1, 0, i[2], 1), (1, 1, 0, i[3])]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            if len(table) == len(set(table)):
                print(p)

