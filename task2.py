lst = [1, 2, 3, 4, 5, 6]
sch = 0
snech = 0
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        sch += lst[i]
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        snech += lst[i]
print(sch / snech)