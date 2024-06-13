from sys import *

setrecursionlimit(10000)

from functools import *

@lru_cache
def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return f(n + 1) - f(n + 2) + 7

print(f(15) - f(24))
