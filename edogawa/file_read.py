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
        if line.find("-------------------------------------------------------")!=-1:
            n=n+1
        if n<2 or line.find("-------------------------------------------------------")!=-1:
            line=""
        #print(line)
        line=line.replace("\n","")
        line=line.replace("　","")
        while line.find("［")!=-1 or line.find("《")!=-1:
            line=re.sub("［.*］","",line)
            line=re.sub("《.*》","",line)
        if line.find("「")==-1:
            line=line.replace("。","。\n")
        else:
            line=line.replace("「","\n「")
            line=line.replace("」","」\n")
            
        line=line.replace("\n\n","\n")
        wf.writelines(line)
f.close()
wf.close()
