import os
import shutil
os.makedirs("garbageGAN/datasets/data",exist_ok=True)
os.makedirs("garbageGAN/datasets/data/trainA",exist_ok=True)
os.makedirs("garbageGAN/datasets/data/trainB",exist_ok=True)
os.makedirs("yolox-pytorch/VOCdevkit",exist_ok=True)
os.makedirs("yolox-pytorch/VOCdevkit/VOC2007",exist_ok=True)
os.makedirs("yolox-pytorch/VOCdevkit/VOC2007/Annotations",exist_ok=True)
os.makedirs("yolox-pytorch/VOCdevkit/VOC2007/JPEGImages",exist_ok=True)
os.makedirs("yolox-pytorch/VOCdevkit/VOC2007/ImageSets",exist_ok=True)
os.makedirs("yolox-pytorch/VOCdevkit/VOC2007/ImageSets/Main",exist_ok=True)
os.makedirs("yolox-pytorch/test",exist_ok=True)
os.makedirs("yolox-pytorch/test/VOC2007",exist_ok=True)
os.makedirs("yolox-pytorch/test/VOC2007/Annotations",exist_ok=True)
os.makedirs("yolox-pytorch/test/VOC2007/JPEGImages",exist_ok=True)
os.makedirs("yolox-pytorch/test/VOC2007/ImageSets",exist_ok=True)
os.makedirs("yolox-pytorch/test/VOC2007/ImageSets/Main",exist_ok=True)

dataset="PersonDetect"

S_dir=dataset+"/S"
T_dir=dataset+"/T"
img_files=os.listdir(os.path.join(S_dir,"imgs"))
xml_files=os.listdir(os.path.join(S_dir,"xml"))
s=0
for i in img_files:
    s=s+1
    name=i.split(".")[0]
    oldpath=os.path.join(S_dir,"imgs",i)  
    newpath=os.path.join("garbageGAN/datasets/data/trainA",i)
    if s<=500:shutil.copy(oldpath,newpath)
    
    oldpath=os.path.join(S_dir,"imgs",i)  
    newpath=os.path.join("yolox-pytorch/VOCdevkit/VOC2007/JPEGImages",i)
    shutil.copy(oldpath,newpath)
    
    oldpath=os.path.join(S_dir,"xml",name+".xml")  
    newpath=os.path.join("yolox-pytorch/VOCdevkit/VOC2007/Annotations",name+".xml")
    shutil.copy(oldpath,newpath)

img_files=os.listdir(os.path.join(T_dir,"imgs"))
xml_files=os.listdir(os.path.join(T_dir,"xml"))
for i in img_files:
    name=i.split(".")[0]
    oldpath=os.path.join(T_dir,"imgs",i)  
    newpath=os.path.join("garbageGAN/datasets/data/trainB",i)
    shutil.copy(oldpath,newpath)
    
    oldpath=os.path.join(T_dir,"imgs",i)  
    newpath=os.path.join("yolox-pytorch/test/VOC2007/JPEGImages",i)
    shutil.copy(oldpath,newpath)
    
    oldpath=os.path.join(T_dir,"xml",name+".xml")  
    newpath=os.path.join("yolox-pytorch/test/VOC2007/Annotations",name+".xml")
    shutil.copy(oldpath,newpath)

fp=open(r"yolox-pytorch/test/VOC2007/ImageSets/Main/test.txt","w+")
imgdir=r"yolox-pytorch/test/VOC2007/JPEGImages"
files=os.listdir(imgdir)
for i in files:
    name=i.split(".")[0]
    fp.write(name+"\n")
fp.close()