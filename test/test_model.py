import test_vision as vision
import test_fr as fr
import numpy as np
import cv2

from sklearn.datasets import fetch_lfw_people



if __name__ == '__main__':
    video_size = ['640', '480']
    # video = vision.Video()
    # video.camera(video_size)
    fr = fr.rcg()
    fr.face_recognition(video_size)
    
