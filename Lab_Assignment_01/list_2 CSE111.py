N = int(input())

sum=0
lst=[]
temp_lst=[]
temp_sum=0

for j in range(N):
    n=input()
    lst=n.split(' ')
    for i in range(len(lst)):
        sum += int(lst[i])
        lst[i] = int(lst[i])

        
    if sum > temp_sum:
        temp_sum = sum
        temp_lst = lst.copy()
        
    sum=0
    lst.clear()
    
print(temp_sum)
print(temp_lst)