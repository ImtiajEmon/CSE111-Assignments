import re
input_lst = []
inpt = input()
input_lst = re.split(':|,', inpt)

ans = {}
for i in range(1 , len(input_lst) , +2):
    if input_lst[i] not in ans:
        ans[input_lst[i]] = []
    ans[input_lst[i]].append(input_lst[i-1])
    #print(input_lst[i])

print(ans)