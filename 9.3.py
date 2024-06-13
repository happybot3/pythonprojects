f = open('9.3.txt')
n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    ch = [x for x in lst if x % 2 == 0]
    nech = [x for x in lst if x % 2 == 1]
    if len(set(lst)) == 5 and len(ch) < len(nech) and sum(ch) > sum(nech):
        n += 1
print(n)

