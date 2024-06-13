lst = []
for x in '0123456789a':
    for y in '0123456789a':
        n1 = int(f'{x}341{y}', 11)
        n2 = int(f'56{x}1{y}', 19)
        if (n1 + n2) % 305 == 0:
            lst.append(n1 + n2)
m = min(lst)
print(m // 305)
