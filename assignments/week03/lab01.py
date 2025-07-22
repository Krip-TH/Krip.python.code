age = int(input("How old are you"))

if age > 0 or age <= 12:
    print("You are : Child")
elif age >= 13 or age <= 19:
    print("You are : Teenager")
elif age >= 20 or age <= 59:
    print("You are : Adult")
elif age >= 60:
    print("You are : Senior")
else :
    print("invaild")               