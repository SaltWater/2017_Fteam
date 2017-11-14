import sys
import os
import glob
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')
test=glob.glob("testfile/*.txt")

playlog=[]
nlist=[]
slist=""
file="talkExtraction.txt"
outtext=open(file,"w")

for novel in test:
    print(novel)
    f=open(novel)
    lines=f.readlines()
    flag=0
    for line in lines:
        #print(line)
        node=tagger.parseToNode(line)
        if flag==1:
            #print(line.replace("\n",""))
            flag=0
            line=line.replace("\n","")
            #while node:
            #    feats=node.feature.split(",")
            #    if feats[0]=="動詞":
            #        slist.append(node.surface)
            #        node=node.next
            #    node=node.next
            if len(nlist)!=0 and len(line)<20 and len(line)>2 and line.find("「")<0:
                #print(str(nlist))
                outtext.write(str(nlist)+"\n")
                outtext.write(str(line)+"\n\n")
                #outtext.write("\n")
                #print(str(line)+"\n")
            nlist=[]
            slist=[]
        while node:
            if node.surface.count("「"):
                while node:
                    feats=node.feature.split(",")
                    if feats[0]=="動詞" or feats[0]=="名詞":
                    #if feats[0]!="助詞" and feats[0]!="助動詞"and feats[0]!="記号":
                       # print(node.feature+"\n")
                        nlist.append(node.surface)
                    node=node.next
                flag=1
                #print(line.replace("\n",""))
                break
            node=node.next
        beforeline=line
f.close()
outtext.close()
