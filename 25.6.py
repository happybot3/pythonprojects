from fnmatch import*
for i in range(4891, 10**10 + 1, 4891):
    if fnmatch(str(i), '1?2711*0'):
        print(i)