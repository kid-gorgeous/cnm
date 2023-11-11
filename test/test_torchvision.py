# Using Torch Vision and OpenCV

import os
import sys
import cv2
import torch
from termcolor import colored
from torchvision.models import ResNet50_Weights
import torchvision.transforms as transforms
import torchvision.models as models


# Define the transformation
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.ToTensor()
])


class Video():
    def __init__(self, video_size=[], device='mps'):

        # Load pre-trained model for ML inference
        self.model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
        self.device = torch.device(device) # For Mac
        # self.device = torch.device('cuda') # For Linux/Windows

        # Set Video Size
        self.video_size = video_size
        self.xsize = int(self.video_size[0])
        self.ysize = int(self.video_size[1])

        # Set Color
        self.blue = 52
        self.green = 206
        self.red = 235

        self.thickness = 3

        self.dtype = torch.float
        

    def open(self):
        # Open the webcam
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.xsize)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.ysize)

    def close(self):
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()


    def detection(self):
        print(colored("Starting Object Detection", 'green'))

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        print(colored("Video Size: " + str(self.xsize) + "x" + str(self.ysize), 'green'))
        
        # Parameters for face detection
        # scale: compensates for the fact that faces closer to the camera will appear bigger than those that are further away
        # minNeighbors: how many neighbors each candidate rectangle should have to retain it
        scale = 1.1
        minNeighbors = 4

        self.open()
        while True:
  
            # Read the frame
            _, img = self.cap.read()

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, scale, minNeighbors)

            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (self.blue, self.green, self.red), self.thickness)
                roi_gray = gray[y:y+h, x:x+w]

                cv2.imwrite('/Users/evan/cnm/test/frames/roi_gray.jpg', roi_gray) # writes one image to the folder
                

            # Display
            cv2.imshow('Camera 1', img)
            # cv2.imshow('Camera 2', gray)
  
            # Stop if escape key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        self.close()

    def train(self, folder_path='/Users/evan/cnm/test/frames'):    
        

        while True:
            # pulls grayscale image from frames folder
            gray = cv2.imread('f{folder_path}/roi_gray.jpg')




            cv2.imshow('Grayscale Picture', gray)
            # Stop if escape key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        



if __name__ == '__main__':

    # Example:
    video_size = ['720', '480']
    video = Video(video_size)
    # video.detection()
    video.train()


    pass