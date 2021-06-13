count=0
n,k=input().split()
n=int(n)
k=int(k)
lst=input().split(' ')

for i in range(len(lst)):
    lst[i]=int(lst[i])
    
for i in lst:
    if 5-i >= k:
        count+=1
               

print(count//3)