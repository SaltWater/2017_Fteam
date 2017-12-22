import sys
import os
import glob
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')
test=glob.glob("testfile/*.txt")


playlog=[]
nlist=[]
wordMax=30#10#30#20 #sys.maxsize
slist=""
file="talkExtraction"+str(wordMax)+".txt"
outtext=open(file,"w")
i=0

for novel in test:
    i=i+1
    sys.stdout.write("\r%d/%d" % (i,len(test)))
    #print(novel)
    outtext.write(novel+"\n")
    f=open(novel)
    lines=f.readlines()
    flag=0
    for line in lines:
        #print(line)
        node=tagger.parseToNode(line)
        if flag==1:
            #print(line)
            flag=0
            line=line.replace("\n","")
            feats=node.next.feature.split(",")
            #feats=node.feature.split(",")
            #print("追加文章"+line)
            #print("先頭一文字の構文解析"+feats[0])
            if len(nlist)!=0 and len(line)<wordMax and len(line)>2 and line.startswith("と") and line.endswith("。") and (feats[0]=="助詞"or feats[0]=="フィラー"):
                while node:
                    if node.feature[1]=="格助詞":
                        print("格助詞発見"+line)
                        flag=2
                        break
                    node=node.next
                if flag!=2:
                    outtext.write(str(nlist)+"\n")
                    outtext.write(str(line)+"\n\n")
            nlist=[]
            slist=[]
        if line.startswith("「"):
            #print(line)
            while node:
                feats=node.feature.split(",")
                if (feats[0]=="動詞" or feats[0]=="名詞")and node.surface!="こと" and node.surface!="もの" and node.surface!="いる" and node.surface!="ある" and node.surface!="する" and node.surface!="ゐる":
                    nlist.append(node.surface)
                node=node.next
            flag=1
        beforeline=line
f.close()
outtext.close()
