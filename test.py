import sys

file="test.txt"
ld = open(file)
lines = ld.readlines()
for line in lines:
    print(line)
print(lines[1])
print(lines)
print(lines.index("図書館\n"))
list=lines[2].split()
print(list)
