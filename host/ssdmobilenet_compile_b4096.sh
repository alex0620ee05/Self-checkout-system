#!/bin/bash

set -e

source /etc/profile.d/conda.sh
# Add ultra96 support
dlet -f ./project.hwh ./
sudo mkdir -p /opt/vitis_ai/compiler/arch/DPUCZDX8G/zcu104
sudo cp /workspace/ACDC/host/*.dcf /opt/vitis_ai/compiler/arch/DPUCZDX8G/zcu104/zcu104.dcf
sudo cp -f /workspace/DPU_workspace/zcu104.json /opt/vitis_ai/compiler/arch/DPUCZDX8G/zcu104/zcu104.json

# Download from model zoo; adjust this for your own model
# The contents of the extracted folder (`cf_resnet50_imagenet_224_224_7.7G`) 
# will contain multiple versions of the model:
#
#* floating point frozen graph (under `float`)
#* quantized evaluation model (under `quantized`)
#* quantized deployment model (under `quantized`)
# 
# In our case we only need the following files inside the `quantized` 
# directory:
# (1) `deploy.caffemodel` and (2) `deploy.prototxt`. 

export PYTHONPATH=/opt/vitis_ai/compiler 
export VAI_ROOT=/opt/vitis_ai
conda activate vitis-ai-tensorflow
#/workspace/hardnet39ds/deploy_model.pb \

vai_c_tensorflow \
  -f ./ssd_mobilenet/deploy_model.pb \
  -a /opt/vitis_ai/compiler/arch/DPUCZDX8G/zcu104/zcu104.json \
  -o . \
  -n ssd_mobilenet_v2_coco_tf\
  -e "{'mode':'normal','dump':'all'}"

# Activate Vitis AI conda environment
#export PYTHONPATH=/opt/vitis_ai/compiler 
#export VAI_ROOT=/opt/vitis_ai
#conda activate vitis-ai-caffe

# Call `vai_c_caffe`; adjust this for your own model
#vai_c_caffe \
#	--prototxt /workspace/host/cf_resnet50_imagenet_224_224_7.7G/quantized/deploy.prototxt \
#	--caffemodel /workspace/host/cf_resnet50_imagenet_224_224_7.7G/quantized/deploy.caffemodel \
#	--arch /opt/vitis_ai/compiler/arch/dpuv2/Ultra96/Ultra96.json \
#	--output_dir . \
#	--net_name resnet50please
