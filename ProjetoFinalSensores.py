from google.colab import drive
drive.mount ("/content/gdrive")


!pip install -r requirements.txt

%cd /content/gdrive/MyDrive

import os
if not os.path.isdir("TheCodingBug"):
  os.makedirs("TheCodingBug")

%cd TheCodingBug


!pwd

!git clone https://github.com/WongKinYiu/yolov7.git 

Treinamento YoloV7

! pwd

cd yolov7

!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt



TREINO

!python train.py --device 0 --batch-size 16 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7x-custom.yaml --weights yolov7x.pt --name yolov7x-custom

!pwd

Teste Imagem

!python detect.py --weights runs/train/yolov7x-custom/weights/best2.pt --conf 0.5 --img-size 640 --source ../yolov7/data/train/images/videoparado.mp4 --no-trace
