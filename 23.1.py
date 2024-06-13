def f(x, fin):
    if x > fin or x % 5 == 0: return 0
    if x == fin: return 1
    return f(x+1, fin) + f(x+3, fin) + f(x*3, fin)

print(f(1, 49))