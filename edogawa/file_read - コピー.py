import os
import zipfile

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in find_all_files(os.getcwd()):
    if file.endswith(".zip"):
        print (file)
        #up2path=os.path.dirname(os.path.dirname(file))
        with zipfile.ZipFile(file, 'r') as post:
            for info in post.infolist():
                print(info.filename)
                if info.filename.endswith(".txt"):
                    f=open(os.path.join(file,info.filename),"r",encoding="utf-8")
                    lines=f.readlines()
                    for line in lines:
                        print(line)
                #print(post.read(info.filename))
                
