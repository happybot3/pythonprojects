from itertools import*
def f(a, b, c, d):
    return ((a * b) <= c) * ((b * c) <= d)

for i in product([0, 1], repeat = 5):
    table = [(i[0], 1, 1, 1), (i[1], 1, 0, 1), (1, 1, 1, i[2]), (i[3], 1, 1, i[4])]
    for p in permutations('abcd'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0, 0]:
            if len(table) == len(set(table)):
                print(p)