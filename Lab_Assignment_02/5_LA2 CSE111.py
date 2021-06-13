part1=""
part2=""

def new_mail(mail,dom1,dom2=part2):
    if dom1 == dom2:
        print("Unchanged:",mail)
    else:
        print("Changed:",part1+dom1)

old_mail=input()
new_domain=input()
old_domain=input()

for i in range(0,len(old_mail)):
    part1 += old_mail[i]
    if old_mail[i]=='@':
        for j in range(i+1,len(old_mail)):
            part2 += old_mail[j]
        break
    

if old_domain == "":
     new_mail(old_mail,new_domain)
else:
    new_mail(old_mail,new_domain,old_domain)