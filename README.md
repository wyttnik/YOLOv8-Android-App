# Object Detection with YOLOv8

## Introduction
This repo allows to train model to classify objects as: coins, banknotes and bank cards

## How to use
Download code and open PowerShell inside folder. To build docker use:
```
docker build -t docker-yolo .
```

For training model use:

```
docker run --rm -it -v .\money_dataset:/usr/yolo_v8_app/datasets/money_dataset -v .\results:/usr/yolo_v8_app/results docker-yolo python3 train.py
```

For validation use:

```
docker run --rm -it -v .\money_dataset:/usr/yolo_v8_app/datasets/money_dataset -v .\results:/usr/yolo_v8_app/results docker-yolo python3 val.py
```
