# import math
# numbers = [list((a,b,c)) for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
# # numbers = [math.sin(i) for i in range(5)]


# # numbers = []
# # numbers1 = []
# # for i in range(1,5): 
# #     numbers1.clear()
# #     for j in range(1,5): 
# #         numbers1.append(j)
# #     numbers.append(numbers1)

# for i in range(2): 
#     for j in range(2): 
#         for k in range(3):
#           [i,j,k]  [0,0,0] [0,0,1] [0,0,2] [0,1,0] [0,1,1] [0,1,2] [1,0,0] [1,0,1] [1,0,2] [1,1,0] [1,1,1] [1,1,2]
    

# print(numbers)

# # 66532

# # for i in range(len(li)-1):
# #    if li[i] > li[i+1]:
# #       print(li[i+1])
# #       break

nested = [["shihab",23],["bati",23],["momen",0]]

for i in range(len(nested)):
    for j in range(2):
        print(nested[i][j],end=" ")
    print()

