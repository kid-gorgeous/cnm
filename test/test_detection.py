# Using OpenCV

# Class module for a Face Recognition wrapper
from termcolor import colored
import numpy as np
# import dlib
import cv2

class recognition():
    def __init__(self, path=''):
        self.path = path
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        # self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        self.scale = 1.1
        self.minNeighbors = 4

        self.xsize = 720
        self.ysize = 480

        self.blue = 52
        self.green = 206
        self.red = 235

    def face_recognition(self, video_size=[]):
        print(colored("Starting Face Recognition", 'green'))
        print(colored("Video Size: " + str(self.xsize) + "x" + str(self.ysize), 'green'))

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.xsize)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.ysize)
     
        while True:
            # Read the frame
            _, img = cap.read()

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect the faces
            faces = self.face_cascade.detectMultiScale(gray, self.scale, self.minNeighbors)

            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                # rectangle(img, pt1, pt2, color=(B,G,R), thickness=None, lineType=None, shift=None) -> img
                
                cv2.rectangle(img, (x, y), (x+w, y+h), (self.blue, self.green, self.red), 3)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)

                # dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
                # landmarks = self.predictor(gray, dlib_rect)
                
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (self.blue, self.green, self.red), 2)

                # for n in range(0, 68):
                #     x = landmarks.part(n).x
                #     y = landmarks.part(n).y
                #     cv2.circle(img, (x, y), 1, (255, 0, 0), -1)

            # Display
            cv2.imshow('img', img)

            # Stop if escape key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the VideoCapture object
        cap.release()
        cv2.destroyAllWindows()







if __name__ == '__main__':

    # Example: 
    video_size = ['720', '480']
    rcg = recognition()
    rcg.face_recognition(video_size)