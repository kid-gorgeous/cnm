import os
import sys
import cv2
from PIL import Image

path = './'
path_to_vgg = '/Volumes/drive/fun/VGG-Face2/sample_0.png'

xsize = 720
ysize = 480

cap = cv2.VideoCapture(path_to_vgg)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, xsize)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ysize)

img = cap.imread(path_to_vgg)
cv2.imshow('img', img)