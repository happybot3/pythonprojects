def f(a, x, y):
    return (12*x + 2*y > 56) or (x > 2*y) or (5*x + y < a)

for a in range(300):
    if any(f(a, x, y) == 0 for x in range(300) for y in range(300)):
        print(a)
