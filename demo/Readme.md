# **Running the project**

* Following steps are on the target(ZCU104):

  If all settings are done, put the directory `demo` into `/home/root/`.    

**1. Revise the display resolution**  

    sh set_monitor.sh  
**2. Excute the Self-checkout-system demo**  
* You need to use the `sd_card.img` in [vcu_decode/](https://github.com/alex0620ee05/Self-checkout-system/tree/main/prebuilt/sd_card_image/vcu_decode)  
  ### Real time checkout-system with camera:   
      python3 DEMO.py -c True 
  ### Checkout-system with video source:   
      python3 DEMO.py -v <mp4 video file>  
    
 

