import cv2
import torch
from termcolor import colored
from torchvision.models import ResNet50_Weights
import torchvision.transforms as transforms
import torchvision.models as models
# import torch.onnx as onnx


# Define the transformation
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.ToTensor()
])


class Video():
    def __init__(self, video_size=[], device='cpu'):


        # Load pre-trained model for ML inference
        self.model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
        self.device = torch.device('mps') # For Mac
        # self.device = torch.device('cuda') # For Linux/Windows

        # Set Video Size
        self.video_size = video_size
        self.xsize = int(self.video_size[0])
        self.ysize = int(self.video_size[1])

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
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display
            cv2.imshow('img', img)

            # Stop if escape key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.close()





# def detection(output):
#     # Apply a threshold to filter out low-confidence detections
#     confidence_threshold = 0.5
#     high_confidence_detections = outputs[outputs[:, 4] > confidence_threshold]

#     # Each row in `high_confidence_detections` is now a detection with format (x1, y1, x2, y2, score, class)
#     for detection in high_confidence_detections:
#         print(detection)

# model = models.to(device)
# model.eval()



if __name__ == '__main__':

    # Example:
    video_size = ['720', '480']
    video = Video(video_size)

    while True:
        video
        
    else:
        video.close()

    pass