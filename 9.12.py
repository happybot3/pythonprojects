f = open('9.12.txt')
c = 0
for i in f:
    lst = list(map(int, i.split()))
    if len(set(lst)) == 3 and max(lst) < (sum(lst) - max(lst)):
        c += 1
print(c)
