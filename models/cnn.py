import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib as plt
from tensorflow import keras
from termcolor import colored
from sklearn.datasets import fetch_olivetti_faces

print(colored("Tensorflow version: ", 'green'), tf.__version__)

# anticipate that the vgg face dataset is importable 
class Neuron: 
    def __init__(self):
        pass


class ConvNET:

    def __init__(self, cwd, path_to_images):
        self.cwd = cwd
        self.path_to_images = path_to_images
        self.model = None
        pass

    def printNetInfo(self):
        print(colored("\nConvNET information: ", 'green'))
        print(colored('Working path to external hard drive: ', 'green'), self.path_to_images)
        print(colored('Current working path: ', 'green'), self.cwd)
        print(colored('Model: ', 'green'), str(self.model))

    def setModel(self, model):
        model = model + '()'

        if model == 'Functional()':
            self.model = keras.Functional()
        elif model == 'Functional()':
            self.model = keras.Sequential()


    def getModel(self):
        return self.model    

     def    

    

if __name__ == '__main__':
    path = '/Volumes/drive/fun/VGG-Face2'
    cwd = os.getcwd()

    ConvNET = ConvNET(cwd, path)
    # set model
    ConvNET.setModel('Sequential')

    # return the name of the number
    model = ConvNET.getModel()
    ConvNET.printNetInfo()