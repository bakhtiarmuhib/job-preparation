name = "Md Bakhtiar Muhib"
# print(chr(ord("m")-32))

output = ""
for i in range(len(name)):
    if  'a' <= name[i] and  "z" >= name[i]:
        output +=name[i].upper()
    else:
        output += name[i].lower()

print(output)
    


