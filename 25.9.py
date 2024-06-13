def f(n):
    lst = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            lst.append(i)
            lst.append(n//i)
    return len(set(lst))

ch = 0
d = 0
for i in range(568023, 569231):
    if f(i) > d:
        d = f(i)
        ch = i
print(d, ch)
