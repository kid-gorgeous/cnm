import os
import cv2
import sys
import numpy as np
import tensorflow as tf
import matplotlib as plt
from tensorflow import keras
from termcolor import colored
from sklearn.datasets import fetch_olivetti_faces, load_sample_image


print(colored("Tensorflow version: ", 'green'), tf.__version__)

# anticipate that the vgg face dataset is importable 


# Sequential method 
class ConvNET:

    def __init__(self, cwd, path_to_images):
        self.cwd = cwd
        self.path_to_images = path_to_images
        self.model = keras.models.Sequential([ ])

        pass

    def loadImages(self):
        pass

    def printNetInfo(self):
        print(colored("\nConvNET information: ", 'green'))
        print(colored('Working path to external hard drive: ', 'green'), self.path_to_images)
        print(colored('Current working path: ', 'green'), self.cwd)


    def SetModel(self):
        print(self.model.summary(...))

def printWorkingDir(path):
    print(colored("Working path to external hard drive: ", 'green'), path)
    

if __name__ == '__main__':
    path = '/Volumes/hd/Data/VGG-Face2/data/data/train'
    cwd = os.getcwd()

    ConvNET = ConvNET(cwd, path)
    ConvNET.printNetInfo()

    img_path = '/Volumes/hd/Data/VGG-Face2/samples_0.png'
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    train_file_path = '/Volumes/hd/Data/VGG-Face2/data/train_list.txt'
    file = open(train_file_path, 'r')
    print(colored("From the Test List","green"), file.read().splitlines()[:10])

    test_file_path = '/Volumes/hd/Data/VGG-Face2/data/test_list.txt'
    file = open(test_file_path, 'r')
    print(colored("From the Test List","green"), file.read().splitlines()[:10])

    train_img_path = '/Volumes/hd/Data/VGG-Face2/data/train/n000002/0001_01.jpg'
    



    
