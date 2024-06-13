from itertools import *

yes = []
lst = []
k = sorted('васил')
for i in product(k, repeat = 6):
    s = ''.join(i)
    lst.append(s)
    gl = [x for x in lst if x == 'а' or x == 'и']
    sogl = [x for x in lst if x == 'в' or x == 'с' or x == 'л']
    if len(gl) > len(sogl):
        yes.append(s)   
    lst.remove(s)
print(len(set(yes)))