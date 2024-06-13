k = int(input())
if k % 2 == 1:
    alive = k // 2 + 1
else:
    alive = k / 2
print(alive)