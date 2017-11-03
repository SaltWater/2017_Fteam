import random
import sys
import MeCab
import re

def pickup(temp,w):
    tagger = MeCab.Tagger("mecabrc")
    tagger.parse('')
    flag=0
    ss=0
    returnText=""
    returnText1=""
    returnText2=""
    node=tagger.parseToNode(str(temp[3]))

    
    for n in range(4):
        checktxt=str(temp[3+ss])
        node=tagger.parseToNode(checktxt)
        while node:
#            print("主語:"+returnText)
#            print("探査単語    "+node.surface)
#            print("flag:"+str(flag))
            if node.surface.count(":") or node.surface.count("："):
                returnText=node.prev.surface
                returnText+="は"
            if node.surface.count("に") or node.surface.count("を"):
                node2=node.prev
                if node2.surface.count(w[0]):
                    break
                if node2.prev.surface.count("の"):
                    returnText1+=node2.prev.surface
                    returnText1+=node2.surface
                returnText1+=node2.surface
            if node.surface.count("成功"):
                flag=1
            if node.surface.count("失敗"):
                flag=2
            node=node.next
        ss=ss+1
        if flag!=0:
            break

    if flag==0:
        for n in range(3):
            checktxt=str(temp[2-n])
            node=tagger.parseToNode(checktxt)
            while node:
                if node.surface.isdigit():
                    filename="playerskill.txt"
                    ld = open(filename)
                    lines = ld.readlines()
                    playerSkill=[]
                    for line in lines:
                        playerSkill.append(line.split())
                        for z in playerSkill:
                            if node.surface.count(z[0]):
                                if int(node.surface)<=z[1]:
                                    flag=1
                                else:
                                    flag=2
                node=node.next
    if flag==1:
        returnText2=w[1]
    if flag==2:
        returnText2=w[2]
    if flag==0:
        returnText2=w[3]

#    if returnText1=="":
        
    
    returnText+=returnText1
    returnText+=returnText2
    
    return returnText
    
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

f = open('out.txt', 'w') # 書き込みモードで開く

for i in range(len(playlog)):
    text=str(playlog[i])#playlog[i]が今見ているところ
    node = tagger.parseToNode(text)
    while node:
        for w in skills:
            if node.surface.count(w[0]):
#                print("検出技能:"+node.surface)
#                print(playlog[i])
                temp=[]
                for n in range(7):
                    temp.append(playlog[i+n-3])
                logs.append(temp)
                print (temp)
                rrr=str(pickup(temp,w))
                print(rrr)
                f.writelines(rrr)
                f.write("\n")
        node=node.next
    text=text+"\n"
    text=re.sub('\[',"",text)
    text=re.sub('\]',"",text)
    text=re.sub('\'',"",text)
    f.writelines(text)
f.close()
