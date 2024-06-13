f = open('24.6.txt')
s = f.readline()
s = s.replace('O', 'A')
s = s.replace('B', 'C')
s = s.replace('D', 'C')
for i in range(1, 300):
    if i * 'CA' in s:
        print(i)