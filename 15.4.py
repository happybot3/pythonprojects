def f(a, x, y):
    return (7*y + 5*x < 1000) or (x < y) or (a < x)

for a in range(300):
    if all(f(a, x, y) for x in range(300) for y in range(300)):
        print(a)
        