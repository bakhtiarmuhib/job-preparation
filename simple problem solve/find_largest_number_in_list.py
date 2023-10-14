numbers = [12,43,54,67,98,43,56,76,101,34,65,76,98,100]

# largest_number = 0
# for number in numbers:
#     if largest_number < number:
#         largest_number = number

numbers.sort(reverse=True)
print(numbers[1])