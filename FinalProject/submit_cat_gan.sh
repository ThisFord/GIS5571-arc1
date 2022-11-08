#!/bin/bash -l        
#SBATCH -p k40 #selects k40 mesabi cluster
#SBATCH --gres=gpu:k40:1 #identifies the k40 gpu we want to use
#SBATCH --time=0:20:00 
#SBATCH --ntasks=10
#SBATCH --mem=48g
#SBATCH --tmp=16g
#SBATCH --mail-type=ALL  
#SBATCH --mail-user=ford0161@umn.edu 

# Where you need to make changes

# Change directory to home directory
# This makes sure we ALWAYS start in home directory and then navigate from there.
cd ~

# Change directory to advgeocomp2022
# Note you will need to make this directory AND move job.py into it...
# Note I also recommend moving this submission script into advgecomp2022 as well...
cd advgeocomp2022

# install tensorflow and other modules for processing the script

pip install --upgrade pip
pip install Pillow
module load tensorflow
pip install imageio

# Run the test python script called dcgan.py a tensorflow GAN tutorial from google collab
python3 cat_gan.py
