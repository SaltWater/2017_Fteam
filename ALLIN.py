import random
import sys
import MeCab
import re

for times in range(10):
    #random.seed(times)
    print("\n"+str(times)+"回目")
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

    file="outfiles/SkillReplaced"+str(times)+".txt"
    f = open(file, 'w') # 書き込みモードで開く
    print("SkillPickSuccessFaile.py")
    for i in range(len(playlog)):
        sys.stdout.write("\r%d/%d" % (i,len(playlog)))
        sys.stdout.flush()
        subject=""
        skill=""
        flag=0
        temp=""
        text=str(playlog[i])#playlog[i]が今見ているところ
        if text.find("成功")!=-1 or text.find("失敗")!=-1:
            for syu in range(2,text.find(":")):
                subject+=text[syu]
            if text.find("成功")!=-1:
                flag=1
            else:
                flag=2
            for k in range(i):
                text1=str(playlog[i-k])
                for w in skills:
                    skill=str(w[0])
                    if text1.find(skill)!=-1:
                        temp=subject+"は"+w[flag]
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
    
    tagger = MeCab.Tagger("mecabrc")
    tagger.parse('')
    pattern=[]
    temp=[]
    file="outfiles/SkillReplaced"+str(times)+".txt"
    ld = open(file)
    file="aozora/talkExtraction30と丸.txt"
    intext=open(file)
    file="outfiles/talkaddOut"+str(times)+".txt"
    outtext=open(file,"w")

    try:
        lines = ld.readlines()
        talkend=intext.readlines()
        flag=0
        i=1
        matchMax=0
        print("\nTalkendAdd.py")
        for line in lines:
            sys.stdout.write("\r%d/%d" % (i,len(playlog)))
            sys.stdout.flush()
            i+=1
            outtext.write(line)
            if line.find("「")!=-1:
                syugo=""
                temp=[]
                node=tagger.parseToNode(line)
                while node:
                    if node.surface.count(":") or node.surface.count("："):
                        syugo=node.prev.surface
                    feats=node.feature.split(",")
                    if feats[0]=="動詞" or feats[0]=="名詞":
                        temp.append(node.surface)
                    node=node.next
                for text in talkend:
                    if flag!=0:
                        if flag>matchMax:
                            pattern=[]
                            matchMax=flag
                        if flag==matchMax:
                            pattern.append(text)
                        flag=0
                    if text.find("'")!=-1:
                        for sp in temp:
                            if text.find(sp)!=-1:
                                flag=flag+1
                if len(pattern)>0:
                    text1=""
                    text=pattern[random.randint(0,len(pattern)-1)]
                    node=tagger.parseToNode(text)
                    while node:
                        feats=node.feature.split(",")
                        if feats[2]=="人名":
                            text1+=syugo
                            node=node.next
                        text1+=node.surface
                        node=node.next
                    outtext.write("【"+text1+"】\n")
                pattern=[]
                matchMax=0
                    
    finally:
        ld.close()
        intext.close()
        outtext.close()
    
    file="outfiles/talkaddOut"+str(times)+".txt"
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

    file="outfiles/SkillRemoved"+str(times)+".txt"
    f = open(file, 'w') # 書き込みモードで開く

    print("\nSkillRemove.py")
    for i in range(len(playlog)):
        sys.stdout.write("\r%d/%d" % (i+1,len(playlog)))
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
