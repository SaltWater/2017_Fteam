import random
import sys
import MeCab
import re
import oreore
import os
from operator import itemgetter
inputfile=input("入力ファイル名を入力して下さい：")
repetition=input("何回出力しますか：")

for times in range(int(repetition)):
    #random.seed(times)
    print("\n"+str(times)+"回目")
    #file="playlog3.txt"
    ld = open(inputfile)
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

    file="outfiles2/SkillReplaced"+str(times)+".txt"
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
        if text.find("成功")!=-1 or text.find("失敗")!=-1 or text.find("ファンブル")!=-1:
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
                        mov=""
                        if skill=="対抗ロール":
                            if text1.find("STR")!=-1:
                                mov="筋力で"
                            if text1.find("POW")!=-1:
                                mov="精神で"
                            if text1.find("INT")!=-1:
                                mov="知力で"
                            if text1.find("DEX")!=-1:
                                mov="速さで"                                                             
                        temp=subject+"は"+mov+w[flag]
                        flag=0
                        break
                if flag==0:
                    break
        if temp=="" or subject=="GM":
            text=re.sub('\[',"",text)
            text=re.sub('\]',"",text)
            text=re.sub('\'',"",text)
            #playlog[i]=text+"\n"
            f.writelines(text+"\n")
        else:
            #playlog[i]="【"+temp+"】\n"
            f.write("【"+temp+"】\n")
    f.close()
    
    tagger = MeCab.Tagger("mecabrc")
    tagger.parse('')
    pattern=[]
    temp=[]
    file="outfiles2/SkillReplaced"+str(times)+".txt"
    ld = open(file)
    file="aozora/talkExtraction30_new.txt"
    intext=open(file)
    file="outfiles2/talkaddOut"+str(times)+".txt"
    outtext=open(file,"w")
    file="outfiles2/hyoukaSkillReplaced"+str(times)+".txt"
    hyoukatxt=open(file,"w")
    try:
        lines = ld.readlines()
        talkend=intext.readlines()
        flag=0
        i=1
        matchMax=0
        print("\nTalkendAdd.py")
        #for i in range(len(playlog)):
        for line in lines:
            #print(line)
            syugo=""
            matchlist=[]
            hyouka=[]
            sys.stdout.write("\r%d/%d" % (i,len(lines)))
            #sys.stdout.write("\r%d/%d" % (i,len(playlog)))
            sys.stdout.flush()
            outtext.write(line)
            #if playlog[i].find("「")!=-1:
            #for syu in range(playlog[i].find(":")):
            for syu in range(line.find(":")):
                syugo+=line[syu]
            if line.find("「")!=-1 and syugo!="GM":
                #hyouka.append(line)
                hyoukatxt.write(line)
                temp=[]
                node=tagger.parseToNode(line)
                while node:
                    feats=node.feature.split(",")
                    if feats[0]=="動詞" or feats[0]=="名詞":# and node.surface!="こと" and node.surface!="もの" and node.surface!="いる" and node.surface!="ある" and node.surface!="する" and node.surface!="ゐる":
                        temp.append(node.surface)
                    node=node.next
                matchlist=[]
                for text in talkend:
                    if flag!=0:
                        #node=tagger.parseToNode(text)
                        #while node:
                        #    if node.feature[1]=="格助詞":
                        #        flag=-1
                        #        break
                        #    node=node.next
                        if flag>0:
                            matchlist.append([text,flag])
                        flag=0
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

                while len(pattern)<11 and len(matchlist)>0 or len(matchlist)!=0:
                    if len(pattern)==0:
                        pattern.append(matchlist.pop())
                    if len(matchlist)>0:
                        if pattern[len(pattern)-1][0]!=matchlist[len(matchlist)-1][0]:
                            pattern.append(matchlist.pop())
                        else:
                            matchlist.pop()
                if len(pattern)>0:
                    text=str(pattern[random.randint(0,len(pattern)-1)][0])
                    #text=pattern[times][0]
                    hyoukatxt.write(text)
                    #hyouka.append(text)
                    text=re.sub("\n","",text)
                    toflag=True
                    if text.startswith("と、"):
                        text=text.lstrip("と、")
                        toflag=False
                    else:
                        text=text.lstrip("と")
                        
                    if oreore.syugo_pickup(text)!="null":
                        text=re.sub(oreore.syugo_pickup(text),syugo,text)
                    else:
                        text=syugo+"は"+text
                    if random.randint(0,1)>0:
                        if toflag:
                            text="と"+text
                        else:
                            text="と、"+text
                    #print(text)
                    outtext.write("【"+text+"】\n")
                    #hyouka.append(text)
                    hyoukatxt.write(text+"\n")
                pattern=[]
                matchMax=0
            i=i+1
                    
    finally:
        ld.close()
        intext.close()
        outtext.close()
        hyoukatxt.close()
    
    file="outfiles2/talkaddOut"+str(times)+".txt"
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

    file="outfiles2/SkillRemoved"+str(times)+".txt"
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
            if text.find(skill)!=-1 and len(text)<40 :
                flag=False
        if flag and text.find("SAN値チェック")==-1 and re.search("[0-9][Dd][0-9]",text)==None:
            text=re.sub('\[',"",text)
            text=re.sub('\]',"",text)
            text=re.sub('\'',"",text)
            if text!="":
                f.write(text+"\n")
    f.close()
