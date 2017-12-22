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
