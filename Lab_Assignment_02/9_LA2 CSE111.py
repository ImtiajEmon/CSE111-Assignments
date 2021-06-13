def upper_machine(para,position):
    m=para[position]
    m=m.upper()
    para=para[:position] + m + para[position+1:]
    return para

 

def punctuation(string):
    for i in range(0,len(string),+1):
        if i==0:
            string = upper_machine(string,i)
            
        if (string[i] == "." or string[i] == "!" or string[i] == "?") and i < len(string)-3:
            string = upper_machine(string,i+2)
            
        if string[i] == "i" and string[i-1] == " " and string[i+1] == " ":
            string = upper_machine(string,i)
            
    print(string)
    
    
paragraph=input()
punctuation(paragraph)
        