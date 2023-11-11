import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib as plt
from tensorflow import keras
from termcolor import colored
from sklearn.datasets import fetch_olivetti_faces, load_sample_image

print(colored("Tensorflow version: ", 'green'), tf.__version__)

# anticipate that the vgg face dataset is importable 
class Neuron: 
    def __init__(self):
        pass

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


    def getModel(self):
        return self.model  

def printWorkingDir(path):
    print(colored("Working path to external hard drive: ", 'green'), path)
    

if __name__ == '__main__':
    path = '/Volumes/drive/fun/VGG-Face2/data/train'
    cwd = os.getcwd()

    ConvNET = ConvNET(cwd, path)
    ConvNET.printNetInfo()

    img_path = '/Volumes/drive/fun/VGG-Face2/samples_0.png'
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    train_file_path = '/Volumes/drive/fun/VGG-Face2/data/train_list.txt'
    file = open(train_file_path, 'r')
    print(colored("From the Test List","green"), file.read().splitlines()[:10])

    test_file_path = '/Volumes/drive/fun/VGG-Face2/data/test_list.txt'
    file = open(test_file_path, 'r')
    print(colored("From the Test List","green"), file.read().splitlines()[:10])

    train_img_path = '/Volumes/drive/fun/VGG-Face2/data/train/n000002/0001_01.jpg'
    
    image = cv2.imread(train_img_path, cv2.IMREAD_GRAYSCALE)
    image_arr = np.array([image])
    batch_size, height, width, channels = image_arr.shape

    # Create 2 filters
    filters = np.zeros(shape=(7, 7, channels, 2), dtype=np.float32)
    filters[:, 3, :, 0] = 1 # vertical line
    filters[3, :, :, 1] = 1 # horizontal line

    outputs = tf.nn.conv2d(image_arr, filters, strides=1, padding="SAME")
    plt.imshow(outputs[0, :, :, 1], cmap="gray") # plot 1st image's 2nd feature map
    plt.show()

    print(colored("Batch size: ", 'green'), batch_size)
    print(colored("Height: ", 'green'), height)
    print(colored("Width: ", 'green'), width)
    print(colored("Image shape: ", 'green'), image.shape)
    print(colored("Image type: ", 'green'), type(image))




    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
