import random
import sys
import MeCab
import re

hyouka=open("hyouka.txt","w")
for i in range(10):
    file="hyouka"+str(i)+".txt"
    ld = open(file)
    lines = ld.readlines()
    playlog=[]
    for line in lines:
        playlog.append(line.splitlines())
    file="output"+str(i+1)+"_cabocha.txt"
    ld=open(file,"r",encoding="utf-8")
    lines=ld.readlines()
    flag=0
    k=0
    for line in lines:
        #playlog[i]が見てる場所
        if line.find("「")!=-1:
           # print("みつけた")
            if flag==0:
                flag=1
            else:
                print(str(playlog[k+1]))
                text=re.sub('\[',"",str(playlog[k+1]))
                text=re.sub('\]',"",text)
                text=re.sub('\'',"",text)
                hyouka.write(text+"\n")
                k=k+3
                if k>=len(playlog):
                    break
        if line.find("【"+str(playlog[k+2])+"】")!=-1 and flag==1:
            flag=0
hyouka.close()
ld.close()
