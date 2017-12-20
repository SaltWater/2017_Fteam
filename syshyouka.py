import random
import sys
import MeCab
import re
import oreore
from operator import itemgetter


#print(oreore.syugo_pickup("と豊世がお倉に言った。"))


test=[1,2,3,4,5,6,7,8,9,10]
print(test)
#sorted(matchlist,key=itemgetter(1),reverse=True)
#test=sorted(test,key=itemgetter(1),reverse=False)
for t in range(len(test)):
    test[t]=1

print(test)
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')
tt="と、余は、所信を滔々と披瀝した。"
node=tagger.parseToNode(tt)
while node:
    print(node.surface+node.feature)
    node=node.next
