from fnmatch import*
for i in range(317, 10**8 + 1, 317):
    if fnmatch(str(i), '12??1*56'):
        print(i, i// 317)