a = input()
lst = []
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        lst.append(a[i])
print(len(lst))
