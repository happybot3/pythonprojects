f = open('17.1.txt')
lst = [int(x) for x in f]
ans = []
for i in range(0, len(lst)-1):
    if (lst[i] % 9 == 0 and int(oct(abs(lst[i+1]))[2:]) % 8 == 3 and lst[i+1] % 9 != 0) or (lst[i+1] % 9 == 0 and int(oct(abs(lst[i]))[2:]) % 8 == 3 and lst[i] % 9 != 0):
        ans.append(max(lst[i], lst[i+1]))
print(len(ans), max(ans))
