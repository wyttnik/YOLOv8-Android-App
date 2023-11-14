# -*- coding: utf-8 -*-

import os
from ultralytics import YOLO

trained_models = os.listdir("/usr/yolo_v8_app/results")
if (len(trained_models) != 0):
    last_trained_model_i = 0
    for i in range(0,len(trained_models)):
        if("train" in trained_models[i]):
            last_trained_model_i += 1
            
    last_trained_model = "/usr/yolo_v8_app/results/"+trained_models[last_trained_model_i-1]
    trained_model = YOLO(last_trained_model+"/weights/best.pt")
    results = trained_model.val(project="results")
    print(results.box.map50)