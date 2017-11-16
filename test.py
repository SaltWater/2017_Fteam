import sys
import MeCab
tagger = MeCab.Tagger("mecabrc")
tagger.parse('')

name="高橋さんが、にが笑いをして、いいました。"
test=[]
node=tagger.parseToNode(name)
while node:
    print(node.surface+node.feature)
    test.append(node.surface)
    node=node.next
print(test)

