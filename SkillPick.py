import random
import sys
import MeCab
def pickup(text,list):
    tagger1 = MeCab.Tagger("mecabrc")
    tagger1.parse('')
    node = tagger1.parseToNode(text)
    returnText=""
    returnText2=""
    flag=False
    
    while node:
        if node.surface.count(":"):
            returnText2+=returnText
            returnText2+="は"
        if node.surface.count("に"):
            returnText2+=subnode.surface
            returnText2+=node.surface
        #print(node.surface)
        if node.surface.count("<"):
            subnode=node.next#探索ノード
            for w in list:
                if subnode.surface.count(w[0]):
                    subnode=subnode.next
                    if subnode.surface.count("成功"):
                        flag=True
                    else:
                        flag=False
                    subnode=subnode.next
                    while subnode:
                        #print(subnode.surface)
                        if subnode.feature.count("を"):
                            returnText2+=beforenode.surface
                            returnText2+="を"
                        beforenode=subnode#一個前見るノード
                        subnode=subnode.next
                    if flag:
                        returnText2+=w[1]
                    else:
                        returnText2+=w[2]
                    break
        returnText+=node.surface #スキルが無いときはそのまま返す
        subnode=node
        node=node.next

    if returnText2!="":
        return returnText2
    else:

        return returnText

file="test.txt"
ld = open(file)
lines = ld.readlines()
list=[]
for line in lines:
    list.append(line.split())

while True:
    print('技能で置き換える')
    text1 = input('sentence1>> ')
    keylist=pickup(text1,list)
    print(keylist)
