import sys
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

playlog=[]
nlist=[]
slist=[]
file="akai_kabutomushi.txt"
ld = open(file)
file="talkExtraction.csv"
outtext=open(file,w)

try:
    lines = ld.readlines()
    flag=0
    for line in lines:
    #    print(line)
        node=tagger.parseToNode(line)
        if flag==1:
            print(line.replace("\n",""))
            flag=0
            while node:
                feats=node.feature.split(",")
                if feats[0]=="動詞":
                    slist.append(node.surface)
                    node=node.next
                node=node.next
            if len(nlist)!=0 and len(slist)!=0:
                print(str(nlist))
                outtext.write(str(nlist))
                print(str(slist)+"\n")

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
                print(line.replace("\n",""))
                break
            node=node.next
        beforeline=line
finally:
    ld.close()
    outtext.close()
