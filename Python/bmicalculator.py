#BMI Calculator
weight=int(input("Enter your weight(in kgs):"))
height=float(input("Enter your height(in meters):"))
bmi=(weight/(height*height))
if bmi<18.5 :print("Your BMI is:",bmi , " You are underweight.")
elif bmi<25 :print("Your BMI is:",bmi, "You are Normal")
elif bmi<30 :print("Your BMI is:",bmi, "You are Overweight")
else :print("You are obese")
