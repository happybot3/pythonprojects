def f(n):
    lst = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return sorted(set(lst))

for i in range(312614, 312652):
    ans = f(i)
    if len(ans) == 6:
        print(ans)