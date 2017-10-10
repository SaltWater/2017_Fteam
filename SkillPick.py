import random
import sys
import MeCab
def pickup(text):
    tagger1 = MeCab.Tagger("mecabrc")
    tagger1.parse('')
    node = tagger1.parseToNode(text)
    returnText=""
    returnText2=""
    skill=["図書館","聞き耳","目星"]
    
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
            if subnode.surface in skill:
                subnode=subnode.next
                if subnode.surface.count("成功"):
                    flag=True #returnText2+="をみつけた"
                else:
                    flag=False #returnText2+="がみつからなかった"
                subnode=subnode.next
                while subnode:
                    #print(subnode.surface)
                    if subnode.feature.count("を"):
                        returnText2+=beforenode.surface
                        break
                    beforenode=subnode#一個前見るノード
                    subnode=subnode.next
                if flag:
                        returnText2+="をみつけた"
                else:
                    returnText2+="がみつからなかった" 
    
        returnText+=node.surface
        
        #if node.feature.count("動詞")and not(node.feature.count("助動詞")):
        #    returnText+="激しく"
        #returnText+=node.surface
        subnode=node
        node=node.next
    if returnText2!="":
        return returnText2
    else:
        return returnText
while True:
    print('技能で置き換える')
    text1 = input('sentence1>> ')
    keylist=pickup(text1)
    print(keylist)
