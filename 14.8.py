n = 4*8**3032 + 3*16**1956 + 870
l = []
while n > 0:
    l.append(n%7)
    n = n // 7
print(l.count(3)-l.count(1))

