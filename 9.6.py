f = open('9.6.txt')
n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    if (lst[0] + lst[3] == lst[2] + lst[1]) and (lst[3] - lst[0]) < ((lst[2] + lst[1]) - lst[3]):
        n += 1
print(n)