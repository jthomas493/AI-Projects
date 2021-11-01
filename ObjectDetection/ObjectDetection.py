# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from imageai.Detection import ObjectDetection
import os

path = os.getcwd()

obj_detector = ObjectDetection()
obj_detector.setModelTypeAsRetinaNet()
obj_detector.setModelPath(os.path.join(path,"resnet50_coco_best_v2.1.0.h5"))
obj_detector.loadModel()
detections = obj_detector.detectObjectsFromImage(input_image= os.path.join(path,"testImage2.jpg"), output_image_path = os.path.join(path, "result-image2.jpg"), extract_detected_objects=True)