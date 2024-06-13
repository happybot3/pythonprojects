def f(a, x, y):
    return ((3*x + 2*y) > 25) or (x > 2*y) or ((x + 4*y) < a)

for a in range(300):
    if any(f(a, x, y) == 0 for x in range(0, 300) for y in range(0, 300)):
        print(a)