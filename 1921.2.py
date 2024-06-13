def f(a, s, n):
    if a+s >= 259: return n%2 == 0
    if n == 0: return 0
    h = [f(a+1, s, n-1),f(a, s+1, n-1),f(a*2, s, n-1),f(a, s*2, n-1)]
    if (n-1)%2 == 0: return any(h)
    if (n-1)%2 != 0: return all(h)

print([s for s in range(1,242) if f(17, s, 2)])
print([s for s in range(1,242) if not f(17, s, 1) and f(17, s, 3)])
print([s for s in range(1,242) if not f(17, s, 2) and f(17, s, 4)])
