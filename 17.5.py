f = open('17.5.txt')
lst = [int(x) for x in f]
ans = []
c25 = max([x for x in lst if abs(x) % 100 == 25])
for i in range(1, len(lst)-1):
    if ((1000 <= lst[i-1] <= 9999) + (1000 <= lst[i] <= 9999) + (1000 <= lst[i+1] <= 9999)) <= 2:
        if lst[i-1] + lst[i] + lst[i+1] <= c25:
            ans.append(lst[i-1] + lst[i] + lst[i+1])
print(len(ans), max(ans))

