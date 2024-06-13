from itertools import *
c = 0
for i in product('01234567', repeat = 5):
    s = ''.join(i)
    for n in range(0, 4):
        if s[0] != '0'  and s.count('1') == 0 and len(set(s)) == 5 and (int(s[n]) % 2) != (int(s[n+1]) % 2):
            c += 1
print(c)

