# **Self-checkout-system**
#### Self-checkout system for Adaptive Computing Developer Contest with Xilinx 2020 

#### Team MAAX

<p align="center">
  <img src="github_images/IMG20201125172027.jpg" >
</p>

### Step 1 : Build and Setup the Environment of the ZCU104 board 

See <https://github.com/alex0620ee05/Self-checkout-system/blob/main/Build_sdcard/README.md> for more details
  
### Step 2 :Preparing the SD Card for Vitis AI Library v1.2

See <https://github.com/alex0620ee05/Self-checkout-system/blob/main/set_up_files/README.md> for more details

### Step 3 :Vitis-AI quantization and compilation  
Use Docker to build Vitis-AI environment  
See <>for more details  
### Step 4 :Evaluate this project on board  
If the above steps are completed , copy the `DEMO` file to target(ZCU104).  
run `python3 DEMO.py -v <mp4 video filename>` to start demo!  
### Reference
Xilinx Vitis-AI quantizer & compiler / Xilinx Vitis-Ai-Library [Xilinx/Vitis-AI](https://github.com/Xilinx/Vitis-AI)  
<https://github.com/Xilinx/Vitis-In-Depth-Tutorial/tree/master/Runtime_and_System_Optimization/Design_Tutorials/02-ivas-ml>
