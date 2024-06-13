n = 49**6 * 7**19 - 7**9 - 21
base = 7
lst = []
while n > 0:
    lst.append(n % base)
    n = n // base
print(lst.count(6))
