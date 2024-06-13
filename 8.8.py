from itertools import *

lst = []
for i in permutations('спортлото'):
    s = ''.join(i)
    if 'оо' in s and 'ооо' not in s:
        lst.append(s)
print(len(set(lst)))
