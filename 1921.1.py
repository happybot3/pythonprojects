def f(s, n):
    if s >= 96: return n%2 == 0
    if n == 0: return 0
    if s % 2 == 0:
        h = [f(s + s/2, n-1),f(s + 1, n-1)]
    if s % 3 == 0:
        h = [f(s + s/3, n-1),f(s + 1, n-1)]
    if s % 3 != 0 and s % 2 != 0:
        h = [f(s*2, n-1), f(s + 1, n-1)]
    if (n-1)%2 == 0: return any(h)
    else: return all(h)

print([s for s in range(1, 96) if not f(s, 2) and f(s, 4)])
