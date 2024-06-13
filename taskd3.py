n = input()
lst = []
for i in n:
    if int(i) % 2 == 0:
        lst.append(i)
print(len(lst))