weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight/(height**2)
if BMI < 18.5:
    print (f"your BMI is:{BMI: .2f} meaning you are underweight.")
elif 18.5 <= BMI < 25 :
    print (f"your BMI is:{BMI: .2f} meaning you are normal weight.")
elif 25 <= BMI < 30: 
     print (f"your BMI is:{BMI: .2f} meaning you are overweight.")
else:
    print (f"your BMI is:{BMI: .2f} meaning you are obese.")
