import sys

file="test.txt"
ld = open(file)
lines = ld.readlines()
name="「図書館"
list=[]
for line in lines:
    list.append(line.split())
print(list)
for w in list:
    if w[0]==name:
        print(w[1])
        break

print(name.find("「"))
print(w[0])

