number = int(input("Enter a number:"))

# 153 % 10 = 3
# 153 / 10 = 15
# 15  
number1 = number
number3 = 0
while(number1 != 0):
    number3 += (number1 % 10)**3
    number1 = int(number1/10)

if number3 == number:
    print("armstrong number")
else:
    print("not armstrong number")


# prime number 

