def f(a, b, s, n):
    if a + s + b >= 71: return n % 2 == 0
    if n == 0: return 0
    h = [f(a+3, b, s, n-1), f(a, b+3, s, n-1), f(a, b, s+3, n-1), f(a*2, b, s, n-1), f(a, b*2, s, n-1), f(a, b, s*2, n-1)]
    if (n-1) % 2 == 0: return any(h)
    if (n-1) % 2 != 0: return all(h)

print([s for s in range(1, 59) if f(7, 5, s, 2)])
print([s for s in range(1, 59) if not f(7, 5, s, 1) and f(7, 5, s, 3)])
print([s for s in range(1, 59) if not f(7, 5, s, 2) and f(7, 5, s, 4)])