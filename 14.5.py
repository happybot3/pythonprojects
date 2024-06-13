lst = []
for x in '01234567':
    for y in '01234567':
        n1 = int(f'{y}04{x}5', 11)
        n2 = int(f'253{x}{y}', 8)
        if (n1 + n2) % 117 == 0:
            lst.append(n1 + n2)
m =  min(lst)
print(m // 117)