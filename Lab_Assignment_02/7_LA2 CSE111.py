# idea 1:

def palindrome(str): 
    str=str.replace(" ","")
    for i in range(0,(len(str)//2)):
        
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  

s = input()

if (palindrome(s)): 
    print("Palindrome") 
else: 
    print("Not a Palindrome") 