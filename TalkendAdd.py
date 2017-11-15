import sys
import MeCab
import random

tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

playlog=[]
pattern=[]
temp=[]
file="playlog.txt"
ld = open(file)
file="talkExtraction10.txt"
intext=open(file)
file="talkaddOut.txt"
outtext=open(file,"w")

try:
    lines = ld.readlines()
    talkend=intext.readlines()
    flag=0
    for line in lines:
        if line.find("「")!=-1:
            print(line)
            outtext.write(line)
            temp=[]
            #print(line)
            node=tagger.parseToNode(line)
            while node:
                #print(node.surface)
                feats=node.feature.split(",")
                if feats[0]=="動詞" or feats[0]=="名詞":
                    temp.append(node.surface)
                    #print(node.surface)
                node=node.next
            #print(temp)
            for text in talkend:
                if flag!=0:
                    if flag>matchMax:
                        pattern=[]
                        matchMax=flag
                    if flag==matchMax and text.endswith("。\n"):
                        #pattern=pattern+text
                        pattern.append(text)
                    #text=str(flag)+text
                    #print(str(flag)+text)
                    flag=0
                if text.find("'")!=-1:
                    for sp in temp:
                        if text.find(sp)!=-1:
                            flag=flag+1
                #print(str(pattern))
            if len(pattern)>0:
                #print(pattern[random.randint(0,len(pattern)-1)])
                outtext.write(pattern[random.randint(0,len(pattern)-1)])
            pattern=[]
            matchMax=0
                
finally:
    ld.close()
    intext.close()
    outtext.close()
