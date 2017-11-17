import os
import shutil
import zipfile

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in find_all_files(os.getcwd()):
    if file.endswith(".zip"):
        print (file)
        up2path=os.path.dirname(os.path.dirname(file))
        with zipfile.ZipFile(file, 'r') as post:
            for info in post.infolist():
                print(info.filename)
                outpath=os.path.join(up2path,info.filename)
                print(outpath)
                shutil.copyfile(outpath,info.filename)
