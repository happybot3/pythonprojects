from itertools import *

lst = []
c = 1 
for i in permutations('водопад'):
    s = ''.join(i)
    if 'оо' not in s and 'ао' not in s and 'оа' not in s:
        lst.append(s)
    c += 1
print(len(set(lst)))
