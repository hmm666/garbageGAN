# garbageGAN
基于garbageGAN的目标检测增强

## 简介：
通过迁移学习的方式对目标检测训练数据集进行迁移，达到扩充数据集的目的,进而提升模型的准确率，整个项目包括两部分：迁移部分和目标检测部分，两部分是分开的，整个流程是先对数据集进行迁移，再进行目标检测模型训练

## 数据集
数据集放在迁移和目标检测项目同级目录，在进行迁移和目标检测时，会从该数据集复制对应图像到对应的位置

数据集标注文件为xml格式，文件目录结构如下：

```
数据集名/
│
├─S/
│ └─imgs
| └─xml
├─T/
| └─imgs
| └─xml
```
将图像放在img中，同名xml标注文件放在xml中，其中S、T代表迁移方向（比如若要将马的图像迁移成斑马图像，这时S中放马的图像，T中放斑马的图像）

## 环境配置
- 克隆该项目
```
git clone https://github.com/hmm666/garbageGAN.git
cd garbageGAN
```
- 安装依赖库
```
pip install -r requirements.txt
```
部分依赖库可能由于优化问题会报错，网上大多有解决方法

## 项目流程
- 运行脚本将图像复制到迁移部分的对应位置,运行前需要到代码中修改数据集路径，line19:dataset
```
python copyimg.py
```
- 训练图像迁移模型
```
cd garbageGAN
python train.py --dataroot ./datasets/data --name PD_garbageGAN  --model garbageGAN
```
--name 存储训练日志以及模型权重的文件夹名，位置在./garbageGAN/checkpoints/

更多参数设置详见./garbageGAN/options/代码里

- 对图像数据集进行迁移
```
python test.py --dataroot ./datasets/data --name PD_garbageGAN  --phase train --model garbageGAN --num_test 1144
```
--num_test 迁移图像数量，应与dataset/S/imgs/里的图像数量保持一致
默认选择最近的模型权重进行迁移，若迁移效果不佳，可利用以下操作选择其它世代的权重进行迁移
```
cp checkpoints/PD_garbageGAN/200_net_G.pth  checkpoints/PD_garbageGAN/latest_net_G.pth
 ```
迁移后的图像保存在./garbageGAN/results/PD_garbageGAN/
- 运行脚本将迁移后的图像数据加入到目标检测训练数据集,同样需要在代码中更改数据集名
  line7:dataset
```
cd ../
python copy_transferedimg.py
```
- 生成目标检测训练数据索引
  
  需要在yolox-pytorch/voc_annotation.py中修改class文件路径
```
cd yolox-pytorch
python voc_annotation.py
```
- 训练目标检测模型
  
  需要在yolox-pytorch/train.py中修改类别文件路径和模型预训练权重路径

  预训练权重：https://pan.baidu.com/s/19b5UJviAPQHpXEgmDJt6ug?pwd=awg8 提取码：awg8，同时训练好的目标检测模型权重也在该云盘
```
python train.py
```
- 计算评估指标
  
  需要在yolox-pytorch/yolo.py，get_map.py里修改类别文件路径和模型权重路径
```
python get_map.py
```
结果保存在yolox-pytorch/map_out里面
