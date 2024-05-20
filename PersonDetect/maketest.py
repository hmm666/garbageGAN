import os
dir="JPEGImages"

fp=open("ImageSets/Main/test.txt","w+")
files=os.listdir(dir)
for i in files:
    name=i.split("-")[0]
    n=i.split(".")[0]
    if name[11]=="E" or name[11]=="F":
        fp.write(n+"\n")

fp.close()