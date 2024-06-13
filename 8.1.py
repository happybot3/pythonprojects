from itertools import *

lst = []
for i in permutations('КЛАБХАУС', r=8):
    s = ''.join(i)
    if  s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4] and s[4] != s[5] and s[5] != s[6] and s[6] != s[7]:
        lst.append(s)
print(len(set(lst)))

