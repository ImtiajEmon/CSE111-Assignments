# to split with 2 command we need to import re
import re
dct1 = {}
lst = []
s = input()
lst = re.split(":|," , s)
for i in range(0,(len(lst) - 1),+2):
    dct1[lst[i]] = int(lst[i+1])

lst.clear()   
dct2 = {}
lst = []
s = input()
lst = re.split(":|," , s)
for i in range(0,(len(lst) - 1),+2):
    dct2[lst[i]] = int(lst[i+1])
    
for i in dct2:
    if (i in dct1):
        dct1[i] += dct2[i]
    else:
        dct1[i] = dct2[i]
        
lst = []
detector = False
for i in dct1:
    for j in lst:
        if dct1[i] == j:
            detector = True
            break
        else:
            detector = False
    if detector == False:
        lst.append(dct1[i])
        
lst.sort()
lst = tuple(lst)
print(dct1)
print("Values:",lst)
