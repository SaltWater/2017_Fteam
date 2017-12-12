import sys
import MeCab
import random

tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

playlog=[]
pattern=[]
temp=[]
file="out.txt"
ld = open(file)
file="aozora/talkExtraction30と丸.txt"
intext=open(file)
file="talkaddOut1.txt"
outtext=open(file,"w")

try:
    lines = ld.readlines()
    talkend=intext.readlines()
    flag=0
    matchMax=0
    for line in lines:
        outtext.write(line)
        if line.find("「")!=-1:
            syugo=""
            print(line)
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
