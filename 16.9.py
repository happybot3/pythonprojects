from sys import *
setrecursionlimit(100000)
def f(n):
    if n >= 2022: return n
    if n < 2022: return f(n+5) + 7

print(f(45) - f(49))
