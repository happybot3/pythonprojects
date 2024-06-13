for x in '0123456789abcdef':
    n1 = int(f'8{x}84{x}', 16)
    n2 = int(f'78{x}34', 16)
    if (n1 + n2) % 23 == 0:
        print(x, (n1 + n2) // 23)
