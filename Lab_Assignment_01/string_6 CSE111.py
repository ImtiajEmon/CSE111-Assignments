def passcheck(s):
    d=0
    u=0
    l=0
    sp=0
    for i in s:
        if i=='0'or i=='1'or i=='2'or i=='3'or i=='4'or i=='5'or i=='6'or i=='7'or i=='8'or i=='9':
            d += 1
        elif i=='_' or i=='$' or i=='#' or i =='@':
            sp += 1
        else:
            m=i.upper()
            if i==m:  
                u+=1
            else:
                l+=1
                
    if d>0 and u>0 and l>0 and sp>0:
        print('OK')
    else:
        if d==0:
            print('Digit missing')
        if u==0:
            print('Uppercase character missing')
        if l==0:
            print('Lowercase character Missing')
        if sp==0:
            print('Special character Missing')


s=input()
passcheck(s)
            