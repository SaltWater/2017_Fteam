import sys
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

playlog=[]

file="akai_kabutomushi.txt"
ld = open(file)
lines = ld.readlines()
flag=0
for line in lines:
#    print(line)
    if flag==1:
        print(line)
        flag=0
    node=tagger.parseToNode(line)
    while node:
        if node.surface.count("「"):
            flag=1
            print(line)
        node=node.next
