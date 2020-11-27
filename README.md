# **Self-checkout-system**
#### Self-checkout system for Adaptive Computing Developer Contest with Xilinx 2020 

#### Team MAAX

<p align="center">
  <img src="github_images/IMG20201127164739.jpg" >
</p>

### [Step 1 : Build and Setup the Environment of the ZCU104 board](https://github.com/alex0620ee05/Self-checkout-system/blob/main/Build_sdcard)   
**If you use the `sd_card.img` in `prebuilt/`, you can skip these steps. (5.)** 

## Build Steps

**1. Clone the full repository (including submodules)**

    $ git clone --recurse-submodules $ git clone --recurse-submodules https://github.com/Xilinx/Vitis-In-Depth-Tutorial
    $ cd Vitis-In-Depth-Tutorial/Runtime_and_System_Optimization/Design_Tutorials/02-ivas-ml/

**Note: Vitis Patch Required:** This design has a large rootfs, and Vitis 2020.1 has an issue packaging SD card images with ext4 partitions over 2GB. This patch changes the packaging flow to round up the initial rootfs size to the first full multiple of 512MB over the ext4 partition size. To install it:

`$ cp ./vitis_patch/mkfsImage.sh ${XILINX_VITIS}/scripts/vitis/util`

**2. Source Vitis2020.1, PetaLinux2020.1 and XRT2020.1**

    $ source ${XILINX_VITIS}/settings64.sh
    $ source ${XILINX_PetaLinux}/settings.sh
    $ source ${XILINX_XRT}/setup.sh
    
**3. Build the hardware platform**

    $ cd platform/dev/zcu104_vcu
    $ make

* It's possible that errors occur when `petalinux-config kernel`, `petalinux-build`, `petalinux-build --sdk`. You should properly modify `Makefile` in `platform/dev/zcu104_vcu` and `platform/dev/zcu104_vcu/petalinux` to re do the command which got errors(`make` again in `platform/dev/zcu104_vcu`)

**4. Build the Vitis design(Adding the DPU ip)**

One time, and one time only, you must apply the patch in the hw_src directory against the Vitis Vision library.

    $ cd ../../../hw_src/Vitis_Libraries
    $ patch -p1 < ../vision_lib_area_resize_ii_fix.patch
    
    $ cd ..
    $ cp ../../../../../dpu_conf_zcu104.vh .
    $ cp ../../../../../zcu10x_config .
    $ make

**5. Get the SD card image**
  
  After above steps, you will get `sd_card.img` in `sd_card_zcu104/`.
  
  Or, you can download the prebuilt `sd_card.img`. (See [SD card image](https://github.com/alex0620ee05/Self-checkout-system/tree/main/prebuilt/sd_card_image))  
### [Step 2 :Preparing the SD Card for Vitis AI Library v1.2](https://github.com/alex0620ee05/Self-checkout-system/tree/main/set_up_files)  
* **All of following steps in this section are on the target(ZCU104 board)**

* The following files and directories should be put into `/home/root/` :
  1. `jsons/` 
  2. `scripts/`
  3. `test_data/`
  4. `.bashrc`
  5. `debug.ini`
  
* The following file should be put into `/` :
  1. `update.tar.gz`

**1. Resize rootfs**

    cd /home/root/scripts
    sh ext4_auto_resize.sh

**2. Install the dependencies and Vitis AI library v1.2**

The following steps needs the board to have a path to the internet(script uses wget to download)  
    
    cd /home/root/scripts
    sh update.sh
    sh install_vai.sh  
### [Step 3 :Vitis-AI quantization and compilation](https://github.com/alex0620ee05/Self-checkout-system/tree/main/host)  
**The compiled file `ssd_mobilenet_v2_coco_tf.elf` is already in `demo/`, you can skip this step and directly use the provided file**  
**1. Build Vitis-AI environment**  
Follow the steps on https://github.com/Xilinx/Vitis-AI/blob/master/README.md to build docker.  
`./docker_run.sh xilinx/vitis-ai-gpu:latest`  
**2. Download tensorflow models from Xilinx AI model zoo ** 
You can get models by following the instructions on https://github.com/Xilinx/Vitis-AI/tree/master/AI-Model-Zoo  
In our project , we use xilinx_model_sample/tf_ssdmobilenetv2_coco_300_300_3.75G as our object detection model.  
Copy `xilinx_model_sample/tf_ssdmobilenetv2_coco_300_300_3.75G/quantized/deploy_model.pb` to `host/ssd_mobilenet`.  
**3. Compile the tensorflow model**  
After excuting`./ssdmobilenet_compile_b4096.sh`,you will get dpu_ssd_mobilenet_v2_coco_tf.elf  
### [Step 4 :Cross-compile the DPU inference code](github.com/alex0620ee05/Self-checkout-system/tree/main/Vitis-AI/Vitis-AI-Library/overview/demo/tfssd_mobilenet)  
**The compiled file `tfssdtest.so` is already in `/demo`, you can skip this step and directly use the provided file**  
**1. Setting Up the Host**  
Follow the steps on [Xilinx/Vitis-AI-Library](https://github.com/Xilinx/Vitis-AI/tree/master/Vitis-AI-Library)  
**2. Cross-compile**  
run `./build_final.sh` , you will get a compiled file `tfssdtest.so` with `ELF 64-bit LSB shared object, ARM aarch64 format`.  
Copy the compiled file to `/DEMO` for the next step .  
### [Step 5 :Evaluate this project on board](https://github.com/alex0620ee05/Self-checkout-system/tree/main/demo)  
* Following steps are on the target(ZCU104):

  If all settings are done, put the directory `demo` into `/home/root/`. 
  
**1. Revise the display resolution **  
      sh set_monitor.sh  
**2. Excute the Self-checkout-system demo**  
* You need to use the `sd_card.img` in [vcu_decode/](https://github.com/alex0620ee05/Self-checkout-system/tree/main/prebuilt/sd_card_image/vcu_decode)  
  ### Real time checkout-system with camera(Our main project):   
      python3 DEMO.py -c True 
  ### Object detection from video source:   
      python3 DEMO.py -v <mp4 video file>  
### Reference
Xilinx Vitis-AI quantizer & compiler / Xilinx Vitis-Ai-Library : [Xilinx/Vitis-AI](https://github.com/Xilinx/Vitis-AI)  
Xilinx Vitis Tutorial : [Xilinx/Vitis-In-Depth-Tutorial](https://github.com/Xilinx/Vitis-In-Depth-Tutorial/tree/master/Runtime_and_System_Optimization/Design_Tutorials/02-ivas-ml)
