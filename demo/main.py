import cv2   
import ctypes
import numpy as np
import SSD 
from threadedcapture import ThreadedCapture
import time
import windowsystem as window_system

ll = ctypes.cdll.LoadLibrary
lib = ll("./tfssdtest.so")
#lib = ll("./ssdhardnet.so")
lib.process.restype = ctypes.c_int

cam = ThreadedCapture(0)
win_sys = window_system.WindowSystem((1900,1000))

frame_count = 0
time_start = time.time()
total_call_func_time = 0

CLASS_NUM = 91
class_table = dict([(44,"bottle"),(47,"cup"),(48,"fork"),(50,"spoon"),(51,"bowl"),(52,"banana"),(53,"apple"),(55,"orange"),(58,"hot dog"),(60,"donut"),(87,"scissors")])

frame = cam.read()
print(frame.shape[1],frame.shape[0])
x_scale = frame.shape[1]/300
y_scale = frame.shape[0]/300

while True:  
    objects_cnt = np.zeros(CLASS_NUM,dtype='int')
    frame_count+=1;  
    frame = cam.read()
    
    # DPU function
    frame_resized = cv2.resize(frame,(300,300))
    call_func_start =time.time()
    size , data = SSD.detect(lib,frame_resized)
    call_func_end = time.time()
    total_call_func_time += (call_func_end - call_func_start)
    
    # bounding box on frame
    for i in range(int(int(size)/6)):
        #print(data[i+0],data[i+1],data[i+2],data[i+3],data[i+4],data[i+5])
        cv2.rectangle(frame, (int(data[i*6+1]*x_scale),int(data[i*6+2]*y_scale)), (int(data[i*6+3]*x_scale),int(data[i*6+4]*y_scale)), (255,0,0),5)
        cv2.putText(frame, class_table[int(data[i*6])],(int(data[i*6+1]*x_scale+5),int(data[i*6+4]*y_scale-5)) , cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 2)
        objects_cnt[int(data[i*6])]+=1
        #print(time.time()-update_time)

    # show on screen
    win_sys.clear()
    for i in range(CLASS_NUM):
        if objects_cnt[i]!=0:
            win_sys.Add_result(i,objects_cnt[i])
            
    win_sys.show(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
time_end = time.time()
print("fps              :  ",frame_count/(time_end-time_start))
print("dpu average time :  ",total_call_func_time/frame_count,"s")
cv2.destroyAllWindows() 
