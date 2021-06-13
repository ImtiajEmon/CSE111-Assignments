def string_check(s):
    n = 0
    l = 0
    for i in s:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            n += 1
        else:
            l += 1

    if(n > 0 and l > 0):
        return 'MIXED'
    elif(n > 0):
        return "NUMBER"
    else:
        return "WORD"

    
s = input()
print(string_check(s))
