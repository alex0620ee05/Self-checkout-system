# **Self-checkout-system**
#### Self-checkout system for Adaptive Computing Developer Contest with Xilinx 2020 

#### Team MAAX

<p align="center">
  <img src="github_images/IMG20201125172027.jpg" >
</p>

## Build and Setup the Environment of the ZCU104 board 

### Build Steps

**Note: Vitis Patch Required:** This design has a large rootfs, and Vitis 2020.1 has an issue packaging SD card images with ext4 partitions over 2GB. This patch changes the packaging flow to round up the initial rootfs size to the first full multiple of 512MB over the ext4 partition size. To install it:

`$ cp ./vitis_patch/mkfsImage.sh ${XILINX_VITIS}/scripts/vitis/util`

**1. Clone the full repository (including submodules)**

``$ git clone --recurse-submodules https://github.com/alex0620ee05/Self-checkout-system``



### Reference

<https://github.com/Xilinx/Vitis-In-Depth-Tutorial/tree/master/Runtime_and_System_Optimization/Design_Tutorials/02-ivas-ml>
