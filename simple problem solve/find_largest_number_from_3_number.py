number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
number3 = int(input("Enter number2:"))

print("number1:",number1,"number2:",number2,"number3:",number3)

if number1 > number2 and number1 > number3:
    print("largest number is:",number1)
elif number2 > number3:
    print("largest number is:",number2)
else:
    print("largest number is:",number3)