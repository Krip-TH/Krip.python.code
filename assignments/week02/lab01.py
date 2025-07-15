weight = float(input("What is yours weight:"))
height = float(input("what's your hight :"))
bmi = weight / height ** 2

if bmi < 18.5:
    print("Underweight")

elif bmi >= 18.5 and bmi <= 24.9 :
    print("Normal Weight")    

elif bmi >= 25.0 and bmi <= 29.5 :
    print("Overweight")

elif bmi >= 30.0 :
    print("Obese")        

print("Your BMI :",bmi)

