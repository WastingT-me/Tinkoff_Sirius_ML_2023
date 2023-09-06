#Hotels 50k

!mkdir hotels-50k
!wget -P hotels-50k https://github.com/GWUvision/Hotels-50K/raw/master/input/dataset.tar.gz
!tar -xvzf hotels-50k/dataset.tar.gz -C hotels-50k
!rm hotels-50k/dataset.tar.gz

#SwinIR
# Clone realESRGAN
!git clone https://github.com/xinntao/Real-ESRGAN.git
%cd Real-ESRGAN
# Set up the environment
!pip install basicsr
!pip install facexlib
!pip install gfpgan
!pip install -r requirements.txt
!python setup.py develop
# Clone BSRGAN
!git clone https://github.com/cszn/BSRGAN.git
!rm -r SwinIR
# Clone SwinIR
!git clone https://github.com/JingyunLiang/SwinIR.git
!pip install timm
# Download the pre-trained models
#!wget https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth -P experiments/pretrained_models
!wget https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth -P experiments/pretrained_models
# SwinIR is already used in AUTOMATIC1111, so we will try using SwinIR-Large
%cd /content

