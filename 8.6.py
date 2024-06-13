from itertools import *

lst = []
for i in permutations('амфибрахий'):
    s= ''.join(i)
    if s[4] == 'б' and s[5] == 'р':
        lst.append(s)
print(len(set(lst)))
