import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 

# get all files from directory
def getFilesList(root):
    listOfFiles = []
    listOfFolder = os.listdir(root)
    for folder in listOfFolder:
        if not folder.endswith('jpg'):
            listOfFiles.extend(os.listdir(root + '/'+folder))
    return listOfFiles

root = 'F:\Python Project\Python_Fake Currency Detection/0010.jpg'


print(next(os.walk(root))[2])