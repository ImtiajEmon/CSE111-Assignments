def vowel_count(name):
    count=0
    vowels=""
    vowel='aeiouAEIOU'
    for i in name:
        if i in vowel:
            vowels += i
            count+=1
        
    if count>0:
        print("Vowels:",end=" ")
        for i in range(0,len(vowels)):
            if i==len(vowels)-1:
                print(vowels[i],end=".")
            else:
                print(vowels[i],end=",")
        print("The number of total vowel:",count)
    else:
        print("No vowels in the name")
                
    
n=input()    
vowel_count(n)
        
    
    