# **Running the project**

* Following steps are on the target(ZCU104):

If all settings are done, put this directory into `/home/root/`.
**1. Install Vitis-AI-Library on target(ZCU104):**
    Ref:https://github.com/Xilinx/Vitis-AI/tree/master/Vitis-AI-Library  --Setting Up the Target
    
**2. Excute the Self-checkout-system demo** 
    -object detection from video source:    
    `python3 DEMO.py -v <mp4 video file>`
    -real time checkout-system with camera:
    `python3 DEMO.py -c True`

