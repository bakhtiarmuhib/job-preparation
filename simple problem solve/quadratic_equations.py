# 3x**2 +4x +2 =0
# x = 12, x =43

import math

a = int(input("Enter the value of X**2 :"))
b = int(input("Enter the value of X :"))
c = int(input("Enter the value of constant:"))

if b**2 - (4*a*c) >= 0:
    x1 = (-b + math.sqrt((b**2-4*a*c))) / 2*a
    x2 = (-b - math.sqrt((b**2-4*a*c))) / 2*a

    print("The value of x are",x1, x2)
else:
    print("Unable to find value of x")