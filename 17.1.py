f = open('17.1.txt')
lst = [int(x) for x in f]
ans = []
for i in range(0, len(lst)-2):
    if abs(lst[i] + lst[i+1] + lst[i+2]) % 10 == 5 and  abs(lst[i] * lst[i+1] * lst[i+2]) % 7 == 0:
        ans.append(lst[i] + lst[i+1] + lst[i+2])
print(len(ans), max(ans))

