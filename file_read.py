import sys
import os
import glob
test=[]
test=glob.glob("/progect/Fteam/*/*.txt")

print(test)
print(test[0])
f=open(test[0])
lines=f.readlines()
for line in lines:
    print(line)
f.close()
