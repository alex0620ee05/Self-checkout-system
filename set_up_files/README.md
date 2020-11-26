# **Preparing the SD Card for Vitis AI Library v1.2**

* **All of following steps are on the target(ZCU104 board)**

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
    
    
You are able to run the demo on the board, please check the `README.md` of `demo/`  
