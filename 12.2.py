for n in range(101, 500):
    s = n * '5'
    while '555' in s or '11' in s or '2' in s:
        if '555' in s:
            s = s.replace('555', '1', 1)
        if '11' in s:
            s = s.replace('11', '25', 1)
        if '2' in s:
            s = s.replace('2', '5', 1)
    if s == '15':
        print(n)
        break 