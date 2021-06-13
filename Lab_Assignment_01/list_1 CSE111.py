lst=[]
count=[]
i=0
while i != 'STOP':
    i=input()
    if i in lst:
        count[lst.index(i)]+=1
    
    else:
        lst.append(i)
        count.append(1)
        
for i in range(len(lst)-1):
    print(lst[i],'-',count[i],'times')
    
