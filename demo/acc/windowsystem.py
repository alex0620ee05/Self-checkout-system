import numpy as np
import cv2
from threadedcapture import ThreadedCapture
import time


class WindowSystem () :
    
    
    def __init__ (self, GUI_SIZE) :
        
        # parameter settings
        #---------------------------------------------------------------------------------
        self.GUI_SIZE = GUI_SIZE
        self.h_border = 10
        self.w_border = 10
        self.camimg_h = 600
        self.camimg_w = 1060
        self.camimg_h_s = 160
        self.camimg_w_s = self.w_border
        self.camimg_h_e = self.camimg_h_s + self.camimg_h
        self.camimg_w_e = self.camimg_w_s + self.camimg_w
        self.usage_h_s = self.camimg_h_e + 5
        self.usage_w_s = self.w_border
        self.usage_h_e = self.GUI_SIZE[1] - self.h_border
        self.usage_w_e = self.usage_w_s + self.camimg_w
        self.payment_h = 99
        self.payment_w = 800
        self.payment_h_s = self.h_border
        self.payment_w_s = self.camimg_w_e + 20
        self.payment_h_e = self.payment_h_s + self.payment_h
        self.payment_w_e = self.payment_w_s + self.payment_w
        self.ntd_h = 90
        self.ntd_w = 398
        self.ntd_h_s = self.GUI_SIZE[1] - self.h_border - self.ntd_h
        self.ntd_h_e = self.GUI_SIZE[1] - self.h_border
        self.ntd_w_s = self.payment_w_s
        self.ntd_w_e = self.payment_w_s + self.ntd_w
        self.label_h = 51
        self.label_h_s = self.payment_h_e + 5
        self.label_h_e = self.label_h_s + self.label_h
        self.label_w_s = self.payment_w_s
        self.label_w_e = self.GUI_SIZE[0] - self.w_border
        self.itemdisp_h_s = self.label_h_e
        self.itemdisp_h_e = self.ntd_h_s - 5
        self.itemdisp_w_s = self.label_w_s
        self.itemdisp_w_e = self.label_w_e
        self.itembase_h_c = self.itemdisp_h_s + 50
        self.itembase_w_c = self.itemdisp_w_s + 19
        self.text1_w_s = self.itembase_w_c
        self.text1_w_e = self.itembase_w_c + 80
        self.text1base_h_e = self.itembase_h_c + 5
        self.text1base_h_s = self.text1base_h_e - 39
        self.text2_w = self.text1_w_s + 275
        self.text3_w = self.text2_w + 189
        self.text4_w = self.text3_w + 168
        self.paynow_h_s = self.ntd_h_s
        self.paynow_h_e = self.ntd_h_e
        self.paynow_w_s = self.ntd_w_e + 5
        self.paynow_w_e = self.GUI_SIZE[0] - self.w_border
        # print('Size of usage.jpg: ', self.usage_w_e - self.usage_w_s, ' x ', self.usage_h_e - self.usage_h_s)
        # print('Size of label.jpg: ', self.itemdisp_w_e - self.itemdisp_w_s, ' x (any)',)
        # print('Size of paynow.jpg: ', self.paynow_w_e - self.paynow_w_s, ' x ', self.paynow_h_e - self.paynow_h_s)
        #---------------------------------------------------------------------------------
        self.gui = np.empty( (self.GUI_SIZE[1], self.GUI_SIZE[0], 3), dtype="uint8" )
        self.item_cnt = 0
        # background color
        self.gui[:, :, :] = 255
        # logo
        logo = cv2.imread('../img/logo.jpg')
        self.gui[:logo.shape[0], :logo.shape[1], :] = logo
        # usage
        usage = cv2.imread('../img/usage.jpg')
        self.gui[self.usage_h_s:self.usage_h_e, self.usage_w_s:self.usage_w_e, :] = usage
        # payment
        payment = cv2.imread('../img/payment.jpg')
        self.gui[self.payment_h_s:self.payment_h_e, self.payment_w_s:self.payment_w_e, :] = payment
        # label
        label = cv2.imread('../img/label.jpg')
        self.gui[self.label_h_s:self.label_h_e, self.label_w_s:self.label_w_e, :] = label
        # item-display area
        self.gui[self.itemdisp_h_s:self.itemdisp_h_e, self.itemdisp_w_s:self.itemdisp_w_e, 0] = 230
        self.gui[self.itemdisp_h_s:self.itemdisp_h_e, self.itemdisp_w_s:self.itemdisp_w_e, 1] = 255
        self.gui[self.itemdisp_h_s:self.itemdisp_h_e, self.itemdisp_w_s:self.itemdisp_w_e, 2] = 245
        # ntd
        self.ntd = cv2.imread('../img/ntd.jpg')
        self.gui[self.ntd_h_s:self.ntd_h_e, self.ntd_w_s:self.ntd_w_e, :] = self.ntd
        # paynow
        print("label")
        print(self.paynow_h_s,self.paynow_w_s)
        paynow = cv2.imread('../img/paynow.jpg')
        self.gui[self.paynow_h_s:self.paynow_h_e, self.paynow_w_s:self.paynow_w_e, :] = paynow
        # Preparing chinese characters of items
        self.chars = {'banana':cv2.imread('../img/banana.jpg'), 'apple':cv2.imread('../img/apple.jpg'), 'orange':cv2.imread('../img/orange.jpg')}
    
    
    def PutCamImg (self, img):
        
        img = cv2.resize(img, (self.camimg_w, self.camimg_h), cv2.INTER_NEAREST)
        self.gui[self.camimg_h_s:self.camimg_h_e, self.camimg_w_s:self.camimg_w_e, :] = img
    
    
    def Item (self, text1, text2, text3, text4):
        
        item_h = self.itembase_h_c + self.item_cnt * 50
        text1_h_s = self.text1base_h_s + self.item_cnt * 50
        text1_h_e = self.text1base_h_e + self.item_cnt * 50
        cimg = self.chars[text1]
        self.gui[text1_h_s:text1_h_e, self.text1_w_s:self.text1_w_e, :] = cimg
        cv2.putText(self.gui, text2, (self.text2_w, item_h), cv2.FONT_HERSHEY_COMPLEX, 1.4, (200, 0, 0), 5)
        cv2.putText(self.gui, text3, (self.text3_w, item_h), cv2.FONT_HERSHEY_COMPLEX, 1.4, (200, 0, 0), 5)
        num4 = int(text4)
        text4_w = self.text4_w
        if (num4 < 100):
            text4_w += 28
        cv2.putText(self.gui, text4, (text4_w, item_h), cv2.FONT_HERSHEY_COMPLEX, 1.4, (200, 0, 0), 5)
        self.item_cnt += 1
    
    
    def NTD (self, number):
        
        cv2.putText(self.gui, str(number), (self.ntd_w_s + 175, self.ntd_h_s + 70), cv2.FONT_HERSHEY_COMPLEX, 2, (200, 0, 0), 6)
    
    
    def clear (self):
        
        self.gui[self.itemdisp_h_s:self.itemdisp_h_e, self.itemdisp_w_s:self.itemdisp_w_e, 0] = 230
        self.gui[self.itemdisp_h_s:self.itemdisp_h_e, self.itemdisp_w_s:self.itemdisp_w_e, 1] = 255
        self.gui[self.itemdisp_h_s:self.itemdisp_h_e, self.itemdisp_w_s:self.itemdisp_w_e, 2] = 245
        self.gui[self.ntd_h_s:self.ntd_h_e, self.ntd_w_s:self.ntd_w_e, :] = self.ntd
        self.item_cnt = 0
    
    
    def show (self) :
        
        cv2.imshow('Check Out So Easy', self.gui)



if __name__ == '__main__' :
    cap = ThreadedCapture(0)
    winsys = WindowSystem( (1900, 1000) )
    winsys.Item('banana', '24', 'x1', '24')
    winsys.Item('orange', '22', 'x2', '44')
    winsys.NTD(68)
    cnt = 0
    start = time.time()
    while True:
        img = cap.read()
        winsys.PutCamImg(img) 
        winsys.show()
        cnt += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    end = time.time()
    print( "fps: ", cnt / (end - start) )
