f = open('9.11.txt')

n = 0
for i in f:
    lst = list(map(int, i.split()))
    ch = [x for x in lst if x % 2 == 0]
    nech = [x for x in lst if x % 2 == 1]
    if sum(nech) > sum(ch):
        n += 1
print(n)

