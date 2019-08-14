#!/bin/bash

#$ -l rt_F=1
#$ -l h_rt=72:00:00
#$ -j y
#$ -cwd
#$ -m abe
#$ -N feats

source /etc/profile.d/modules.sh
module purge
module load cuda/9.0/9.0.176.4
module load cudnn/7.3/7.3.1
module load nccl/2.1/2.1.15-1

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv global torch
cd /home/aab10820pu/video_feature_extractor

nohup env CUDA_VISIBLE_DEVICES=0 python extract.py /groups1/gaa50131/datasets/MSR-VTT/TrainValVideo \
/groups1/gaa50131/datasets/MSR-VTT/features/r50_k700_16f resnet50 ./weights/resnet50_kinetics700.pth &> ./nohup0.out &

nohup env CUDA_VISIBLE_DEVICES=1 python extract.py /groups1/gaa50131/datasets/MSR-VTT/TestHdf5 \
/groups1/gaa50131/datasets/MSR-VTT/features/r50_k700_16f resnet50 ./weights/resnet50_kinetics700.pth &> ./nohup1.out &

nohup env CUDA_VISIBLE_DEVICES=2 python extract_ms.py /groups1/gaa50131/datasets/MSR-VTT/TrainValVideo \
/groups1/gaa50131/datasets/MSR-VTT/features/sfnl152_k700_16f slowfast152_nl slowfast152_nl ./weights/slowfast152_nl_kinetics700.pth &> ./nohup2.out &

nohup env CUDA_VISIBLE_DEVICES=3 python extract_ms.py /groups1/gaa50131/datasets/MSR-VTT/TestHdf5 \
/groups1/gaa50131/datasets/MSR-VTT/features/sfnl152_k700_16f slowfast152_nl ./weights/slowfast152_nl_kinetics700.pth &> ./nohup3.out &