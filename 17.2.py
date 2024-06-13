f = open('17.2.txt')
lst = [int(x) for x in f]
ind = []
for i in range(1, len(lst)-1):
    a, b, c = lst[i-1], lst[i], lst[i+1]
    if b < a and c > b:
        ind.append(lst[i])
print(len(ind), max(ind)) 

