"""Face Detection and Cropping of the dataset"""

import numpy as np
import mediapipe as mp
import cv2
import os

mp_drawing = mp.solutions.drawing_utils

# load face detection model
mp_face = mp.solutions.face_detection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.5
)

path = "./FacePhotos"
new_path = "./FacePhotosCleaned/"

if not os.path.exists(new_path):
    os.makedirs(new_path)

for file in os.listdir(path):
    img = cv2.imread(path + "/" + file)
    image_input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mp_face.process(image_input)

    # By default mediapipe returns detection data in normalize form and we have to convert to original size by multiplying x values by width and y values by height of input image.
    # Get width and height of the image
    height, width, _ = img.shape
    detection_results= []
    for detection in results.detections:
        bbox = detection.location_data.relative_bounding_box
        bbox_points = {
            "xmin" : int(bbox.xmin * width),
            "ymin" : int(bbox.ymin * height),
            "xmax" : int(bbox.width * width + bbox.xmin * width),
            "ymax" : int(bbox.height * height + bbox.ymin * height)
        }
        detection_results.append(bbox_points)
    # Crop face from image
    for i, bbox in enumerate(detection_results):
        face = img[bbox['ymin']:bbox['ymax'], bbox['xmin']:bbox['xmax']]
        cv2.imwrite(new_path+file, face)