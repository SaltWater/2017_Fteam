import sys
import os
import glob
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')
test=glob.glob("*.txt")

for novel in test:
    f=open(novel,'r')
    filename="../testfile/test"+novel
    wf=open(filename,'w')
    print(filename)
    print(novel)
    lines=f.readlines()
    for line in lines:
        #print(line)
        line=line.replace("\n","")
        line=line.replace("「","\n「")
        line=line.replace("」","」\n")
        line=line.replace("。","。\n")
        wf.writelines(line)
f.close()
wf.close()
