l1=[]
l2=[]
l3=[]

lst1=input()
l1=lst1.split(' ')

for i in range(len(l1)):
    l1[i]=int(l1[i])

lst2=input()
l2=lst2.split(' ')
    
for i in range(len(l2)):
    l2[i]=int(l2[i])
    
for i in range(len(l1)):
    for j in range(len(l2)):
        l3.append(l1[i]*l2[j])
        
print(l3)
