import random
import sys
import MeCab
import re
RNG=12

def pickup(temp,w):
    tagger = MeCab.Tagger("mecabrc")
    tagger.parse('')
    flag=0
    ss=0
    subject=""
    target=""
    result=""    
    
    for n in range(RNG):
        checktxt=str(temp[int(RNG/2)+ss])
        node=tagger.parseToNode(checktxt)
        ss=0
        
        
        #以下主語と目的語の探索、成否の明言があれば取得
        while node:
#            print("主語:"+subject)
#            print("探査単語    "+node.surface)
#            print("flag:"+str(flag))
            if ( node.surface.count(":") or node.surface.count("：") )and subject=="":
                subject=node.prev.surface
            if (node.surface.count("に") or node.surface.count("を"))and target=="":
                node2=node.prev
                if node2.surface.count(w[0]):
                    break
                if node2.prev.surface.count("の") and node2.feature.startswith("名詞"):
                    print(node2.feature)
                    target+=node2.prev.surface
                    target+=node2.surface
                #target+=node2.surface
            if node.surface.count("成功"):
                flag=1
            if node.surface.count("失敗"):
                flag=2
            node=node.next
            if flag!=0:
                print("flag:"+str(flag))
                print("ss:"+str(ss))
        ss=ss+1
        if flag!=0:
            break

    if flag==0:#成否が判明していなかったら出目で判断
        ld = open("playerskill.txt")#プレイヤーのスキル一覧ファイルを開く
        lines = ld.readlines()
        for line in lines:
            if line.startswith(w[0]):#一行ずつ見ていって探してる技能があったら技能値を確保
                skill=line.split()
                ld.close()
                break
        
        for n in range(RNG):
            if flag!=0:
                break
            checktxt=str(temp[n])
            if checktxt.startswith(subject):
                node=tagger.parseToNode(checktxt)
                while node:
                    if node.surface.isdigit():
                        if int(node.surface)<=skill[1]:
                            flag=1
                        else:
                            flag=2
                        break
                    node=node.next
    if flag==1:
        result=w[1]
    if flag==2:
        result=w[2]
    if flag==0:
        result=w[3]

#    if target=="":
        
    subject+="は"
    subject+=target
    subject+=result
    
    return subject
    
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')


file="playlog.txt"
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

logs=[]

f = open('out.txt', 'w') # 書き込みモードで開く

for i in range(len(playlog)):
    text=str(playlog[i])#playlog[i]が今見ているところ
    node = tagger.parseToNode(text)
    while node:
        for w in skills:
            if node.surface.count(w[0]):
                print("検出技能:"+node.surface)
                print(playlog[i])
                temp=[]
                for n in range(RNG):
                    temp.append(playlog[i+n-int(RNG/2)])
                logs.append(temp)
                print (temp)
                rrr=str(pickup(temp,w))
                print(rrr)
                f.writelines(rrr)
                f.write("\n")
        node=node.next
    text=text+"\n"
    text=re.sub('\[',"",text)
    text=re.sub('\]',"",text)
    text=re.sub('\'',"",text)
    f.writelines(text)
f.close()
