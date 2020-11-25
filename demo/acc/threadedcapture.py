import cv2
from threading import Thread
import time

class ThreadedCapture ():
    
    def __init__(self, src=0):        
        self.cap = cv2.VideoCapture(src)
        self.fps = 20
        self.delay = 1 / self.fps
        # Start frame retrieval thread
        self.thread = Thread( target=self.update, args=() )
        self.thread.daemon = True
        self.thread.start()
        time.sleep(0.3)
    
    def update(self):
        while True:
            _, self.img = self.cap.read()
            time.sleep(self.delay)
    
    def read(self):
        return self.img