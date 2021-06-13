#idea: 1=> frist we find common from s1 & s2. Then concatenate
s1 = input()
s2 = input()

com_frm_s1 = ''
com_frm_s2 = ''
for i in s1:
    if i in s2:
        com_frm_s1 += i

for i in s2:
    if i in s1:
        com_frm_s2 += i

s = com_frm_s1 + com_frm_s2
if s == '':
    s = 'Nothing in common.'
print(s)



#idea: 2=> first find out the common things. Then concatenate according to their occurence
'''
def common(s1,s2):
    c1=''
    c2=''
    s3=''
    s4=''
    for i in s1:
        if i in s2:
            if i != c2:
                c1+=i
                c2=i
    
    for i in c1:
        s3+=i*s1.count(i)
        s4+=i*s2.count(i)
        
    s=s3+s4
    if s!='':
        print(s)
    else:
        print("Nothing in common.")
                
                
    
        

s1=input()
s2=input()
common(s1,s2)
'''