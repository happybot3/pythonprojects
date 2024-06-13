f = open ('9.9.txt')
n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    pov = [x for x in lst if lst.count(x) == 2]
    nepov = [x for x in lst if lst.count(x) == 1]
    if len(nepov) != 0:
        if len(pov) == 2 and (sum(nepov) / len(nepov)) <= sum(pov):
            n += 1
print(n)
