from sys import *
setrecursionlimit(10000)

def f(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + f(n - 1)

print(f(2024) - f(2022))
