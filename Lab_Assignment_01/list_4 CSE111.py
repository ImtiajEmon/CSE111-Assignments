lst=[]
li=[]
s=input()
while s != 'STOP':
    lst=s.split(' ')
    for i in lst:
        li.append(int(i))
    
    lst.clear()

    for i in range(len(li)-1):
        lst.append(abs(li[i]-li[i+1]))
    
    lst.sort()
    
    c=1
    for i in range(len(li)-1):
        if i+1 != lst[i]:
            c=0
            break
    
    if c:
        print('UB Jumper')
    else:
        print('Not UB Jumper')
    lst.clear()
    li.clear()
    s=input()
    