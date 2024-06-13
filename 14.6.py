
for x in '0123456789':
    n1 = int(f'3{x}da', 14)
    n2 = int(f'5{x}a6', 12)
    if (n1 + n2) % 81 == 0:
        print(x, (n1 + n2) // 81)
