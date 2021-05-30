#Find BMI

height = float(input("Enter height ft(foot) : "))
weight = float(input("Enter weight Kg  : "))

height = (height*12*2.54)/100
BMI = round(weight/height**2)

print(f'Your BMI is {BMI} KGM^2')
