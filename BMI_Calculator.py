weight=int(input("Enter your weight:"))
height=float(input("Enter your height:"))
bmi=weight/(height/100)**2
if bmi<18.5:
    print("You are Underweight")
if bmi>=18.5 and bmi<25:
    print("You are in Normal weight") 
if bmi>=25 and bmi<30:
    print("You are Overweight")  
if bmi>=30:
    print("You are in Obesity State")
