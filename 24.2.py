f = open('24.2.txt').read()
f = f.replace('D', 'C')
f = f.replace('F', 'C')
f = f.replace('O', 'A')
for i in range(0, 200):
    if i * 'CA' in f:
        print(i)
        