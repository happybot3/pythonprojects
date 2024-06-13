s = 4*625**1920 + 4*125**1930 - 4*25**1940 - 3*5**1950 - 1960
lst = []
while s > 0:
    lst.append(s%5)
    s = s // 5
print(lst.count(0))