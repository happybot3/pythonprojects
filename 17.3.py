f = open('17.1.txt')
lst = [int(x) for x in f]
ans = []
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        ans.append(abs(lst[i] - lst[i-1]))
print(len(ans), min(ans))

