import numpy as np
import cv2
from threadedcapture import ThreadedCapture
import time

class_table = dict([(44,"coke"),(47,"cup"),(48,"fork"),(50,"spoon"),(51,"bowl"),(52,"banana"),(53,"apple"),(55,"orange"),(58,"hot dog"),(60,"donut"),(87,"scissors")])
price_table = dict([(44,      1.89),(47,   2.00),(48,    1.20),(50,     1.30),(51,    1.40),(52,     0.59),(53,     1.15),(55,      0.99),(58,       1.25),(60,     2.49),(87,       5.50)])

class WindowSystem () :
    
    
    def __init__ (self, GUI_SIZE) :
        
        # parameter settings
        self.GUI_SIZE = GUI_SIZE
        self.gui = np.empty( (self.GUI_SIZE[1], self.GUI_SIZE[0], 3), dtype="uint8" )
        self.gui[:, :, :] = 255
        
        # logo
        self.PutImg(0, 0, 'logo.jpg')
        
        # camera img (size & position)
        self.camimg_x = 160
        self.camimg_y = 10
        self.camimg_h = 600
        self.camimg_w = 1060

        # usage
        self.usage_x = 765
        self.usage_y = 10
        self.PutImg(self.usage_x, self.usage_y, 'usage.jpg')
        
        # payment
        self.payment_x = 10
        self.payment_y = 1090
        self.PutImg(self.payment_x, self.payment_y, 'payment.jpg')
        
        # label
        self.label_x = 114
        self.label_y = 1090
        self.PutImg(self.label_x, self.label_y, 'label.png')
        
        # space for item list 
        self.itemdisp_x = 165
        self.itemdisp_y = 1090
        self.itemdisp_h = 730
        self.itemdisp_w = 800
        self.gui[self.itemdisp_x:self.itemdisp_x+self.itemdisp_h, self.itemdisp_y:self.itemdisp_y+self.itemdisp_w, 0] = 230
        self.gui[self.itemdisp_x:self.itemdisp_x+self.itemdisp_h, self.itemdisp_y:self.itemdisp_y+self.itemdisp_w, 1] = 255
        self.gui[self.itemdisp_x:self.itemdisp_x+self.itemdisp_h, self.itemdisp_y:self.itemdisp_y+self.itemdisp_w, 2] = 245
                
        # ntd
        self.ntd_x = 900
        self.ntd_y = 1090
        self.PutImg(self.ntd_x, self.ntd_y, 'ntd.jpg')
        
        # paynow
        self.paynow_x = 900
        self.paynow_y = 1493
        self.PutImg(self.paynow_x, self.paynow_y, 'paynow.jpg')
        #---------------------------------------------------------------------------------
        
        self.item_x = 210
        self.text_1 = 1110
        self.text_2 = 1400
        self.text_3 = 1600
        self.text_4 = 1760
        
        self.item_cnt = 0
        self.price = 0
           
    def PutImg(self, x, y, img_name):
        img = cv2.imread('./img/'+img_name)
        self.gui[x:x+img.shape[0], y:y+img.shape[1]] = img
        
    def PutCamImg (self, img):
        img = cv2.resize(img, (self.camimg_w, self.camimg_h), cv2.INTER_NEAREST)
        self.gui[self.camimg_x:self.camimg_x+img.shape[0], self.camimg_y:self.camimg_y+img.shape[1], :] = img
    
    def Add_result(self,object_class,object_num):
        text1 = class_table[object_class]
        text2 = str(format(price_table[object_class], '.2f'))
        text3 = str(object_num)
        text4 = str(format(price_table[object_class]*object_num, '.2f'))
        cv2.putText(self.gui, text1,(self.text_1, self.item_x + 60*self.item_cnt) , cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 2)
        cv2.putText(self.gui, text2,(self.text_2, self.item_x + 60*self.item_cnt) , cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 2)
        cv2.putText(self.gui, text3,(self.text_3, self.item_x + 60*self.item_cnt) , cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 2)
        cv2.putText(self.gui, text4,(self.text_4, self.item_x + 60*self.item_cnt) , cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 2)
        
        self.item_cnt += 1
        self.price += price_table[object_class]*object_num

        
    def clear (self):
        
        self.gui[self.itemdisp_x:self.itemdisp_x+self.itemdisp_h, self.itemdisp_y:self.itemdisp_y+self.itemdisp_w, 0] = 230
        self.gui[self.itemdisp_x:self.itemdisp_x+self.itemdisp_h, self.itemdisp_y:self.itemdisp_y+self.itemdisp_w, 1] = 255
        self.gui[self.itemdisp_x:self.itemdisp_x+self.itemdisp_h, self.itemdisp_y:self.itemdisp_y+self.itemdisp_w, 2] = 245
        self.PutImg(self.ntd_x, self.ntd_y, 'ntd.jpg')
        self.item_cnt = 0
        self.price = 0
    
    def show (self, img) :
        # show price
        cv2.putText(self.gui, str(format(self.price, '.2f')), (self.ntd_y + 200, self.ntd_x + 70), cv2.FONT_HERSHEY_COMPLEX, 2, (200, 0, 0), 6)
        
        # paste image 
        img = cv2.resize(img, (self.camimg_w, self.camimg_h), cv2.INTER_NEAREST)
        self.gui[self.camimg_x:self.camimg_x+img.shape[0], self.camimg_y:self.camimg_y+img.shape[1], :] = img
        gui = cv2.resize(self.gui,(1200,660))
        cv2.imshow('Check Out So Easy', gui)
