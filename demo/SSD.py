import cv2   
import ctypes
import numpy as np
def detect(lib,frame):
  frame_data = np.asarray(frame, dtype=np.uint8)
  frame_data = frame_data.ctypes.data_as(ctypes.c_char_p)
  data = (ctypes.c_float * 120)()
  size=lib.process(frame.shape[0], frame.shape[1], frame_data,data)
  return size ,data
