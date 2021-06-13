def food_panda(name,place="Mohakhali"):
    if place == "Mohakhali":
        if name =="BBQ Chicken Cheese Burger":
            prize=250+40+250*8/100
        elif name=="Beef Burger":
            prize=170+40+170*8/100
        elif name=="Naga Drums" :
            prize=200+40+200*8/100
            
    else:
        if name =="BBQ Chicken Cheese Burger":
            prize=250+60+250*8/100
        elif name=="Beef Burger":
            prize=170+60+170*8/100
        elif name=="Naga Drums" :
            prize=200+60+200*8/100
            
    print(prize)

n=input()
p=input()

if p=="":
    food_panda(n)
else:
    food_panda(n,p)
   