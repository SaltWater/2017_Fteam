import random
import sys
import MeCab
import re
import oreore
from operator import itemgetter

for times in range(1):
    #random.seed(times)
    print("\n"+str(times)+"回目")
    file="playlog2.txt"
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
    file="outfiles/hyouka"+str(times)+".txt"
    hyoukatxt=open(file,"w")
    file="outfiles/hyouka.txt"
    defile=open(file)
    try:
        lines = ld.readlines()
        talkend=intext.readlines()
        flag=0
        i=1
        matchMax=0
        print("\nTalkendAdd.py")
        for line in lines:
            syugo=""
            sys.stdout.write("\r%d/%d" % (i,len(playlog)))
            i=i+1
            sys.stdout.flush()
            outtext.write(line)
            for syu in range(line.find(":")):
                syugo+=line[syu]
            if line.find("「")!=-1 and syugo!="GM":
                hyoukatxt.write(line)
                temp=[]
                node=tagger.parseToNode(line)
                while node:
                    feats=node.feature.split(",")
                    if feats[0]=="動詞" or feats[0]=="名詞":
                        temp.append(node.surface)
                    node=node.next
                matchlist=[]
                for text in talkend:
                    if flag!=0:
                        matchlist.append([text,flag])
                        #以下最大合致のみ
                        #if flag>matchMax:
                        #    pattern=[]
                        #    matchMax=flag
                        #if flag==matchMax:
                        #    pattern.append(text)
                        flag=0
                    if text.find("'")!=-1:
                        for sp in temp:
                            if text.find(sp)!=-1:
                                flag=flag+1
                matchlist=sorted(matchlist,key=itemgetter(1),reverse=False)
                while len(pattern)<11:#or len(matchlist)!=0:
                    if len(pattern)==0:
                        pattern.append(matchlist.pop())
                    if pattern[len(pattern)-1][0]!=matchlist[len(matchlist)-1][0]:
                        pattern.append(matchlist.pop())
                    else:
                        matchlist.pop()
                print(pattern)
                op=0
                for n in pattern:
                    print(n[0])
                    for d in defile:
                        #print(d)
                        if n[0]==d:
                            pattern.pop(op)
                            break
                    op=op+1
                print(pattern)         
                if len(pattern)>0:
                    text=str(pattern[random.randint(0,len(pattern)-1)][0])
                    #text=pattern[times][0]
                    hyoukatxt.write(text)
                    text=re.sub("\n","",text)
                    if oreore.syugo_pickup(text)!="null":
                        text=re.sub(oreore.syugo_pickup(text),syugo,text)
                    hyoukatxt.write(text+"\n")
                    outtext.write("【"+text+"】\n")
                pattern=[]
                matchMax=0
                    
    finally:
        ld.close()
        intext.close()
        outtext.close()
        hyoukatxt.close()
        defile.close()
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
            if text.find(skill)!=-1 and len(text)<20:
                flag=False
        if flag:
            text=re.sub('\[',"",text)
            text=re.sub('\]',"",text)
            text=re.sub('\'',"",text)
            if text!="":
                f.write(text+"\n")
    f.close()