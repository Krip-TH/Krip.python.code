currency = input("Your conversion direction (1 : THB to USD , 2 : USD to THB):")
amount = float(input("Amout to convert :"))


if currency == "1":
    result = amount / 35.5
    print("Result :",result,"USD")

if currency == "2":
    result = amount * 35.5
    print("Result:",result, "THB")   

