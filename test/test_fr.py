# Class module for a Face Recognition wrapper

import numpy as np
import cv2

class rcg():
    def __init__(self, path=''):
        self.path = path

    def face_recognition(self, video_size):

        print("Starting Face Recognition")
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        xsize = int(video_size[0])
        ysize = int(video_size[1])
    
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, xsize)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ysize)

     
        while True:
            # Read the frame
            _, img = cap.read()

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display
            cv2.imshow('img', img)

            # Stop if escape key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the VideoCapture object
        cap.release()
        cv2.destroyAllWindows()