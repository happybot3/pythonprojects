def f(x, y, A):
    return (x + 2*y > A) or (y < x) or (x < 30) 
lst = []
for A in range(0,300):
    if all(f(x, y, A) == 1 for x in range(0,300) for y in range(0,300)):
        print(A)
