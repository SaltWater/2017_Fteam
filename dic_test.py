import sys
import MeCab
tagger1 = MeCab.Tagger("mecabrc")
tagger1.parse('')

while True:
    text=input('check>>')
    print(tagger1.parse (text))
