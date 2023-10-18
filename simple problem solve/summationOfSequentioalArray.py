numbers = [1,2,3,4,5,6,7,8,9,10]

summation = 0
for number in numbers:
    summation += number
print("summation is:",summation)

# n*(n+1)/2

n = len(numbers)
summation = (n*(n+1))/2
print("summation is:",summation)