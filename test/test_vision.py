
import cv2
print("Open CV version: ",cv2.__version__)


class Video():
    def __init__(self, path=''):
        self.path = path

    def camera(self, video_size):

        xsize = int(video_size[0])
        ysize = int(video_size[1])

        print("Starting Camera")

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, xsize)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ysize)
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
    # video_size = ['720', '480']
    # video = Video()
    # video.camera(video_size)


    pass