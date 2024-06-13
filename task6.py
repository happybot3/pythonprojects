print('введите количество элементов в списке')
k = int(input())
print('введите каждый элемент списка через пробел')
num = input().split()
num1 =[int(x) for x in num]
neg = []
for i in range(k):
    if num1[i] < 0:
        neg.append(num1[i])
print(len(neg))
