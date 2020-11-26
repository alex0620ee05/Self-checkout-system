# **Self-checkout-system**
#### Self-checkout system for Adaptive Computing Developer Contest with Xilinx 2020 

#### Team MAAX

<p align="center">
  <img src="github_images/IMG20201125172027.jpg" >
</p>

## Build and Setup the Environment of the ZCU104 board 

### Build Steps

**1. Clone the full repository (including submodules)**

``$ git clone --recurse-submodules https://github.com/alex0620ee05/Self-checkout-system``

**Note: Vitis Patch Required:** This design has a large rootfs, and Vitis 2020.1 has an issue packaging SD card images with ext4 partitions over 2GB. This patch changes the packaging flow to round up the initial rootfs size to the first full multiple of 512MB over the ext4 partition size. To install it:

`$ cp ./vitis_patch/mkfsImage.sh ${XILINX_VITIS}/scripts/vitis/util`

**2. Source Vitis2020.1, PetaLinux2020.1 and XRT2020.1**

    $ source ${XILINX_VITIS}/settings64.sh
    $ source ${XILINX_PetaLinux}/settings.sh
    $ source ${XILINX_XRT}/setup.sh
    
**3. Build the hardware platform**

    $ cd 02-ivas-ml/platform/dev/zcu104_vcu
    $ make

* It's possible that errors occur when `petalinux-config kernel`, `petalinux-build`, `petalinux-build --sdk`. You should properly modify `Makefile` in `02-ivas-ml/platform/dev/zcu104_vcu` and `02-ivas-ml/platform/dev/zcu104_vcu/petalinux` to re do the command which got error(`make` again in `02-ivas-ml/platform/dev/zcu104_vcu`)

### Reference

<https://github.com/Xilinx/Vitis-In-Depth-Tutorial/tree/master/Runtime_and_System_Optimization/Design_Tutorials/02-ivas-ml>
