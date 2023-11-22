# !/usr/bin/env python
# -*- coding: utf-8 -*-
# !pip3 install opencv-python
# !pip3 install termcolor


import cv2
from termcolor import colored
print("Open CV version: ",cv2.__version__)


class Video():
    def __init__(self, path='', video_size=[]):
        self.video_size = video_size
        self.xsize = int(self.video_size[0])
        self.ysize = int(self.video_size[1])
        self.path = path

    def camera(self):
        print("Starting Camera")
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.xsize)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.ysize)
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    # Helper Function to record video ( might work )
    def capture(self):
        cap = cv2.VideoCapture(0)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

        while True:
            ret, frame = cap.read()
            if ret:
                # Write the frame
                out.write(frame)

                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Video saved")

    


if __name__ == '__main__':

    # Example: 
    video_size = ['720', '480']
    video = Video(video_size=video_size)
    video.camera()
