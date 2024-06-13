f = open('24.5.txt').read()
ind = []
ans = []
for i in range(len(f)):
    if f[i] == 'V':
        ind.append(i)
for i in range(0, len(ind) - 119):
    ans.append(ind[i+119] - ind[i] + 1)
print(min(ans))
