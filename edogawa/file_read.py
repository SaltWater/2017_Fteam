import sys
import os
import glob
import MeCab
import re
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')
test=glob.glob("*.txt")

for novel in test:
    n=0
    f=open(novel,'r')
    filename="../testfile/"+novel
    wf=open(filename,'w')
    print(filename)
    print(novel)
    lines=f.readlines()
    for line in lines:
        if n<16:
            line=""
            n=n+1
        #print(line)
        line=line.replace("\n","")
        line=re.sub("［.*］","",line)
        line=re.sub("《.*》","",line)
        
        if line.find("「")<0:
            line=line.replace("。","。\n")
        else:
            line=line.replace("「","\n「")
            line=line.replace("」","」\n")
            
        line=line.replace("\n\n","\n")
        wf.writelines(line)
f.close()
wf.close()
