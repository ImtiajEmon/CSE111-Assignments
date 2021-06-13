def bmi(height,weight):
    height=height/100
    bm=weight/(height*height)
    if bm<18.5:
        bmiReport="Underweight"
    elif bm>=18.5 and bm<=24.9:
        bmiReport="Normal"
    elif bm>=25 and bm<=30:
        bmiReport="Overweight"
    else:
        bmiReport="Obese"
        
    print("Score is ",round(bm,1),end=".")
    print("You are",bmiReport)



h=input("Enter your height :")
h=int(h)
w=input("Enter your weight :")
w=int(w)
       
bmi(h,w)