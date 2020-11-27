### This directory is for C++ cross-compilation on host, compile the DPU inference code to arm excutable format  
* Step 1 : Setting Up the Host  
Follow the steps on <https://github.com/Xilinx/Vitis-AI/tree/master/Vitis-AI-Library>  
* Step 2 : Cross-compile  
run `./build_final.sh` , you will get a compiled file `tfssdtest.so` with `ELF 64-bit LSB shared object, ARM aarch64 format`.  
Copy the compiled file to `/DEMO` for the next step .
