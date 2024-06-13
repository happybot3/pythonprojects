f = open('9.10.txt')

c = 0
for i in f:
    s = list(map(int, i.split()))
    if s[0] - s[1] >= 5 and (0 <= s[4] <= 45 or 315 <= s[4] <= 360):
        c += 1
print(c)