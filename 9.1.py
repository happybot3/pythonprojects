f = open('9.1.txt')

n = 0
for i in f:
    lst = sorted(map(int, i.split()))
    pov = [x for x in lst if lst.count(x) == 2] 
    nepov = [x for x in lst if lst.count(x) == 1]
    if len(pov) == 4 and len(nepov) == 2 and ((lst[0] + lst[-1]) / 2) < (sum(lst[1:5]) / 4):
        n += 1
print(n)
