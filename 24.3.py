s = open('24.3.txt')
f = 'T' + s.read() + 'T'
ind = []
ans = []
for i in range(len(f)):
    if f[i] == 'T':
        ind.append(i)
for i in range(len(ind)-151):
    ans.append(ind[i+151] - ind[i] - 1)
print(min(ans)-2)