import sys,time
import MeCab
import re

file="talkaddOut1.txt"
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

f = open('SkillRemoved.txt', 'w') # 書き込みモードで開く

for i in range(len(playlog)):
    sys.stdout.write("\r%d/%d" % (i,len(playlog)))
    sys.stdout.flush()
    skill=""
    flag=True
    temp=""
    text=str(playlog[i])#playlog[i]が今見ているところ
    for w in skills:
        skill=str(w[0])
        if text.find(skill)!=-1:
            flag=False
    if flag:
        text=re.sub('\[',"",text)
        text=re.sub('\]',"",text)
        text=re.sub('\'',"",text)
        f.write(text+"\n")
f.close()
