from itertools import*
c= 0
for i in permutations('левий', r = 5):
    s = ''.join(i)
    if s[0] != 'й' and 'еи' not in s:
        c += 1
print(c)