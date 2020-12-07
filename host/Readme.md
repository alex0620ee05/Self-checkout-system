### This directory is for compiling tensorflow model to DPU excutable elf format by using Vitis-AI  
* Step 1 : Build Vitis-AI environment  
Follow the steps on [Vitis-AI](https://github.com/Xilinx/Vitis-AI/blob/master/README.md) to build docker.  
`./docker_run.sh xilinx/vitis-ai-gpu:latest` 
* Step 2 : Download tensorflow models from Xilinx AI model zoo  
**To download .pb file only, run `sh download_deploy_model.sh` and you can skip the following instructions in this step**  
You can get models by following the instructions on [Xilinx/Vitis-AI/AI-Model-Zoo](https://github.com/Xilinx/Vitis-AI/tree/master/AI-Model-Zoo) 
In our project , we use xilinx_model_sample/tf_ssdmobilenetv2_coco_300_300_3.75G as our object detection model.  
Copy `xilinx_model_sample/tf_ssdmobilenetv2_coco_300_300_3.75G/quantized/deploy_model.pb` to `host/ssd_mobilenet`.  
* Step 3 : Compile the tensorflow model  
After excuting`./ssdmobilenet_compile_b4096.sh`,you will get dpu_ssd_mobilenet_v2_coco_tf.elf 
