import sys
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

playlog=[]
pattern=[]
file="playlog.txt"
ld = open(file)
file="talkExtraction.txt"
intext=open(file)


try:
    lines = ld.readlines()
    talkend=intext.readlines()
    flag=0
    for line in lines:
        #print(line)
        if line.find("「")!=-1:
            for text in talkend:
                if flag!=0:
                    text=str(flag)+text
                    pattern.append(text)
                    flag=0
                if text.find("'")!=-1:
                    node=tagger.parseToNode(line)
                    while node:
                        print(node.surface)
                        feats=node.feature.split(",")
                        if feats[0]=="動詞" or feats[0]=="名詞":
                            temp=str(node.surface)
                            #print(text)
                            if text.find(temp)!=-1:
                                print(node.surface)
                                flag=flag+1
                        node=node.next
    print(pattern)
finally:
    ld.close()
    intext.close()
