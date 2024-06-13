from itertools import*

c = 0
k = sorted('тимашевск')[::-1]
for i in product(k, repeat = 5):
    s =''.join(i)
    if s == s[::-1] and s[2] in 'тмшвск' and s[0] in 'иае' and s[1] in 'иае' and s[3] in 'иае' and s[4] in 'иае' :
        print(c)
    c += 1