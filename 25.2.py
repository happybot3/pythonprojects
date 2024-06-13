def f(n):
    lst = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return sorted(set(lst))

for i in range(123456789, 223456790):
    i == round(i**0.5)**2