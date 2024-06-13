f = open('9.7.txt')
n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    pov = [ x for x in lst if lst.count(x) == 2]
    if len(pov) == 2 and ((lst[0] + lst[5]) / 2) > ((lst[1] + lst[2] + lst[3] + lst[4]) / 4):
        n += 1
print(n)