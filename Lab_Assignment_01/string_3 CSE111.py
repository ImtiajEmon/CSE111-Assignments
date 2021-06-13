s = input()

start = 0
stop = 0
flag = 1
for i in range(len(s)):
    if s[i].isupper():
        if flag == 1:
            start = i
            flag += 1
        else:
            stop = i

    elif(stop > 0):
        break

sub_string = s[start+1 : stop]
if sub_string == "":
    sub_string = "BLANK"
print(sub_string)
