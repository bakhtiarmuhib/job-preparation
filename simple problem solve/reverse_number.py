# 123 % 10 = 3
# 123 / 10 = 12

# 12 % 10 = 2
# 12/10 = 1

# 1 % 10 = 1
# 1/10 = 0

# 3*10 + 2= 32
# 32*10 +1 = 321

######reverse number

# number =  int(input("Enter A number:"))
# print("number is:" ,number)
# reverse_number = 0

# while(number != 0):
#     reverse_number = reverse_number * 10 + (number % 10)
#     number = int(number / 10)

# print("reverse number:", reverse_number)

######palindrome   number


number =  int(input("Enter A number:"))
print("number is:" ,number)
number1 = number
reverse_number = 0

while(number != 0):
    reverse_number = reverse_number * 10 + (number % 10)
    number = int(number / 10)
if reverse_number == number1:
    print(f"{number1} is a palindrome")
else:
    print(f"{number1} is not a palindrome")




