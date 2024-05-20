import os 
import shutil
imgdir="yolox-pytorch/VOCdevkit/VOC2007/JPEGImages"
xmldir="yolox-pytorch/VOCdevkit/VOC2007/Annotations"
T_imgdir="garbageGAN/results/PD_garbageGAN/train_latest/images/fake_B"

dataset="PersonDetect"

S_imgdir=dataset+"/S/imgs"
S_xmldir=dataset+"/S/xml"

files=os.listdir(T_imgdir)
for i in files:
    name=i.split(".")[0]
    oldname=os.path.join(T_imgdir,i)
    newname=os.path.join(imgdir,name+"_fake.jpg")
    shutil.copy(oldname,newname)
    oldname=os.path.join(S_xmldir,name+".xml")
    newname=os.path.join(xmldir,name+"_fake.xml")
    shutil.copy(oldname,newname)
    
