import random
import sys
import MeCab

tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

file="playlog.txt"
ld = open(file)
lines = ld.readlines()
playlog=[]
for line in lines:
    playlog.append(line.splitlines())

file="skill.txt"
ld = open(file)
lines = ld.readlines()
skills=[]
for line in lines:
    skills.append(line.split())

logs=[]

for i in range(len(playlog)):
    text=str(playlog[i])
    node = tagger.parseToNode(text)
    while node:
        for w in skills:
            if node.surface.count(w[0]):
                print(node.surface)
                temp=[]
                for n in range(7):
                    temp.append(playlog[i+n-3])
                logs.append(temp)
                print(temp)
        node=node.next
