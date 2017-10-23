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
    text=str(playlog[i])#playlog[i]が今見ているところ
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
                for n in range(3):
                    flag=0
                    checktxt=temp[4+n]
                    node2=tagger.parseToNode(checktxt)
                    while node2:
                        if node.surface.count("成功"):
                            flag=1
                            break
                        if node.surface.count("失敗"):
                            flag=2
                            break
                        node2=node2.next
                if flag==0:
                    for n in range(3-n):
                        checktxt=temp[3-n]
                        node2=tagger.parseToNode(checktxt)
                        playerName=node2.surface
                        while node2:
                            if node2.surface.isdigit():
                                filename=playerName+".txt"
                                ld = open(filename)
                                lines = ld.readlines()
                                playerSkill=[]
                                for line in lines:
                                    playerSkill.append(line.split())
                                for z in playerSkill:
                                    if node.surface.count(z[0])):
                                        if int(node2.surface)<z[1]:
                                            flag=1
                                        else:
                                            
        node=node.next
