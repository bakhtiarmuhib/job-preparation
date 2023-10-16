# 5! = 1*2*3*4*5 = 125

# 0! = 1
# 1! = 1
# 2! = 2

number = int(input("Enter a Number:"))
factorial_calculate = 1

if number < 0:
    print("Unable to calculate factorial number")
elif number == 0 or number == 1:
    print("factorial number is:" ,1)
else:
    while(number > 1):
        factorial_calculate *= number
        number -= 1
    print("factorial number is:" ,factorial_calculate)




