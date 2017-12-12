import random
import sys
import MeCab
import re

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

f = open('out.txt', 'w') # 書き込みモードで開く

for i in range(len(playlog)):
    subject=""
    skill=""
    flag=0
    temp=""
    text=str(playlog[i])#playlog[i]が今見ているところ
    if text.find("成功")!=-1 or text.find("失敗")!=-1:
        print("成否発見"+text)
        for syu in range(2,text.find(":")):
            subject+=text[syu]
        if text.find("成功")!=-1:
            flag=1
        else:
            flag=2
        for k in range(i):
            text1=str(playlog[i-k])
            #print(text1)
            for w in skills:
                skill=str(w[0])
                if text1.find(skill)!=-1:
                    print("技能検出文:"+text1)
                    #playlog[i-k]=""
                    print("検出技能:"+skill)
                    print("主語:"+subject)
                    temp=subject+"は"+w[flag]
                    print(temp)
                    flag=0
                    break
            if flag==0:
                break
    if temp=="" or subject=="GM":
        text=re.sub('\[',"",text)
        text=re.sub('\]',"",text)
        text=re.sub('\'',"",text)
        f.writelines(text+"\n")
    else:
        f.write("【"+temp+"】\n")
f.close()
