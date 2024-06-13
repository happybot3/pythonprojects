from statistics import*
cg = []
ans = []
f = open('24.1.txt').readlines()
for i in f:
    cg.append(i.count('G'))
ming = min(cg)
st = cg.index(ming)
print(max(multimode(f[st])))
