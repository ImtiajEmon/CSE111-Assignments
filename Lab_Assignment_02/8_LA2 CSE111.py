def count(num):
    num=int(num)
    year=num//365
    
    num=num%365
    month=num//30
    
    num=num%30
    
    if year>1:
        print(year,"years"+",",end=" ")
    else:
        print(year,"year"+",",end=" ")
        
    if month>1:
        print(month,"months and",end=" ")
    else:
         print(month,"month and",end=" ")
         
    if num>1:
        print(num,"days")
    else:
        print(num,"day")
        
        
n=input()
count(n)