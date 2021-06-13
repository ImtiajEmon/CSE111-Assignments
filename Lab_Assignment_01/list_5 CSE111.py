up_case=[]
l_case=[]
digit_lst=[]

s=input()
for i in s:
    if i != i.lower():
        up_case.append(i)
    elif i != i.upper():
        l_case.append(i)
    else:
        digit_lst.append(int(i))
        
odd=[]
even=[]
for i in digit_lst:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
up_case.sort()
l_case.sort()
odd.sort()
even.sort()


sort_lst=l_case+up_case+odd+even
        
sort=''
for i in sort_lst:
    sort += str(i)
    
print(sort)