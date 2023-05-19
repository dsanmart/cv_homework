import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def load_face_data(path="./FacePhotosCleaned"):
    """Function to load the face dataset and return the cropped faces and labels"""
    faces = []
    labels = []
    for file in os.listdir(path):
        img = cv2.imread(path + "/" + file)
        faces.append(img)
        labels.append(file.split(".")[0]) # get the name of the person from the file name
    return faces, labels
        

def plt_imshow(title, image):
    """Function to display images in Jupyter Notebooks and Google Colab.
    Converts the image frame BGR to RGB color space and display it.
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.grid(False)
    plt.show()