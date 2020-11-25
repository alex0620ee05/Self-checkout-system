import cv2
from threading import Thread
import time



class ThreadedCapture ():
    
    
    def __init__(self, src=0):
        
        self.cap = cv2.VideoCapture('filesrc location=object_vid.mp4 ! qtdemux ! queue ! h264parse ! omxh264dec ! queue ! videoconvert ! queue ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER)
        self.fps = 60
        self.delay = 1 / self.fps
        #self.cnt=0
        # Start frame retrieval thread
        self.thread = Thread( target=self.update, args=() )
        self.thread.daemon = True
        self.thread.start()
        time.sleep(0.3)
        
    
    def update(self):
        
        while True:
            #self.cnt+=1
            _, self.img = self.cap.read()
            #time.sleep(self.delay)
    
    
    def read(self):
        #_, self.img = self.cap.read()
        #_, self.img = self.cap.read()
        #_, self.img = self.cap.read()
        #_, self.img = self.cap.read()
        #print(self.cnt)
        return self.img
