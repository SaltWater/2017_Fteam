import sys
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

name="GM(石澤):「中華屋いこうぜ」"
test=[]
node=tagger.parseToNode(name)
while node:
    test.append(node.surface)
    node=node.next
print(test)

