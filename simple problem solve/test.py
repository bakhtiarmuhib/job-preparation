n = int(input())
if n%2 != 0:
    print("Weird" )

elif n%2 == 0 and (1 < n < 6):
    print("Not weird") 
elif n%2 == 0 and (5 < n and n < 21):
    print("Weird")
elif n%2 == 0 and (20 < n):
    print("Not weird")
