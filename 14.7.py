for x in '0123456789abcdef':
    n1 = int(f'1{x}bad', 16)
    n2 = int(f'2c{x}fe', 16)
    if (n1 + n2) % 15 == 0:
        print(x, (n1 + n2) // 15)
        break
