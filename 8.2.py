from itertools import *
c = 0
for i in product('абвг', repeat=6):
    s = ''.join(i)
    if s[0] != 'а' and s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4] and s[4] != s[5]:
        c += 1
print(c)